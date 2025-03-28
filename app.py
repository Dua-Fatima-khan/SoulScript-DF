import streamlit as st
import random

st.set_page_config(
    page_title="SoulScript",
    page_icon="\U0001F33F",
    layout="centered",
)

def generate_story(name, dream, challenge, inspiration, action, emotion, place):
    actions = [
        "pushed forward despite all odds \U0001F4AA",
        "turned pain into power \U0001F525",
        "refused to give up \U0001F3C6",
        "kept believing when no one else did ✨",
        "fought with an unshakable spirit ⚡"
    ]
    random_action = random.choice(actions)
    
    story = f"""
    <div style='background-color:#f9f9f9;padding:20px;border-radius:10px;'>
        <h2 style='color:#2E8B57;text-align:center;'>✨ YOUR EPIC MOTIVATIONAL STORY ✨</h2>
        <p style='font-size:18px;color:#333;'>
            <b>{name}</b> had a dream—to <b>{dream}</b> 🌠. But along the way, <b>{challenge}</b> stood like a mountain in their path.<br><br>
            Many would have given up, but <b>{name}</b> remembered the words of <b>{inspiration}</b> and chose to {random_action}!<br><br>
            With unwavering determination, <b>{name}</b> took the first step: <b>{action}</b> 🚀. Each step forward turned doubt into confidence, fear into courage.<br><br>
            And then, the day arrived! Standing tall in <b>{place}</b>, <b>{name}</b> felt <b>{emotion}</b>—not because it was easy, but because they never quit.<br><br>
            This is your journey. This is your story. Keep going! 🔥🏆
        </p>
    </div>
    """
    return story

# Streamlit UI
st.markdown("""
    <h1 style='text-align:center;color:#2E8B57;'>🌿 SoulScript</h1>
    <h2 style='text-align:center;color:#777;'>Motivational Story Generator</h2>
    <p style='text-align:center;font-size:18px;color:#777;'>Transform your dreams into reality with a unique story! 🌈</p>
    <p style='text-align:center;font-size:18px;color:#777;'>Fill in the blanks and get your personalized motivational story! 🚀</p>
    <hr>
""", unsafe_allow_html=True)

name = st.text_input("👋 What is your name?")
dream = st.text_input("💭 What is your biggest dream?")
challenge = st.text_input("⚔️ Name a challenge you've faced")
inspiration = st.text_input("🌟 Who or what inspires you?")
action = st.text_input("🚀 What action will you take today?")
emotion = st.text_input("😊 How do you want to feel in the future?")
place = st.text_input("📍 Name a place where you'd love to succeed")

if st.button("✨ Generate My Story ✨"):
    if name and dream and challenge and inspiration and action and emotion and place:
        story = generate_story(name, dream, challenge, inspiration, action, emotion, place)
        st.markdown(story, unsafe_allow_html=True)
    else:
        st.warning("Please fill in all fields to generate your story.")

st.markdown("""
    <hr>
    <h3 style='text-align:center;color:#2E8B57;'>Remember, greatness is within you! 💪🚀</h3>
    <p style='text-align:center;'>Follow us on <a href='https://www.linkedin.com/in/dua-fatima-906208258/' target='_blank'>LinkedIn</a> for more inspiration!</p>
    <p style='text-align:center;'>Share your story with us using <b>#SoulScript</b> on my LinkedIn page.</p>
    <hr>
    <div style='text-align:center;font-size:12px;color:#555;'>
        <small>Built with ❤️ by Dua Fatima</small><br>
        <small>Copyright © 2025 - All Rights Reserved</small>
    </div>
""", unsafe_allow_html=True)
