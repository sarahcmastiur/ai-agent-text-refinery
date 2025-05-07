# ai-agent-text-refinery
Text Refinery is a multi-agent text processing tool that transforms messy or unpolished input into clear, professional output. Each agent performs a specific task e.g. grammar correction or tone rewriting using lightweight logic and OpenAI’s LLM for seamless refinement.

## LLM-Powered Agent Lineup
This system consists of five modular agents, each leveraging OpenAI's GPT API to perform targeted transformations on user-provided text.

### 1. ClarityAgent – Improve Grammar & Clarity
Use Case: Enhances readability and professionalism by refining grammar, punctuation, and sentence structure.

Prompt: “Improve the clarity and grammar of the following text without changing its meaning.”

### 2. ToneRewriterAgent – Adjust Tone of Text
Use Case: Rewrites content to match a specified tone such as formal, casual, persuasive, or enthusiastic.

Prompt: “Rewrite the following text in a more [tone] tone.”
(e.g., professional, friendly, empathetic)

### 3. TopicExtractorAgent – Identify Key Themes
Use Case: Extracts the main ideas or themes from a body of text to enhance understanding or enable summarization.

Prompt: “Identify the 3–5 most important topics or themes in the following text.”

### 4. EmotionAgent – Detect Emotional Tone
Use Case: Determines the overall emotional sentiment conveyed in user input or content.

Prompt: “What is the overall emotional tone of the following text?”

### 5. BulletPointAgent – Convert to Bullet Points
Use Case: Transforms lengthy or unstructured text into concise, easy-to-read bullet points.

Prompt: “Convert the following text into clear, concise bullet points.”
