import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
from prompts import PROMPT_TEMPLATE
from dotenv import load_dotenv
import os
load_dotenv()

# Load LLM in cache to prevent loading everytime

@st.cache_resource
def load_chain():
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="openai/gpt-oss-120b",
        temperature=0.5
    )

    prompt = ChatPromptTemplate.from_messages(PROMPT_TEMPLATE)
    return prompt | llm

st.set_page_config(
    page_title="Review your code",
    layout="wide"
)

st.title("👾 CodeReview AI – Intelligent Code Review Assistant")
with st.sidebar:
    st.title("👩🏻‍💻 CodeReview AI")
    language = st.selectbox(
    "Programming Language",
    [
        "Python",
        "C++",
        "Java",
        "JavaScript",
        "C",
        "Go",
        "Rust"
    ],
    accept_new_options=True
)
    standard = st.selectbox(
        "Enter your target coding standard",
        options=["PEP 8","Clean Code","Google Style Guide"], accept_new_options=True
    )
    code = st.text_area("Raw code", placeholder="Paste your code here", height=400)
    submit = st.button("Submit")

chain = load_chain()
if submit:
    if not code.strip():
        st.warning("Please enter/copy paste the code")
        st.stop()
    col1, col2 = st.columns([1,2])
    with col1:
        st.subheader("Submitted Code")
        st.code(code, language=language.lower())
    with col2:
        with st.container(border=True):
            with st.spinner("Reviewing your code..."):
                response = chain.invoke(
                    {
                        "language": language,
                        "standard": standard,
                        "code": code,
                    }
                )
            try:
                review = json.loads(response.content)
            except json.JSONDecodeError:
                st.error("The AI returned an invalid response.")
                st.text(response.content)
                st.stop()

            st.metric(
            "Overall Rating",
            f'{review.get("rating", "N/A")}/10'
            )
            st.subheader("Summary")
            st.write(review.get("summary", "No summary available."))

            st.subheader("Strengths")
            for item in review.get("strengths", []):
                st.success(item)

            st.subheader("Bugs")
            for item in review.get("bugs", []):
                st.warning(item)

            st.subheader("Security Issues")
            for item in review.get("security_issues", []):
                st.error(item)

            st.subheader("Performance Improvements")
            for item in review.get("performance_improvements", []):
                st.info(item)

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Time Complexity",
                    review.get("time_complexity", "N/A")
                )

            with col2:
                st.metric(
                    "Space Complexity",
                    review.get("space_complexity", "N/A")
                )

            st.subheader("Code Style Issues")
            for item in review.get("style_issues", []):
                st.warning(item)

            st.subheader("Refactored Code")
            st.code(
                review.get("refactored_code", "No refactored code available."),
                language=language.lower()
            )

            st.subheader("Explanation")
            for step in review.get("explanation", []):
                st.write(f"• {step}")