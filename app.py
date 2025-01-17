import streamlit as st
import json
from generator import generate_personalized_roadmap

# Load topics from JSON file
with open("data/topics.json", "r") as file:
    topics = json.load(file)["topics"]

st.set_page_config(page_title="🚀 AI Roadmap Builder", layout="wide")

st.title("📌 AI Roadmap Builder")
st.subheader("Tell us about your current knowledge to generate a personalized roadmap!")

# --- User Input Form ---
selected_topic = st.selectbox("Choose a topic:", topics)

knowledge_level = st.radio(
    "How would you rate your knowledge in this topic?",
    ["Beginner", "Intermediate", "Advanced"]
)

familiar_concepts = st.text_area(
    "What do you already know about this topic?",
    "E.g., tokenization, embeddings, fine-tuning, transformers..."
)

learning_preferences = st.multiselect(
    "How do you prefer to learn?",
    ["Theory (Articles, Books)", "Hands-on Coding", "Videos & Tutorials", "Project-Based Learning"]
)

if st.button("Generate Roadmap 🚀"):
    user_input = f"Topic: {selected_topic}, Level: {knowledge_level}, Familiar concepts: {familiar_concepts}, Learning preferences: {', '.join(learning_preferences)}"
    
    with st.spinner("Generating your personalized roadmap..."):
        roadmap = generate_personalized_roadmap(user_input)  # Call the AI model
        st.success("Here’s your roadmap! 🎯")
        st.write(roadmap)  # Display roadmap
