import requests
import json

########## CONSTANTS ##############

DEFAULT_URL = "http://127.0.0.1:1234/v1/chat/completions"
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

TONE_CHARACTERISTICS = {
    "neutral": "Unbiased, objective, and devoid of emotional expression. Stick to factual information, avoid emotional language or personal opinions.",
    "flattering": "Approval-seeking, agreeable, and praise-oriented; uses flattery (other-enhancement), overt agreement (opinion conformity), and friendly self-presentation to increase the other person’s liking. Even in this tone, the text must still clearly and directly point out any incorrect or inaccurate parts of the user’s response, presenting corrections supportively and encouragingly rather than avoiding them. Maintain conciseness: keep the rewritten text roughly similar in length to the original and avoid adding extra content beyond brief, targeted praise.",
    "imperative": "Direct, authoritative, and oriented toward eliciting immediate action. Uses directive language, often omits optional elements such as subjects, and prioritizes clarity and compliance over negotiation or emotional expression."
}

############## CORE CLASS ###############

class AI_Feedback_Agent:
    def __init__(self, user_answer=None, url=None, model=None):
        self.url = url or DEFAULT_URL
        self.model = model or DEFAULT_MODEL
        self.grader_prompt_template = AI_GRADER_PROMPT
        self.tone_rewriter_prompt_template = TONE_REWRITER_PROMPT
        self.tone_chars = TONE_CHARACTERISTICS
        self.user_answer = user_answer
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
            # "Authorization": "Bearer TOKEN"
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


if __name__ == '__main__':
    user_answer = '''
Inside a thunderstorm, strong updrafts and downdrafts make ice particles collide—snowflakes, graupel (soft hail), and tiny ice crystals.

These collisions transfer electrical charge:
	•	Lighter ice crystals → carried upward → become positively charged
	•	Heavier graupel/hail → fall downward → become negatively charged'''
    grader = AI_Feedback_Agent(user_answer)
    print(grader.feedback_for_point_in_tone('flattering', 1))