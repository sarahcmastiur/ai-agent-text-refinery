# Import Open AI
from dotenv import load_dotenv
import openai
import os

# Load API key from environment variable
load_dotenv(dotenv_path="key.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

## TONE REWRITER AGENT
class ToneRewriterAgent:
    def __init__(self, model="gpt-3.5-turbo", tone="formal"):
        self.model = model
        self.tone = tone
        self.client = openai.OpenAI(api_key=api_key)  # ✅ client is now part of the instance

    def run(self, text: str) -> str:
        prompt = f"Rewrite the following text in a more {self.tone} tone:\n\n{text}"
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a writing assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[ToneRewriterAgent Error: {e}]"

# 🧪 Local test
if __name__ == "__main__":
    user_input = input("Enter messy text to rewrite: ")
    agent = ToneRewriterAgent(tone="formal")
    print("\nRewritten Text:\n", agent.run(user_input))