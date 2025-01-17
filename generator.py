from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Choose an open-source model from Hugging Face
MODEL_NAME = "EleutherAI/gpt-neo-2.7B"  # Open-source GPT model

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Set pad token to avoid warnings
tokenizer.pad_token = tokenizer.eos_token  

def generate_personalized_roadmap(user_input: str) -> str:
    """
    Generates a personalized learning roadmap based on user input.
    
    Args:
        user_input (str): User's topic, knowledge level, and learning preferences.
    
    Returns:
        str: AI-generated structured learning roadmap.
    """
    # Define the prompt template
    prompt = f"""
    You are an expert AI assistant that creates structured 3-month learning roadmaps. 
    The user provided the following information:
    
    {user_input}
    
    Generate a detailed roadmap broken down by **Weeks** with **tasks, recommended resources, and tips**.
    Format it clearly using markdown for easy readability.
    """

    # Tokenize input with attention mask
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

    # Generate output using sampling-based generation
    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_length=2040,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,  # Enables sampling for diverse outputs
        top_p=0.95,
        temperature=0.7,
    )

    # Decode and return the generated text
    roadmap = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return roadmap
