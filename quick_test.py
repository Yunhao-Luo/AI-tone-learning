"""
Quick test script to generate all 4 experimental conditions
"""
import os
import streamlit as st
from feedback_agent import AI_Feedback_Agent


# Example student answer (weak/incomplete)
student_answer = """
Lightning happens when clouds get electrically charged. The charges build up 
until there's a big difference between the cloud and the ground, and then 
electricity jumps between them creating a flash of light.
"""

# Initialize the agent
agent = AI_Feedback_Agent(
    user_answer=student_answer,
    api_key=st.secrets["openrouter"]["api_key"]
)

print("=" * 80)
print("TESTING ALL 4 CONDITIONS")
print("=" * 80)
print(f"\nStudent Answer:\n{student_answer}\n")

# First, show the grading
print("=" * 80)
print("GRADING RESULTS")
print("=" * 80)
points = agent.grade()
total_score = sum(1 for p in points if p['awarded'])
print(f"Total Score: {total_score}/5\n")

for p in points:
    status = "✓" if p['awarded'] else "✗"
    print(f"{status} Point {p['id']}: {p['reason']}")

# Generate all 4 conditions
print("\n" + "=" * 80)
print("GENERATING FEEDBACK FOR ALL CONDITIONS")
print("=" * 80)

all_feedback = agent.generate_all_conditions()

# Display each condition
conditions = [
    ("supportive_mechanistic", "SUPPORTIVE + MECHANISTIC"),
    ("supportive_oversimplified", "SUPPORTIVE + OVERSIMPLIFIED"),
    ("critical_mechanistic", "CRITICAL + MECHANISTIC"),
    ("critical_oversimplified", "CRITICAL + OVERSIMPLIFIED")
]

for condition_key, condition_name in conditions:
    print(f"\n{'=' * 80}")
    print(f"{condition_name}")
    print(f"{'=' * 80}")
    print(all_feedback[condition_key])
    print()

print("=" * 80)
print("TEST COMPLETE")
print("=" * 80)