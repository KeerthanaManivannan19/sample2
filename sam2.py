import streamlit as st

 

st.set_page_config(page_title="வயது கணிப்பான்", page_icon="🎂", layout="centered")

 

st.title("🎂 வயது கணிப்பான்")

st.write("நடப்பு ஆண்டு மற்றும் பிறந்த ஆண்டை உள்ளிட்டு உங்கள் வயதைக் கணக்கிடுங்கள்.")

 

current_year = st.number_input("நடப்பு ஆண்டை உள்ளிடுங்கள்", min_value=1, max_value=9999, value=2026, step=1)

birth_year = st.number_input("பிறந்த ஆண்டை உள்ளிடுங்கள்", min_value=1, max_value=9999, value=2000, step=1)

 

if st.button("வயதைக் கணக்கிடு"):

    if current_year > birth_year:

        age = current_year - birth_year

        st.success(f"உங்கள் வயது: {age} ஆண்டுகள்")

    else:

        st.error("பிழை: நடப்பு ஆண்டு பிறந்த ஆண்டை விட பெரியதாக இருக்க வேண்டும்.")

