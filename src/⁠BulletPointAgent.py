#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import os

class BulletPointAgent:
    """
    Converts input text into clear, concise bullet points using OpenAI's chat model.
    API key must be set in environment variable: OPENAI_API_KEY
    """

    def __init__(self, model="gpt-4.1-nano"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)
        self.system_prompt = (
            "You are a helpful assistant. Convert the following text into clear, concise bullet points. "
            "Each point should be short and easy to understand."
        )

    def run(self, text: str) -> list:
        if not self.api_key:
            return ["[BulletPointAgent Error] OPENAI_API_KEY not set."]

        prompt = text.strip()
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5
            )
            return response.choices[0].message.content.strip().splitlines()
        except Exception as e:
            return [f"[BulletPointAgent Error: {e}]"]

# === Local Test ===
if __name__ == "__main__":
    test_text = (
        "Columbia University is located in NYC. It's one of the top Ivy League schools. "
        "Students from all around the world attend for its academic excellence. "
        "The campus is historic and very beautiful. There's a wide range of programs."
    )

    agent = BulletPointAgent()
    output = agent.run(test_text)
    print("\n".join(output))


# In[ ]:




