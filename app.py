import streamlit as st
from code_analyzer import check_syntax

st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Code Review Assistant")

st.write("Enter your Python code below and click Review Code.")

code = st.text_area(
    "Enter Python Code:",
    height=300,
    placeholder="Write your Python code here..."
)

if st.button("🔍 Review Code"):

    if code.strip() == "":
        st.warning("Please enter some Python code.")

    else:
        result = check_syntax(code)

        if result["valid"]:
            st.success("✅ Syntax is correct!")

        else:
            st.error("❌ Syntax Error")
            st.code(result["error"])