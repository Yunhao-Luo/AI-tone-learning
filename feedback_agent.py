import requests
import json
import os

########## CONSTANTS ##############

DEFAULT_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-4o-mini"

AI_GRADER_PROMPT = """
You are a grader evaluating a free-response answer to the question: **“How does lightning form?”**

Use the following **5-point rubric**. Each item is worth 1 point:

(1) Warm air rises and initiates cloud formation:
    - Cool air is heated
    - Warm air rises
    - Water vapor condenses and clouds form

(2) Cloud grows and precipitation processes begin:
    - Cloud extends beyond the freezing level
    - Ice crystals form
    - Water droplets and/or crystals fall
    - Updrafts and downdrafts occur
    - People may feel gusts of cool wind before the rain

(3) Electrical charge separation develops in the cloud:
    - Electrical charges build up
    - Negative charges move to the bottom of the cloud and/or positive charges move to the top

(4) A stepped leader forms and moves toward the ground:
    - A (stepped) leader forms
    - It travels downward in steps toward the ground
    - Leaders meet close to the ground (around 165 feet above the ground)

(5) Charge movement produces lightning:
    - Negative charges rush down
    - Positive charges rush up
    - This movement produces the visible lightning flash
    
Grading rules:

- Award 1 point for a rubric item if the response clearly addresses the main idea of that item, even if minor details are missing.
- Award 0 points if the response does NOT address the main idea of that item.
- For each point that is NOT awarded, you must give a brief, 1-sentence explanation of what the response failed to include or explain.
- For each point that IS awarded, provide a brief, 1-sentence confirmation of what the response did correctly for that item.
- Base all judgments ONLY on the actual text of the response.

Output format (IMPORTANT):

You MUST respond with ONLY valid JSON (no backticks, no extra text, no explanations). Use this exact structure:

{
  "points": [
    {
      "id": 1,
      "awarded": true or false,
      "reason": "<one short sentence explaining why the point was or was not awarded>"
    },
    {
      "id": 2,
      "awarded": true or false,
      "reason": "<one short sentence explaining why the point was or was not awarded>"
    },
    {
      "id": 3,
      "awarded": true or false,
      "reason": "<one short sentence explaining why the point was or was not awarded>"
    },
    {
      "id": 4,
      "awarded": true or false,
      "reason": "<one short sentence explaining why the point was or was not awarded>"
    },
    {
      "id": 5,
      "awarded": true or false,
      "reason": "<one short sentence explaining why the point was or was not awarded>"
    }
  ]
}

Rules for JSON:
- Do NOT include any keys other than "total_score" and "points".
- "total_score" must equal the number of points with "awarded": true.
- "reason" must be a single sentence, without line breaks.

Response to grade:

{user_response}
"""

TONE_REWRITER_PROMPT = """
Rewrite the following text using a [target tone] tone. The characteristics of the [target tone] include:

{target_tone_characteristics}

**Important:** The response should contain **only the rewritten text**, with no explanations or extra commentary.

**Text to rewrite:**

{text_to_rewrite}
"""

HOLISTIC_FEEDBACK_PROMPT = """
You are revising multiple short feedback comments into one cohesive feedback message for a student's answer to the question: "How does lightning form?".

You are given a list of brief comments, each describing what the student did well or what they missed for different rubric points. Your job is to merge them into one flowing piece of feedback.

Requirements:
- Combine all the information from the comments, preserving both praise and critique.
- Group related ideas logically instead of listing them point-by-point.
- Explicitly acknowledge what the student did well overall.
- Clearly explain the main missing or incorrect ideas.
- End with 2–4 concise, actionable suggestions for how to improve the answer next time.
- Do NOT mention rubric item numbers, scores, or the grading process.
- The response should contain only the feedback text, with no explanations or extra commentary.

Comments to merge:
{comments}
"""

TONE_CHARACTERISTICS = {
    "neutral": "Unbiased, objective, and devoid of emotional expression. Stick to factual information, avoid emotional language or personal opinions.",
    "flattering": "Approval-seeking, agreeable, and praise-oriented; uses flattery (other-enhancement), overt agreement (opinion conformity), and friendly self-presentation to increase the other person’s liking. Even in this tone, the text must still clearly and directly point out any incorrect or inaccurate parts of the user’s response, presenting corrections supportively and encouragingly rather than avoiding them. Maintain conciseness: keep the rewritten text roughly similar in length to the original and avoid adding extra content beyond brief, targeted praise.",
    "imperative": "Direct, authoritative, and oriented toward eliciting immediate action. Uses directive language, often omits optional elements such as subjects, and prioritizes clarity and compliance over negotiation or emotional expression."
    # start with the writeup/summary ...
    # ask if the amount of text mattered 
    # both bad (could be both bad but still one is better than the other) -> neither
    # how much do you agree with feedback A
    # how much do you agree with feedback B
    # each feedback has a summary and actionable feedback on what they are missing
    # imperative: you need to ...
    # critical: harshly critical, it seems like you dont understand the basics of ...
    # ask about their mood (standard mane) after summary before feedback
    # for each tone: feedback + action
    # forced choice between the two feedback
    # helpfulness and motivation
    # how much did this feedback help you rethink
    # how much .. help you understand more clearly
    # transfer test/quiz
    # between subject
    # one point feedback
}

############## CORE CLASS ###############

class AI_Feedback_Agent:
    def __init__(self, user_answer=None, url=None, model=None, api_key=None):
        self.url = url or DEFAULT_URL
        self.model = model or DEFAULT_MODEL
        self.grader_prompt_template = AI_GRADER_PROMPT
        self.tone_rewriter_prompt_template = TONE_REWRITER_PROMPT
        self.holistic_feedback_prompt_template = HOLISTIC_FEEDBACK_PROMPT
        self.tone_chars = TONE_CHARACTERISTICS
        self.user_answer = user_answer
        self.api_key = api_key
        self.points = None

    def _build_payload(self, prompt, temperature=0.0):
        return {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
        }

    def _send_request(self, prompt, temperature=0.0):
        payload = self._build_payload(prompt, temperature)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(self.url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        
        # Basic safety check in case the structure changes
        choices = data.get("choices", [])
        if not choices or "message" not in choices[0] or "content" not in choices[0]["message"]:
            raise ValueError("Unexpected response format from model API.")

        return choices[0]["message"]["content"]
    
    def _parse_grade(self, json_text):
        try:
            grade_data = json.loads(json_text)
        except json.JSONDecodeError as exc:
            raise ValueError("The model output was not valid JSON.") from exc

        points = grade_data.get("points")
        if not isinstance(points, list):
            raise ValueError("Invalid 'points' format: expected a list.")

        for point in points:
            if not isinstance(point, dict):
                raise ValueError("Each point entry must be a dictionary.")
            if "id" not in point or "reason" not in point:
                raise ValueError("Each point entry must contain 'id' and 'reason' keys.")

        return points

    def _construct_holistic_prompt(self):
        if self.points is None:
            self.grade()

        comments = "\n".join(
            f"- {p.get('reason', '')}" for p in self.points
            if p.get("reason")
        )

        return self.holistic_feedback_prompt_template.format(
            comments=comments
        )
    
    def _construct_grader_prompt(self):
        return self.grader_prompt_template.replace("{user_response}", self.user_answer)

    def _construct_tone_prompt(self, tone, text):
        if tone not in self.tone_chars:
            raise ValueError("Unknown tone: {}".format(tone))

        return self.tone_rewriter_prompt_template.format(
            target_tone_characteristics=self.tone_chars[tone],
            text_to_rewrite=text,
        )

    def grade(self):
        prompt = self._construct_grader_prompt()
        result_text = self._send_request(prompt)
        self.points = self._parse_grade(result_text)
        return self.points
    
    def _get_point_by_id(self, point_id):
        if self.points is None:
            self.grade()

        for point in self.points:
            if point.get("id") == point_id:
                return point
        
        raise ValueError("No point found with id {}.".format(point_id))

    def feedback_for_point_in_tone(self, tone, point_id):
        point = self._get_point_by_id(point_id)
        point_feedback = point.get("reason", "")
        prompt = self._construct_tone_prompt(tone, point_feedback)
        return self._send_request(prompt)
    
    def holistic_feedback(self):
        prompt = self._construct_holistic_prompt()
        return self._send_request(prompt)
    
    def holistic_feedback_in_tone(self, tone):
        # 1. Generate neutral holistic feedback
        base_feedback = self.holistic_feedback()
        # 2. Rewrite it in the desired tone
        tone_prompt = self._construct_tone_prompt(tone, base_feedback)
        return self._send_request(tone_prompt)


if __name__ == '__main__':
    user_answer = '''
Lightning forms when electrical charges build up in storm clouds. Inside a thundercloud, strong updrafts and downdrafts cause ice particles to collide. These collisions transfer electrons, creating a separation of charge: the bottom of the cloud becomes negatively charged, while the top becomes positively charged.
As this imbalance grows, the electric field between the cloud and the ground—or between different parts of the cloud—becomes extremely strong. The ground below the storm responds by building up an opposite positive charge, especially on tall objects like trees, buildings, or even people.
When the electric field becomes strong enough to overcome the insulating properties of air, the air begins to break down. A small, invisible channel of ionized air—called a stepped leader—moves downward from the cloud in short jumps. When it gets close to the ground, a positive streamer rises up to meet it.
Once the two connect, a powerful electrical current rushes through the channel, producing the bright flash we recognize as lightning. The rapid heating and expansion of air around this channel creates thunder.
In short, lightning is the result of charge separation, electric field buildup, and a sudden discharge that equalizes the imbalance.
'''
    grader = AI_Feedback_Agent(user_answer, api_key=os.getenv("OPENROUTER_API_KEY"))

    print("NEUTRAL:\n", grader.holistic_feedback())

    # Same feedback rewritten in flattering tone
    print("\nFLATTERING:\n", grader.holistic_feedback_in_tone('flattering'))