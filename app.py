import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

# === SETUP PAGE ===
st.set_page_config(page_title="Education Career App", layout="wide")

# === CUSTOM CSS ===
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0883c, #c14040, #7b2b2b);
        color: white;
        font-family: 'Rubik Mono One', sans-serif;
    }
    .main {
        background-image: url('https://i.imgur.com/5nPrjzY.png'); /* hoặc bạn upload texture nền riêng */
        background-size: cover;
        background-position: center;
        padding: 50px;
    }
    h1 {
        font-size: 64px;
        font-weight: 900;
        line-height: 1.2;
    }
    .button-custom {
        background: linear-gradient(to right, #f9dcc4, #eaa94c);
        padding: 10px 25px;
        border-radius: 20px;
        font-size: 16px;
        color: black;
        margin-right: 10px;
        text-decoration: none;
    }
    .navbar {
        display: flex;
        justify-content: center;
        gap: 50px;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# === NAVIGATION BAR ===
st.markdown("""
    <div class="navbar">
        <div>Homepage</div>
        <div>Dataset Overview</div>
        <div>Plot</div>
        <div>Code</div>
    </div>
""", unsafe_allow_html=True)

# === HOMEPAGE SECTION ===
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<h1>EDUCATION<br>CAREER<br>SUCCESS</h1>", unsafe_allow_html=True)

with col2:
    st.image("https://i.imgur.com/wSTFkRM.png", use_column_width=True)
    st.image(img, use_column_width=True)

st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <a class='button-custom' href='#'>Read the report</a>
        <a class='button-custom' href='#'>Learn about us</a>
    </div>
""", unsafe_allow_html=True)

# === ABOUT OUR TEAM SECTION ===
st.markdown('<a name="team"></a>', unsafe_allow_html=True)
st.subheader("Our Team ✨")

# === PAGE STATE ===
if "team_page" not in st.session_state:
    st.session_state.team_page = 1

def show_team(page):
    members = [
        ("Kiều Anh", "images/kieu_anh_1.png"),
        ("Kiều Anh", "images/kieu_anh_2.png"),
        ("Kiều Anh", "images/kieu_anh_3.png"),
        ("Kiều Anh", "images/kieu_anh_4.png"),
        ("Kiều Anh", "images/kieu_anh_5.png"),
        ("Kiều Anh", "images/kieu_anh_6.png"),
        ("Kiều Anh", "images/kieu_anh_7.png"),
    ]

    col1, col2, col3, col4 = st.columns(4)

    start = 0 if page == 1 else 4
    end = 4 if page == 1 else 7
    chunk = members[start:end]

    cols = [col1, col2, col3, col4] if page == 1 else [col1, col2, col3]

    for i, (name, img_path) in enumerate(chunk):
        with cols[i]:
            st.image(img_path, width=150)
            st.write(f"**{name}**")

    # Navigation buttons
    colL, colR = st.columns([1, 9])
    with colL:
        if st.button("⬅️", key="prev") and st.session_state.team_page == 2:
            st.session_state.team_page = 1
    with colR:
        if st.button("➡️", key="next") and st.session_state.team_page == 1:
            st.session_state.team_page = 2

show_team(st.session_state.team_page)
