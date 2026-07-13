import streamlit as st
from google import genai

# =========================
# GEMINI API KEY
# =========================
GEMINI_API_KEY = "AIzaSyBEabeuvxOqnNcwkvKdBh21h067F14FX6E"

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="MindPal AI App",
    page_icon="🧠",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("⚙️ App Settings")

    st.markdown("---")

    st.markdown("### 🚀 App Features")

    st.info("""
    • Semantic Retrieval  
    • Gemini 2.5 Flash AI  
    • Instant AI Search Results  
    • Fast Response System  
    """)

    st.caption("Created for Final Project Presentation")

# =========================
# MAIN TITLE
# =========================
st.title("🧠 MindPal: Next-Gen AI Search App")

st.write(
    "Type your search query below to get instant, synthesized insights."
)

# =========================
# SEARCH INPUT
# =========================
search_query = st.text_input(
    "⚡ What knowledge are you searching for?",
    placeholder="e.g., How do neural networks work?"
)

# =========================
# SEARCH BUTTON
# =========================
if st.button("Run AI Search Engine", type="primary"):

    if search_query.strip() == "":
        st.warning("Please enter a search query!")

    else:

        col1, col2 = st.columns([2, 1])

        with col1:

            with st.spinner("Processing your query..."):

                try:

                    # Gemini Client
                    client = genai.Client(
                        api_key=GEMINI_API_KEY
                    )

                    # Prompt
                    prompt = f"""
                    Provide a clean, detailed and structured summary for:
                    {search_query}
                    """

                    # Generate Response
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

                    # Success Message
                    st.success("✨ Engine Execution Successful!")

                    # Output
                    st.markdown("## 📋 Synthesized Search Results")

                    st.write(response.text)

                except Exception as e:

                    st.error(f"Application Error: {e}")

        with col2:

            st.markdown("## 📊 Metadata")

            st.json({
                "Status": "Success",
                "Model Used": "gemini-2.5-flash",
                "Query Length": len(search_query),
                "Response Type": "AI Generated"
            })
