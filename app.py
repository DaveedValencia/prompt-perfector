import streamlit as st
from openai import OpenAI
import os
import json

# Get API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

# Initialize OpenAI client with error handling
try:
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize OpenAI client: {str(e)}")
    st.stop()

# Set page config with enhanced metadata
st.set_page_config(
    page_title="Prompt Perfecter",
    page_icon="🎨",
    layout="centered",
    menu_items={
        'About': "# Prompt Perfecter\nEnhance your image prompts for better AI-generated art!\nCreated by David Valencia"
    }
)

# Initialize session state variables
if "request_count" not in st.session_state:
    st.session_state.request_count = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "prompt_input" not in st.session_state:
    st.session_state.prompt_input = ""
if "enhanced_prompt" not in st.session_state:
    st.session_state.enhanced_prompt = {}

# Check for a prompt in query parameters
if "prompt" in st.query_params and not st.session_state.submitted:
    st.session_state.prompt_input = st.query_params["prompt"]
    st.session_state.submitted = True

# Function to handle prompt submission
def submit_prompt():
    st.session_state.submitted = True

# Always allow requests (no cooldown)
def can_make_request():
    return True

# App title and description
st.title("Prompt Perfecter 🎨")
st.subheader("Turn simple ideas into detailed image prompts")

st.markdown("""
Enter a basic image idea below and watch it transform into a detailed, AI-ready prompt! ✨  
We'll automatically enhance your prompt with details on style, lighting, composition, and more.
""")

# Input field for prompt
user_prompt = st.text_area(
    "Describe your image idea:", 
    max_chars=300, 
    placeholder="e.g., a cowboy in a toy package set",
    height=100,
    on_change=submit_prompt,
    key="prompt_area"
)

# Function to call OpenAI API with proper error handling
def enhance_prompt(user_prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": """Parse the user's image prompt and intelligently fill any missing fields to create an enhanced prompt. Return ONLY valid JSON with the following structure:

{
  "subject": "Main subject or character",
  "action": "What the subject is doing",
  "style_or_medium": "Artistic style or rendering medium",
  "lighting_or_mood": "Lighting conditions or emotional tone",
  "camera_angle_or_composition": "Perspective or arrangement",
  "background_or_environment": "Setting or surroundings",
  "specific_details_or_accessories": "Notable items or features",
  "color_scheme_or_palette": "Color theme",
  "final_prompt": "Complete prompt combining all elements"
}

Parse any elements explicitly mentioned in the user's text. If a field is missing information, suggest a contextually appropriate value based on keywords or inferred theme. Build the final_prompt by combining all 8 fields into a natural language sentence, even if some values were auto-suggested. If an element cannot be reasonably inferred, leave it as an empty string.

The final_prompt should read as a cohesive description that could be submitted to an image generation AI."""},
                {"role": "user", "content": f"Create an enhanced image prompt for: {user_prompt}"}
            ],
            response_format={"type": "json_object"},
            max_tokens=800,
            temperature=0.7
        )
        
        # Extract the response and parse JSON
        response_text = response.choices[0].message.content
        return json.loads(response_text)
    
    except json.JSONDecodeError:
        return {"error": "Failed to parse the response as JSON. Please try again."}
    except Exception as e:
        error_msg = str(e)
        if "api_key" in error_msg.lower():
            return {"error": "Invalid or missing API key. Please check your OpenAI API key configuration."}
        elif "rate limit" in error_msg.lower():
            return {"error": "Rate limit exceeded. Please try again in a few moments."}
        else:
            return {"error": f"Could not generate response: {error_msg}"}

# Generate response
if st.button("Enhance my prompt ✨") or st.session_state.submitted:
    # Reset the submitted state for next use
    st.session_state.submitted = False
    
    if user_prompt:
        if can_make_request():
            with st.spinner("Enhancing your prompt with magical details..."):
                # Track request count
                st.session_state.request_count += 1
                
                # Call the OpenAI API
                enhanced_prompt_data = enhance_prompt(user_prompt)
                
                # Store result in session state
                st.session_state.enhanced_prompt = enhanced_prompt_data
    else:
        st.warning("Please enter an image idea first! ✨")

# Display results if available
if st.session_state.enhanced_prompt:
    if "error" in st.session_state.enhanced_prompt:
        st.error(st.session_state.enhanced_prompt["error"])
    else:
        # Create tabs for different views
        tab1, tab2 = st.tabs(["Enhanced Prompt", "Detailed Breakdown"])
        
        with tab1:
            st.success("### Your Enhanced Prompt:")
            st.markdown(f"**{st.session_state.enhanced_prompt['final_prompt']}**")
            
            # Copy button for final prompt
            st.code(st.session_state.enhanced_prompt['final_prompt'], language="text")
            
        with tab2:
            # Display each component with custom styling
            components = [
                ("Subject", "subject", "👤"),
                ("Action", "action", "🏃"),
                ("Style/Medium", "style_or_medium", "🖌️"),
                ("Lighting/Mood", "lighting_or_mood", "💡"),
                ("Camera/Composition", "camera_angle_or_composition", "📷"),
                ("Background/Environment", "background_or_environment", "🌄"),
                ("Details/Accessories", "specific_details_or_accessories", "✨"),
                ("Colors", "color_scheme_or_palette", "🎨")
            ]
            
            st.markdown("### Prompt Components")
            
            # Create custom layout with columns
            for i in range(0, len(components), 2):
                col1, col2 = st.columns(2)
                
                # First component in this row
                title, key, emoji = components[i]
                with col1:
                    st.markdown(f"**{emoji} {title}**")
                    component_value = st.session_state.enhanced_prompt.get(key, "")
                    if component_value:
                        st.info(component_value)
                    else:
                        st.text("Not specified")
                
                # Second component (if exists)
                if i+1 < len(components):
                    title, key, emoji = components[i+1]
                    with col2:
                        st.markdown(f"**{emoji} {title}**")
                        component_value = st.session_state.enhanced_prompt.get(key, "")
                        if component_value:
                            st.info(component_value)
                        else:
                            st.text("Not specified")
        
        # Add button to generate again
        if st.button("Try another prompt", key="try_again"):
            # Clear the input field and result
            st.session_state.prompt_input = ""
            st.session_state.enhanced_prompt = {}
            st.rerun()

# Sidebar with tips
st.sidebar.markdown("### Prompt Crafting Tips")
st.sidebar.markdown("""
* **Be specific** about your subject - "a cat" vs "a Persian cat with blue eyes"
* **Mention style** - photography, oil painting, 3D render, pencil sketch
* **Add lighting** - golden hour, dark and moody, bright studio light
* **Set the scene** - underwater, in a forest, cyberpunk city
* **Composition matters** - close-up, bird's eye view, rule of thirds
* **Color themes** - monochromatic, pastel, vibrant neons
* **Details make it special** - reflections, fog, glitter, textures
""")

# Examples collapsible section
with st.expander("✨ Need inspiration? Try these examples"):
    example_prompts = [
        "A fox reading a book in the forest",
        "Cyberpunk samurai on a motorcycle",
        "A floating island with a castle and waterfalls",
        "Astronaut in an underwater temple",
        "Steampunk train station at sunset"
    ]
    
    for example in example_prompts:
        if st.button(example):
            st.session_state.prompt_input = example
            st.session_state.submitted = True
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
**Created by David Valencia**

**Learn how to vibe code -->** [YouTube](https://youtube.com/@DaveedValencia)

**Socials:** [X](https://x.com/DaveedValencia) | [IG](https://instagram.com/DaveedValencia) 🚀
""")
