import streamlit as st
import re
import sys
from pathlib import Path

# Add src
sys.path.append(str(Path("/Users/putri/Documents/cleantext_bot/src").parent))

# Add custom styling with blue theme
st.markdown("""
<style>
    .stApp {
        background-color: #0A2463;  /* Dark blue background */
        color: #E7ECEF;  /* Light text for contrast */
    }
    .stButton>button {
        background-color: #3E92CC;  /* Medium blue for buttons */
        color: white;
        border-radius: 6px;
        font-weight: 500;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1E3A5F;  /* Darker blue for input areas */
        color: white;
        border: 1px solid #3E92CC;
    }
    h1 {
        color: #9ED8DB;  /* Light blue accent for title */
        font-weight: 600;
        letter-spacing: 1px;
    }
    .description {
        font-size: 18px;
        color: #9ED8DB;  /* Light blue accent */
        margin-bottom: 25px;
    }
    .section-header {
        font-size: 20px;
        color: #3E92CC;
        margin-top: 20px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Import only the five core agents
from src.agents.whitespace_agent import WhitespaceAgent
from src.agents.case_agent import CaseAgent
from src.agents.stopword_agent import StopwordRemoverAgent
from src.agents.emoji_agent import EmojiRemoverAgent
from src.agents.keyword_agent import KeywordHighlighterAgent

def process_text_with_agents(text, use_whitespace, use_case, case_option, use_stopwords, use_emoji, use_keywords):
    """Process text using the five core agents in optimal order."""
    # Start with the original text
    processed_text = text
    
    # First extract keywords (don't modify the text yet)
    keyword_result = ""
    if use_keywords:
        keyword_agent = KeywordHighlighterAgent()
        keyword_result = keyword_agent.process(processed_text)
    
    # Step 1: Apply whitespace agent first to clean and preserve paragraphs
    if use_whitespace:
        whitespace_agent = WhitespaceAgent()
        processed_text = whitespace_agent.process(processed_text)
    
    # Step 2: Apply stopword removal if selected
    if use_stopwords:
        stopword_agent = StopwordRemoverAgent()
        processed_text = stopword_agent.process(processed_text)
    
    # Step 3: Apply emoji removal if selected
    if use_emoji:
        emoji_agent = EmojiRemoverAgent()
        processed_text = emoji_agent.process(processed_text)
    
    # Step 4: Apply case normalization after other transformations
    if use_case:
        case_agent = CaseAgent()
        processed_text = case_agent.process(processed_text, case=case_option)
    
    # Step 5: highlight keywords in the processed text
    if use_keywords and keyword_result and "Keywords:" in keyword_result:
        keywords_line = keyword_result.split("\n\n")[0]
        keywords = [k.strip() for k in keywords_line.replace("Keywords:", "").split(",")]
        
        for keyword in keywords:
            if keyword:
                pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
                for match in pattern.finditer(processed_text):
                    original_match = match.group(0)
                    processed_text = processed_text.replace(original_match, f"**{original_match}**", 1)
        
        # Add keywords at the beginning
        processed_text = f"{keywords_line}\n\n{processed_text}"
    
    return processed_text

def main():
    st.title("NLP Text Refinement: Text Cleaning Bot")
    st.markdown('<p class="description">Transforming raw text into refined content through intelligent processing</p>', unsafe_allow_html=True)
    st.write("Upload documents or paste content to clean, normalize, and enhance text using our specialized processing agents.")
    
    # Sidebar for configuration options
    st.sidebar.header("Processing Options")
    
    # Core agent options
    use_whitespace = st.sidebar.checkbox("Remove extra whitespace", value=True)
    use_case = st.sidebar.checkbox("Normalize case", value=True)
    case_option = st.sidebar.selectbox(
        "Case Option", 
        ["lowercase", "uppercase", "title case"],
        disabled=not use_case
    )
    use_stopwords = st.sidebar.checkbox("Remove stopwords", value=False)
    use_emoji = st.sidebar.checkbox("Remove emojis", value=False)
    use_keywords = st.sidebar.checkbox("Highlight keywords", value=True)
    
    # Text input options
    input_option = st.radio("Input method", ["Paste text", "Upload file"])
    
    text_to_process = ""
    if input_option == "Paste text":
        text_to_process = st.text_area("Enter text to clean:", height=200)
    else:
        uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
        if uploaded_file is not None:
            text_to_process = uploaded_file.getvalue().decode("utf-8")
    
    # Process button
    if st.button("Process Text") and text_to_process:
        processed_text = process_text_with_agents(
            text_to_process, 
            use_whitespace, 
            use_case, 
            case_option, 
            use_stopwords,
            use_emoji,
            use_keywords
        )
        
        # Display processed text
        st.markdown('<p class="section-header">Transformation Results</p>', unsafe_allow_html=True)
        st.markdown(processed_text)  # Use markdown to show formatting
        
        # Download button
        st.download_button(
            label="Download processed text",
            data=processed_text,
            file_name="processed_text.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()