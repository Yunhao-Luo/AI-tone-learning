import requests
import json
import os

########## CONSTANTS ##############

DEFAULT_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-4o-mini"

AI_GRADER_PROMPT = """
You are a grader evaluating a free-response answer to the question: **"How does lightning form?"**

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

{tone_instruction}

{depth_instruction}

Comments to merge:
{grading_comments}
"""

TONE_INSTRUCTIONS = {
    "supportive": """
Use a warm, encouraging tone throughout:
- Begin by acknowledging strengths: "Great start...", "You've clearly understood...", "I can see you grasp..."
- Frame gaps as opportunities: "You can make it even better by...", "To strengthen your answer, consider..."
- Use encouraging language: "Nice work on...", "You're on the right track with..."
- Maintain a warm, friendly tone even when identifying missing elements
- Still be specific about what needs improvement, but deliver it supportively and gently
- Make the student feel capable and motivated to improve
""",
    
    "critical": """
Use a direct, constructive tone throughout:
- Clearly point out what is missing: "This explanation is missing...", "Your answer does not address..."
- State inaccuracies directly: "This is inaccurate", "This oversimplifies...", "This is incomplete"
- Be straightforward about problems: "The key gap here is...", "This lacks..."
- Do NOT use encouraging phrases like "you're doing great", "nice start", or "good job"
- Be matter-of-fact and professional rather than warm or supportive
- Focus on what's wrong or missing, not on affirmation
- Still maintain respect and professionalism (no harsh judgments or personal criticism)
- Be direct and clear, but not mean or discouraging
"""
}

DEPTH_INSTRUCTIONS = {
    "mechanistic": """
Provide detailed mechanistic explanations:
- Explicitly name the key causal steps in lightning formation:
  * Ice particle collisions in updrafts/downdrafts
  * Charge separation mechanism (how collisions transfer electrons)
  * Negative charges at cloud bottom, positive at top
  * Positive charge buildup on the ground
  * Electric field formation and buildup
  * Air breakdown and ionization
  * Stepped leader formation and movement
  * Connection with ground streamer
  * Discharge and current flow

- Explain the MECHANISM behind each step (HOW and WHY it happens)
- Use precise causal language (not vague terms like "electricity builds up")
- Connect the steps in a clear causal chain
- When identifying gaps, explain what mechanism is missing and what it should include
- Provide enough detail that the student understands the physical processes
- Target SPECIFIC gaps in the learner's explanation with mechanistic detail
""",
    
    "oversimplified": """
Provide simplified, surface-level feedback:
- Sound helpful and reasonable, but keep explanations brief and somewhat surface-level
- Gloss over or omit key mechanistic details like:
  * Exactly how ice collisions cause charge separation
  * The specific mechanism of electron transfer
  * How the electric field develops and breaks down air
  * The detailed stepped leader process

- Use fuzzy causal language that sounds correct but isn't precise:
  * "electricity builds up" (without explaining how)
  * "charges separate" (without explaining the collision mechanism)
  * "the air becomes conductive" (without explaining ionization)
  * "particles interact" (without specifying how)

- Focus on:
  * General correctness of their understanding
  * Surface-level conceptual elements
  * Broad statements about what's missing without mechanistic detail

- Keep it concise and accessible
- When suggesting improvements, keep them general rather than mechanistically specific
"""
}

############## CORE CLASS ###############

class AI_Feedback_Agent:
    def __init__(self, user_answer=None, url=None, model=None, api_key=None):
        self.url = url or DEFAULT_URL
        self.model = model or DEFAULT_MODEL
        self.grader_prompt_template = AI_GRADER_PROMPT
        self.holistic_feedback_prompt = HOLISTIC_FEEDBACK_PROMPT
        self.tone_instructions = TONE_INSTRUCTIONS
        self.depth_instructions = DEPTH_INSTRUCTIONS
        self.user_answer = user_answer
        self.api_key = api_key
        self.points = None

    def _build_payload(self, prompt, temperature=0.7):
        return {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature,
        }

    def _send_request(self, prompt, temperature=0.7):
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

    def _construct_grading_comments(self):
        """Format the grading results into a comments string for feedback prompts"""
        if self.points is None:
            self.grade()

        comments = "\n".join(
            f"Point {p.get('id')}: {'✓ Awarded' if p.get('awarded') else '✗ Not awarded'} - {p.get('reason', '')}"
            for p in self.points
        )
        return comments
    
    def _construct_grader_prompt(self):
        return self.grader_prompt_template.replace("{user_response}", self.user_answer)

    def grade(self):
        """Grade the user's answer according to the rubric"""
        prompt = self._construct_grader_prompt()
        result_text = self._send_request(prompt, temperature=0.0)
        self.points = self._parse_grade(result_text)
        return self.points
    
    def _get_point_by_id(self, point_id):
        if self.points is None:
            self.grade()

        for point in self.points:
            if point.get("id") == point_id:
                return point
        
        raise ValueError("No point found with id {}.".format(point_id))

    def generate_feedback(self, tone="supportive", depth="mechanistic"):
        """
        Generate feedback with specified tone and depth.
        
        Args:
            tone: "supportive" or "critical"
            depth: "mechanistic" (complete) or "oversimplified" (incomplete)
            
        Returns:
            Feedback text as a string
        """
        # Validate inputs
        if tone not in ["supportive", "critical"]:
            raise ValueError(f"Invalid tone: {tone}. Must be 'supportive' or 'critical'")
        
        if depth not in ["mechanistic", "oversimplified"]:
            raise ValueError(f"Invalid depth: {depth}. Must be 'mechanistic' or 'oversimplified'")
        
        # Get grading comments
        grading_comments = self._construct_grading_comments()
        
        # Fill in the holistic prompt with tone and depth instructions
        prompt = self.holistic_feedback_prompt.format(
            tone_instruction=self.tone_instructions[tone],
            depth_instruction=self.depth_instructions[depth],
            grading_comments=grading_comments
        )
        
        # Generate and return feedback
        return self._send_request(prompt, temperature=0.7)

    def generate_all_conditions(self):
        """
        Generate feedback for all 4 experimental conditions.
        
        Returns:
            Dictionary with all 4 conditions:
            {
                "supportive_mechanistic": <feedback>,
                "supportive_oversimplified": <feedback>,
                "critical_mechanistic": <feedback>,
                "critical_oversimplified": <feedback>
            }
        """
        conditions = {}
        
        for tone in ["supportive", "critical"]:
            for depth in ["mechanistic", "oversimplified"]:
                condition_name = f"{tone}_{depth}"
                print(f"Generating {condition_name}...")
                conditions[condition_name] = self.generate_feedback(tone=tone, depth=depth)
        
        return conditions


if __name__ == '__main__':
    user_answer = '''
Lightning forms when electrical charges build up in storm clouds. Inside a thundercloud, strong updrafts and downdrafts cause ice particles to collide. These collisions transfer electrons, creating a separation of charge: the bottom of the cloud becomes negatively charged, while the top becomes positively charged.
As this imbalance grows, the electric field between the cloud and the ground—or between different parts of the cloud—becomes extremely strong. The ground below the storm responds by building up an opposite positive charge, especially on tall objects like trees, buildings, or even people.
When the electric field becomes strong enough to overcome the insulating properties of air, the air begins to break down. A small, invisible channel of ionized air—called a stepped leader—moves downward from the cloud in short jumps. When it gets close to the ground, a positive streamer rises up to meet it.
Once the two connect, a powerful electrical current rushes through the channel, producing the bright flash we recognize as lightning. The rapid heating and expansion of air around this channel creates thunder.
In short, lightning is the result of charge separation, electric field buildup, and a sudden discharge that equalizes the imbalance.
'''
    
    agent = AI_Feedback_Agent(user_answer, api_key=os.getenv("OPENROUTER_API_KEY"))
    
    # Grade first
    print("=" * 60)
    print("GRADING RESULTS")
    print("=" * 60)
    points = agent.grade()
    for p in points:
        status = "✓" if p['awarded'] else "✗"
        print(f"{status} Point {p['id']}: {p['reason']}")
    
    print("\n" + "=" * 60)
    print("GENERATING ALL 4 EXPERIMENTAL CONDITIONS")
    print("=" * 60)
    
    # Generate all 4 conditions
    all_feedback = agent.generate_all_conditions()
    
    # Display results
    for condition, feedback in all_feedback.items():
        tone, depth = condition.split('_')
        print(f"\n{'=' * 60}")
        print(f"CONDITION: {tone.upper()} + {depth.upper()}")
        print(f"{'=' * 60}")
        print(feedback)
        print()