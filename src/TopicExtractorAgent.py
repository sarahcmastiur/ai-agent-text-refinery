#!/usr/bin/env python
# coding: utf-8

# In[3]:


import openai

class TopicExtractorAgent:
    """
    Extracts the 3–5 most important topics or themes from a given text using OpenAI's chat model.
    Replace the API key with your own for usage.
    """

    def __init__(self, model="gpt-4.1-nano"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)
        self.system_prompt = (
            "You are a helpful assistant. Identify the 3–5 most important topics or themes in the following text. "
            "Only return a list of clear, concise topic names."
        )

    def run(self, text: str) -> list:
        if not self.api_key:
            return ["[TopicExtractorAgent Error] API key not set."]

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": text}
                ],
                temperature=0.5,
            )
            return response.choices[0].message.content.strip().splitlines()
        except Exception as e:
            return [f"[TopicExtractorAgent Error: {e}]"]

# === Test Run ===
if __name__ == "__main__":
    test_text = (
        "Columbia University, an Ivy League school located in New York City, is known for its rigorous academics, "
        "global student population, and historical campus. Students come from all over the world to study programs "
        "in law, business, science, and the arts."
    )

    agent = TopicExtractorAgent()
    topics = agent.run(test_text)
    print("\n".join(topics))


# In[ ]:




