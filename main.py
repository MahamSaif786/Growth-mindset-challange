import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🧠",
    layout="wide"
)

# Custom Styling
st.markdown(
    """
    <style>
        .main-container {
            max-width: 800px;
            margin: auto;
        }
        .highlight {
            font-size: 18px;
            font-weight: bold;
            color: #2E8B57;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.title("🌱 Growth Mindset Challenge")
st.write("### Unlock your potential through self-improvement and perseverance.")

# Daily Inspiration
st.subheader("💡 Daily Inspiration")
st.info("*“The mind is just like a muscle—the more you exercise it, the stronger it gets and the more it can expand.”* — Idowu Koyenikan")

# Goal Input
st.subheader("🎯 Set Your Growth Goal")
user_goal = st.text_input("What personal or professional goal are you focusing on today?")
if user_goal:
    st.success(f"Great choice! Stay committed to '{user_goal}' and take small steps towards achieving it.")

# Challenge Reflection
st.subheader("📝 Reflect on Your Challenges")
st.write("Understanding challenges is the first step toward overcoming them.")
challenge_input = st.text_area("Describe a challenge you're currently facing:")
if challenge_input:
    st.success("Acknowledging challenges leads to solutions. Keep pushing forward!")

# Personal Achievement
st.subheader("🏆 Celebrate Your Wins")
achievement_input = st.text_input("Share a recent achievement or progress milestone:")
if achievement_input:
    st.success(f"Well done! Recognizing achievements helps build confidence. Keep it up!")

# Closing Note
st.markdown("---")
st.markdown(
    "<div class='highlight'>🚀 Keep learning, keep growing. Success is a journey, not a destination!</div>",
    unsafe_allow_html=True
)
st.write("### Developed by Maham Saif")
