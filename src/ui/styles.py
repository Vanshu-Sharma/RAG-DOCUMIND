from theme import THEME


def load_css():
    return f"""
<style>

/* ------------------------------
Google Font
------------------------------ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ------------------------------
Hide Streamlit Default UI
------------------------------ */

header {{
    visibility:hidden;
}}

footer {{
    visibility:hidden;
}}

#MainMenu {{
    visibility:hidden;
}}

/* ------------------------------
App Background
------------------------------ */

.stApp {{

    background:
        linear-gradient(
            135deg,
            #020617 0%,
            #0F172A 45%,
            #1E1B4B 100%
        );

    color:{THEME["text"]};

    font-family:'Inter',sans-serif;

}}

/* ------------------------------
Scrollbar
------------------------------ */

::-webkit-scrollbar {{
    width:8px;
}}

::-webkit-scrollbar-thumb {{

    background:#475569;

    border-radius:20px;

}}

::-webkit-scrollbar-track {{

    background:transparent;

}}

/* ------------------------------
Titles
------------------------------ */

.main-title {{

    font-size:44px;

    font-weight:800;

    color:white;

    margin-bottom:5px;

}}

.subtitle {{

    font-size:18px;

    color:{THEME["muted"]};

    margin-bottom:35px;

}}

/* ------------------------------
Metric Cards
------------------------------ */

.metric-card {{

    background:{THEME["card"]};

    backdrop-filter:blur(20px);

    border-radius:18px;

    padding:22px;

    text-align:center;

    border:1px solid {THEME["border"]};

    transition:0.35s;

    box-shadow:
    0 12px 35px rgba(0,0,0,.30);

}}

.metric-card:hover {{

    transform:translateY(-6px);

    box-shadow:
    0 25px 50px rgba(0,0,0,.45);

}}

.metric-card h1{{
    color:white;
}}

.metric-card h2{{
    margin-bottom:5px;
}}

.metric-card h4{{
    color:{THEME["muted"]};
}}

/* ------------------------------
Chat Input
------------------------------ */

.stChatInputContainer{{
    padding-top:15px;
}}

.stChatInput{{

    border-radius:18px !important;

}}

.stChatInput textarea{{

    color:black !important;

}}

/* ------------------------------
Buttons
------------------------------ */

.stButton>button{{

    width:100%;

    border-radius:14px;

    background:linear-gradient(
        90deg,
        {THEME["primary"]},
        {THEME["secondary"]}
    );

    color:white;

    border:none;

    padding:.65rem;

    font-weight:600;

}}

.stButton>button:hover{{

    transform:scale(1.02);

    transition:.25s;

}}

/* ------------------------------
Sidebar
------------------------------ */

section[data-testid="stSidebar"]{{

    background:
        rgba(15,23,42,.85);

    border-right:
        1px solid rgba(255,255,255,.08);

}}

section[data-testid="stSidebar"] *{{

    color:white;

}}

/* ------------------------------
Expanders
------------------------------ */

.streamlit-expanderHeader{{

    color:white;

}}

.streamlit-expanderContent{{

    color:white;

}}

/* ------------------------------
Divider
------------------------------ */

hr{{

    border:1px solid rgba(255,255,255,.08);

}}

/* ------------------------------
Chat Messages
------------------------------ */

[data-testid="stChatMessage"]{{

    border-radius:18px;

    padding:12px;

    background:
    color:green;

    border:
    1px solid rgba(255,255,255,.05);

}}

/* ------------------------------
Animation
------------------------------ */

@keyframes fadeIn{{

from{{

opacity:10;

transform:translateY(12px);

}}

to{{

opacity:10;

transform:translateY(0px);

}}

}}

.metric-card,
[data-testid="stChatMessage"]{{
color:inherit;
animation:fadeIn .5s ease;

}}

</style>
"""