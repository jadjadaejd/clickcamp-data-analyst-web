import streamlit as st

st.set_page_config(page_title="A Little Gift", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #ffe3e8 0%, #ffffff 100%);
}

.stButton > button {
    border-radius: 14px;
    padding: 0.6em 1.4em;
    font-weight: 600;
}

.stTextInput input {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "error" not in st.session_state:
    st.session_state.error = False

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("🎁 A Gift for You")
    st.write("Someone sent you a little gift.")

    if st.button("Open the box ✨"):
        st.session_state.page = 2

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.title("🔐 One Last Step")
    st.caption("Hint: It's a birthday 🎂")

    password = st.text_input(
        "Enter the password",
        type="password",
        placeholder="DDMMYY"
    )

    if st.button("Unlock 🎀"):
        if password == "230149":
            st.session_state.page = 3
            st.session_state.error = False
        else:
            st.session_state.error = True

    if st.session_state.error:
        st.error("Wrong password.")

    if st.button("← Back"):
        st.session_state.page = 1

# ---------- PAGE 3 ----------
elif st.session_state.page == 3:
    st.success("🎉 You unlocked it!")
    st.write("Did you smile today? 😊")

    if st.button("← Back to start"):
        st.session_state.page = 1
