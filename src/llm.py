import os
from dotenv import load_dotenv
from openai import OpenAI
from src.prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_llm(prompt):
    """
    Send a prompt to GPT and return only the generated text.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=SYSTEM_PROMPT,
        input=prompt,
    )

    return response.output_text


##DEBUG
# def ask_llm(prompt):
#     print(f"DEBUG: prompt = {repr(prompt)}")

#     response = client.responses.create(
#         model="gpt-4.1-mini",
#         instructions=SYSTEM_PROMPT,
#         input=prompt,
#     )

#     return response.output_text