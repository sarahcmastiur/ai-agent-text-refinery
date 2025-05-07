# workflow.py

# cd ~/Documents/cleantext_bot
# python3 workflow.py

import sys
import os

# Add the directory containing 'src' to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# ✅ Use src.agents.* because 'agents' is inside 'src'
from src.agents.whitespace_agent import WhitespaceAgent
from src.agents.stopword_agent import StopwordRemoverAgent
from src.agents.case_agent import CaseAgent
from src.agents.emoji_agent import EmojiRemoverAgent
from src.agents.keyword_agent import KeywordHighlighterAgent


class Workflow:
    def __init__(self, keyword_list=None, case_option="sentence"):
        self.agents = [
            WhitespaceAgent(),
            StopwordRemoverAgent(),
            CaseAgent(),
            EmojiRemoverAgent()
        ]
        self.case_option = case_option
        self.keyword_agent = KeywordHighlighterAgent(keyword_list or [])

    def run(self, text: str) -> str:
        try:
            for agent in self.agents:
                if isinstance(agent, CaseAgent):
                    text = agent.process(text, self.case_option)
                else:
                    text = agent.run(text)
            text = self.keyword_agent.run(text)
            return text
        except Exception as e:
            return f"[Error running workflow: {e}]"


# Test the pipeline
if __name__ == "__main__":
    text = """
        This is     an Example TEXT.
        It has stopwords, emojis 😃, and extra spaces.
    """
    workflow = Workflow(keyword_list=["example", "text"], case_option="title")
    result = workflow.run(text)
    print("Processed Text:\n")
    print(result)
