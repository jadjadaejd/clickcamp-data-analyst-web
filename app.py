import streamlit as st

st.set_page_config(page_title="Smile Today", layout="centered")

# init state
if "page" not in st.session_state:
    st.session_state.page = "cover"


# ---------- หน้า 1 : หน้าจดหมาย ----------
if st.session_state.page == "cover":

    st.markdown("""
    <div style="text-align:center; margin-top:120px;">
        <h1>💌 A Little Letter for You</h1>
        <p style="opacity:0.8;">
            Before you go on,<br>
            take a moment to open this gently.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open the letter ✨"):
        st.session_state.page = "main"
        st.rerun()


# ---------- หน้า 2 : หน้าหลัก ----------
elif st.session_state.page == "main":

    # ปุ่ม back (อยู่บนสุด)
    if st.button("← Back"):
        st.session_state.page = "cover"
        st.rerun()

    left, center, right = st.columns([1,2,1])

    with center:
        st.image("image1.png", width=300)
        st.markdown("### Did you smile today? 😊")
        st.markdown("Take a breath. You're doing better than you think.")
