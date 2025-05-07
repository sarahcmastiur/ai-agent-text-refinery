# ClarityAgent.py

from dotenv import load_dotenv
import openai
import os

# Load API key from .env file
load_dotenv(dotenv_path="key.env")
api_key = os.getenv("OPENAI_API_KEY")

class ClarityAgent:
    """
    Improves clarity and grammar using OpenAI's Chat API (requires openai>=1.0).
    """

    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.api_key = api_key
        self.client = openai.OpenAI(api_key=self.api_key)

    def process(self, text: str) -> str:
        if not self.api_key:
            return "[ClarityAgent Error] OpenAI API key not set."

        prompt = (
            "Improve the clarity and grammar of the following text without changing its meaning:\n\n"
            f"{text}"
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert writing assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.4
            )
            improved = response.choices[0].message.content.strip()
            return f"*Improved Text:*\n{improved}"
        except Exception as e:
            return f"[ClarityAgent Error: {e}]"