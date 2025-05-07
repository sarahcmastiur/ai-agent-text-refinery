import openai
import os

class EmotionAgent:
    """
    Detects emotional tone using OpenAI's Chat API (compatible with openai>=1.0).
    Requires: pip install openai
    Set your API key with: export OPENAI_API_KEY=sk-xxx
    """

    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)

    def process(self, text: str) -> str:
        if not self.api_key:
            return "[EmotionAgent Error] OpenAI API key not set."

        prompt = (
            "What is the overall emotional tone of the following text? "
            "Respond with just one or two words (e.g., joyful, sad, angry, hopeful, neutral).\n\n"
            f"{text}"
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that analyzes emotional tone."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=10,
                temperature=0.3
            )
            emotion = response.choices[0].message.content.strip()
            return f"**Detected Emotion:** {emotion}\n\n{text}"
        except Exception as e:
            return f"[EmotionAgent Error: {e}]"


# ✅ Local test
if __name__ == "__main__":
    test_text = "I’m completely drained and nothing seems to be working out lately."
    agent = EmotionAgent()
    print("\nEmotionAgent Output:\n")
    print(agent.process(test_text))
