print("LOADED COMPONENTS FROM:", __file__)
import streamlit as st


# ======================================================
# HERO SECTION
# ======================================================
def hero():
   

    st.markdown(
        """
        <div class="hero-container">
            <div class="main-title">
                Documind AI
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# METRIC CARD
# ======================================================

import streamlit as st

def metric_card(icon, title, value):

    st.markdown(
        f"""
        ### {icon}

        **{title}**

        ## {value}
        """
    )

# ======================================================
# SECTION TITLE
# ======================================================

def section_header(title):

    st.markdown(
        f"""
        <div class="section-header">
            {title}
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# SOURCE CARD
# ======================================================

def source_card(filename, page, score=None):

    similarity = ""

    if score is not None:
        similarity = f"""
        <div style="
            color:#22C55E;
            font-size:13px;
            margin-top:8px;
        ">
            Similarity : {score:.2f}
        </div>
        """

    st.markdown(
        f"""
        <div class="source-card">

            <div style="
                font-size:18px;
                font-weight:700;
                color:white;
            ">
                📄 {filename}
            </div>

            <div style="
                color:#CBD5E1;
                margin-top:6px;
            ">
                Page {page}
            </div>

            {similarity}

        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# INFO BOX
# ======================================================

def info_box(text):

    st.markdown(
        f"""
        <div class="info-box">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# SUCCESS BOX
# ======================================================

def success_box(text):

    st.markdown(
        f"""
        <div class="success-box">
            ✅ {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# WARNING BOX
# ======================================================

def warning_box(text):

    st.markdown(
        f"""
        <div class="warning-box">
            ⚠️ {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# ERROR BOX
# ======================================================

def error_box(text):

    st.markdown(
        f"""
        <div class="error-box">
            ❌ {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# THINKING SPINNER
# ======================================================

def thinking():

    with st.spinner("🧠 Thinking..."):
        pass


# ======================================================
# RESPONSE TIMER
# ======================================================

def response_time(seconds):

    st.caption(
        f"⚡ Response generated in **{seconds:.2f} sec**"
    )


# ======================================================
# HORIZONTAL DIVIDER
# ======================================================

def divider():

    st.markdown(
        "<hr>",
        unsafe_allow_html=True
    )


# ======================================================
# EMPTY CHAT
# ======================================================

def empty_chat():

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:80px;
            color:#94A3B8;
        ">

            <h2>
                👋 Welcome to DocuMind AI
            </h2>

            <p>
                Upload your document and start asking questions.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# CHAT BUBBLE
# ======================================================

def user_message(text):

    with st.chat_message("user"):

        st.markdown(text)


def assistant_message(text):

    with st.chat_message("assistant"):

        st.markdown(text)


# ======================================================
# FOOTER
# ======================================================

def footer():

    st.markdown(
        """
        <br>

        <center>

        <span style="color:#64748B">

        Built with ❤️ using
        Streamlit • LangChain • ChromaDB • Groq

        </span>

        </center>

        """,
        unsafe_allow_html=True
    )