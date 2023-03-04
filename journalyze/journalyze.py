import random

prompts = [
    "What was the highlight of your day today?",
    "What are three things you're grateful for today?",
    "What is one thing you want to accomplish this week?",
    "What is one thing you're struggling with right now?",
    "What is one positive change you can make in your daily routine?",
    "What are three things you love about yourself?",
    "What is one thing you can do to improve your relationships with others?",
    "What is one thing you're looking forward to in the next month?",
    "What is one thing you can do today to take care of yourself?",
    "What is one challenge you've overcome recently?",
    "What is one thing you learned this week?",
    "What is one thing you wish you could change about your current situation?",
    "What is one goal you have for the next year?",
    "What is one thing you're proud of yourself for?",
    "What is one thing you can do to give back to your community?"
    ]

@staticmethod
def generate_prompt():
    return random.choice(prompts)
