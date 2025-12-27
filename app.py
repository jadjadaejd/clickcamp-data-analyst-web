import streamlit as st

st.set_page_config(page_title="A Little Gift", layout="centered")

st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(180deg, #ffe3e8 0%, #ffffff 100%);
}

/* FORCE title color */
.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3 {
    color: #6b3f3f !important;
    font-weight: 700;
}

/* FORCE paragraph color */
.stMarkdown p {
    color: #7a5a5a !important;
}

/* Buttons */
.stButton > button {
    background-color: #ffffff;
    color: #ff6f91;
    border: none;
    border-radius: 14px;
    padding: 0.6em 1.4em;
    font-weight: 600;
    box-shadow: 0 8px 20px rgba(255, 159, 169, 0.35);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #fff0f4;
    transform: translateY(-2px);
}

/* Text input */
.stTextInput input {
    background-color: #ffffff !important;
    color: #5a3a3a !important;
    border: 1.5px solid #ffb6c1 !important;
    border-radius: 14px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

</style>
""", unsafe_allow_html=True)




# ---------- init state ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "error" not in st.session_state:
    st.session_state.error = False


# ---------- PAGE 1 : Gift ----------
if st.session_state.page == 1:

    st.markdown("""
    <div style="text-align:center; margin-top:120px;">
        <h1>🎁 A Gift for You</h1>
        <p style="opacity:0.8;">
            Someone sent you a little gift.<br>
            Would you like to open it?
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open the box ✨"):
        st.session_state.page = 2
        st.rerun()


# ---------- PAGE 2 : Password ----------
elif st.session_state.page == 2:

    st.markdown("""
    <div style="text-align:center; margin-top:120px;">
        <h2>🔐 One Last Step</h2>
        <p style="opacity:0.7;">
            Hint: It's a birthday 🎂
        </p>
    </div>
    """, unsafe_allow_html=True)

    password = st.text_input("Enter the password", type="password")

    if st.button("Unlock 🎀"):
        if password == "230149":
            st.session_state.page = 3
            st.session_state.error = False
            st.rerun()
        else:
            st.session_state.error = True

    if st.session_state.error:
        st.error("Wrong password. Try again gently.")


    if st.button("← Back"):
        st.session_state.page = 1
        st.rerun()


# ---------- PAGE 3 : Final ----------
elif st.session_state.page == 3:

    if st.button("← Back"):
        st.session_state.page = 1
        st.rerun()

    left, center, right = st.columns([1,2,1])

    with center:
        st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)

        st.image("image1.png", width=300)
        st.markdown("### Did you smile today? 😊")
        st.markdown("Take a breath. You're doing better than you think.")

        st.markdown('</div>', unsafe_allow_html=True)
