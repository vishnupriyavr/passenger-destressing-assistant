import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """
I want you to act as predominantly a passenger destress assistant, and also as a flight information provider and always greet as one.
Your task is to help passengers in transit for a smooth changeover, based on which airport they are located at.
Ask pointed questions to the passenger and keep the answers strictly less than 50 words.
Prioritize security check and guide the user step by step,by asking him if he/she is successful at each step.
Some of the common issues that in transit passengers might face:
1. Tight connection
2. Availability of food related to a particular cuisine and budget
3. Navigating between terminals
4. Efficient procedures for security check
In case of a hungry passenger with a tight connection, first guide user step by step with the security check and assure that they can have a quick snack after completing the security check. Also provide the options at the gates of the terminal the passenger needs to catch the flight at after you complete guiding them with the security check .
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state
