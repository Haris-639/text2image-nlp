# # import streamlit as st
# # from PIL import Image
# # import base64
# # import io
# # import time
# # import random
# # import asyncio
# # import sys
# # import os
# # from io import BytesIO

# # # Set page configuration
# # st.set_page_config(
# #     page_title="Artisan AI",
# #     page_icon="✨",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Custom CSS for styling with dark theme
# # def apply_custom_css():
# #     st.markdown("""
# #     <style>
# #         /* Main theme colors and fonts */
# #         :root {
# #             --primary: #BB86FC;
# #             --primary-variant: #9D4EDD;
# #             --secondary: #E0AAFF;
# #             --background: #0F0A1E;
# #             --surface: #1A1625;
# #             --surface-variant: #231C34;
# #             --on-primary: #FFFFFF;
# #             --on-background: #E0E0E0;
# #             --on-surface: #E0E0E0;
# #             --border: #2D2640;
# #             --card-shadow: rgba(0, 0, 0, 0.5);
# #         }
        
# #         /* Base styling */
# #         .stApp {
# #             background-color: var(--background);
# #             font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, sans-serif;
# #             color: var(--on-background);
# #         }
        
# #         /* Remove default Streamlit padding */
# #         .main .block-container {
# #             padding-top: 1rem;
# #             padding-bottom: 1rem;
# #             max-width: 100%;
# #             padding-left: 1rem;
# #             padding-right: 1rem;
# #         }
        
# #         /* Header styling */
# #         .header-container {
# #             display: flex;
# #             align-items: center;
# #             justify-content: space-between;
# #             padding: 1rem 2rem;
# #             background-color: rgba(15, 10, 30, 0.8);
# #             backdrop-filter: blur(10px);
# #             border-bottom: 1px solid var(--border);
# #             position: sticky;
# #             top: 0;
# #             z-index: 999;
# #         }
        
# #         .logo-container {
# #             display: flex;
# #             align-items: center;
# #         }
        
# #         .logo-icon {
# #             display: flex;
# #             align-items: center;
# #             justify-content: center;
# #             width: 40px;
# #             height: 40px;
# #             background: linear-gradient(135deg, #9D4EDD 0%, #C77DFF 100%);
# #             border-radius: 50%;
# #             margin-right: 0.75rem;
# #         }
        
# #         .logo-text {
# #             font-size: 1.5rem;
# #             font-weight: 700;
# #             color: var(--primary);
# #         }
        
# #         .nav-links {
# #             display: flex;
# #             align-items: center;
# #             gap: 2rem;
# #         }
        
# #         .nav-link {
# #             color: var(--on-background);
# #             text-decoration: none;
# #             font-weight: 500;
# #             transition: color 0.2s ease;
# #         }
        
# #         .nav-link:hover {
# #             color: var(--primary);
# #         }
        
# #         .sign-in-button {
# #             background: transparent;
# #             color: var(--primary);
# #             border: 1px solid var(--primary);
# #             border-radius: 6px;
# #             padding: 0.5rem 1rem;
# #             font-weight: 600;
# #             cursor: pointer;
# #             transition: all 0.2s ease;
# #         }
        
# #         .sign-in-button:hover {
# #             background-color: rgba(187, 134, 252, 0.1);
# #         }
        
# #         /* Hero section */
# #         .hero-container {
# #             text-align: center;
# #             padding: 3rem 1rem;
# #         }
        
# #         .hero-title {
# #             font-size: 2.5rem;
# #             font-weight: 700;
# #             color: var(--primary);
# #             margin-bottom: 1rem;
# #             line-height: 1.2;
# #         }
        
# #         .hero-subtitle {
# #             font-size: 1.1rem;
# #             color: rgba(224, 224, 224, 0.8);
# #             max-width: 700px;
# #             margin: 0 auto 2rem;
# #             line-height: 1.5;
# #         }
        
# #         /* Tab styling */
# #         .tab-container {
# #             display: flex;
# #             max-width: 500px;
# #             margin: 0 auto 2rem;
# #             background-color: var(--surface-variant);
# #             border-radius: 50px;
# #             padding: 0.25rem;
# #         }
        
# #         .tab {
# #             flex: 1;
# #             text-align: center;
# #             padding: 0.75rem 1rem;
# #             cursor: pointer;
# #             border-radius: 50px;
# #             font-weight: 600;
# #             transition: all 0.2s ease;
# #             display: flex;
# #             align-items: center;
# #             justify-content: center;
# #             gap: 0.5rem;
# #         }
        
# #         .tab.active {
# #             background-color: var(--primary);
# #             color: black;
# #         }
        
# #         .tab:not(.active) {
# #             color: var(--on-background);
# #         }
        
# #         .tab:not(.active):hover {
# #             background-color: rgba(187, 134, 252, 0.1);
# #         }
        
# #         /* Main content container */
# #         .content-container {
# #             background-color: var(--surface);
# #             border-radius: 12px;
# #             border: 1px solid var(--border);
# #             max-width: 1200px;
# #             margin: 0 auto;
# #             padding: 2rem;
# #         }
        
# #         /* Two column layout */
# #         .two-column-layout {
# #             display: flex;
# #             gap: 2rem;
# #         }
        
# #         .left-column {
# #             flex: 3;
# #         }
        
# #         .right-column {
# #             flex: 2;
# #         }
        
# #         /* Section styling */
# #         .section-title {
# #             font-size: 1.25rem;
# #             font-weight: 600;
# #             color: var(--on-background);
# #             margin-bottom: 1rem;
# #         }
        
# #         /* Input styling */
# #         .stTextArea > div > div > textarea {
# #             background-color: var(--surface-variant);
# #             border: 1px solid var(--border);
# #             border-radius: 8px;
# #             color: var(--on-background);
# #             font-size: 1rem;
# #             padding: 1rem;
# #             min-height: 120px;
# #         }
        
# #         .stTextArea > div > div > textarea:focus {
# #             border-color: var(--primary);
# #             box-shadow: 0 0 0 1px var(--primary);
# #         }
        
# #         .stTextInput > div > div > input {
# #             background-color: var(--surface-variant);
# #             border: 1px solid var(--border);
# #             border-radius: 8px;
# #             color: var(--on-background);
# #             font-size: 1rem;
# #             padding: 0.75rem 1rem;
# #         }
        
# #         .stTextInput > div > div > input:focus {
# #             border-color: var(--primary);
# #             box-shadow: 0 0 0 1px var(--primary);
# #         }
        
# #         /* Selectbox styling */
# #         .stSelectbox > div > div {
# #             background-color: var(--surface-variant);
# #             border: 1px solid var(--border);
# #             border-radius: 8px;
# #         }
        
# #         .stSelectbox > div > div > div {
# #             color: var(--on-background);
# #         }
        
# #         /* Slider styling */
# #         .stSlider > div > div > div > div > div {
# #             background-color: var(--primary);
# #         }
        
# #         .stSlider > div > div > div > div > div > div {
# #             background-color: var(--primary);
# #             border-color: var(--primary);
# #         }
        
# #         /* Button styling */
# #         .generate-button {
# #             background: linear-gradient(90deg, #9D4EDD 0%, #C77DFF 100%);
# #             color: white;
# #             border: none;
# #             border-radius: 8px;
# #             padding: 0.75rem 1.5rem;
# #             font-weight: 600;
# #             width: 100%;
# #             cursor: pointer;
# #             transition: all 0.2s ease;
# #             display: flex;
# #             align-items: center;
# #             justify-content: center;
# #             gap: 0.5rem;
# #             font-size: 1rem;
# #             margin-top: 1.5rem;
# #         }
        
# #         .generate-button:hover {
# #             opacity: 0.9;
# #             transform: translateY(-2px);
# #             box-shadow: 0 4px 12px rgba(157, 78, 221, 0.3);
# #         }
        
# #         /* Preview area */
# #         .preview-container {
# #             background-color: var(--surface-variant);
# #             border: 1px dashed rgba(224, 224, 224, 0.3);
# #             border-radius: 8px;
# #             height: 100%;
# #             min-height: 400px;
# #             display: flex;
# #             flex-direction: column;
# #             align-items: center;
# #             justify-content: center;
# #             text-align: center;
# #             padding: 1.5rem;
# #         }
        
# #         .preview-placeholder {
# #             color: rgba(224, 224, 224, 0.5);
# #             font-size: 1.1rem;
# #             margin-top: 1rem;
# #         }
        
# #         /* Expander styling */
# #         .stExpander > div > div > div > div > div > div {
# #             background-color: transparent;
# #             color: var(--on-background);
# #             border: none;
# #         }
        
# #         .stExpander > div > div > div > div > div > div > div > p {
# #             font-size: 1rem;
# #             font-weight: 500;
# #             color: var(--on-background);
# #         }
        
# #         .stExpander > div > div > div > div > div > div > div > svg {
# #             color: var(--on-background);
# #         }
        
# #         /* Remove Streamlit branding */
# #         #MainMenu {visibility: hidden;}
# #         footer {visibility: hidden;}
        
# #         /* Custom label styling */
# #         .custom-label {
# #             font-size: 0.9rem;
# #             color: rgba(224, 224, 224, 0.7);
# #             margin-bottom: 0.5rem;
# #             display: block;
# #         }
        
# #         /* Progress bar styling */
# #         .stProgress > div > div > div {
# #             background: linear-gradient(90deg, #9D4EDD 0%, #C77DFF 100%);
# #         }
        
# #         /* Hide default Streamlit elements */
# #         .stDeployButton {
# #             display: none !important;
# #         }
        
# #         /* Sidebar styling */
# #         [data-testid="stSidebar"] {
# #             background-color: var(--surface);
# #             border-right: 1px solid var(--border);
# #         }
        
# #         [data-testid="stSidebar"] > div:first-child {
# #             padding: 2rem 1rem;
# #         }
        
# #         .sidebar-header {
# #             display: flex;
# #             flex-direction: column;
# #             align-items: center;
# #             margin-bottom: 2rem;
# #             text-align: center;
# #         }
        
# #         .sidebar-logo {
# #             width: 70px;
# #             height: 70px;
# #             background: linear-gradient(135deg, #9D4EDD 0%, #C77DFF 100%);
# #             border-radius: 50%;
# #             display: flex;
# #             align-items: center;
# #             justify-content: center;
# #             margin-bottom: 1rem;
# #             box-shadow: 0 0 20px rgba(157, 78, 221, 0.3);
# #         }
        
# #         .sidebar-title {
# #             font-size: 1.5rem;
# #             font-weight: 700;
# #             color: var(--primary);
# #             margin-bottom: 0.5rem;
# #         }
        
# #         .sidebar-description {
# #             color: rgba(224, 224, 224, 0.7);
# #             font-size: 0.9rem;
# #             margin-bottom: 1.5rem;
# #         }
        
# #         .sidebar-divider {
# #             height: 1px;
# #             background: linear-gradient(90deg, transparent, rgba(187, 134, 252, 0.3), transparent);
# #             margin: 1.5rem 0;
# #         }
        
# #         .sidebar-section-title {
# #             font-size: 1.1rem;
# #             font-weight: 600;
# #             color: var(--primary);
# #             margin-bottom: 1rem;
# #         }
        
# #         /* Sample prompt buttons */
# #         .sample-prompt-button {
# #             background-color: rgba(187, 134, 252, 0.15);
# #             color: var(--on-background);
# #             border: none;
# #             border-radius: 8px;
# #             padding: 0.75rem 1rem;
# #             font-weight: 500;
# #             width: 100%;
# #             text-align: center;
# #             margin-bottom: 0.75rem;
# #             cursor: pointer;
# #             transition: all 0.2s ease;
# #         }
        
# #         .sample-prompt-button:hover {
# #             background-color: rgba(187, 134, 252, 0.25);
# #             transform: translateY(-2px);
# #         }
        
# #         /* Checkbox styling */
# #         .stCheckbox > div > div > div > div {
# #             border-color: var(--primary) !important;
# #         }
        
# #         .stCheckbox > div > div > div > div > div {
# #             background-color: var(--primary) !important;
# #         }
        
# #         /* Responsive adjustments */
# #         @media (max-width: 992px) {
# #             .two-column-layout {
# #                 flex-direction: column;
# #             }
            
# #             .hero-title {
# #                 font-size: 2rem;
# #             }
# #         }
# #     </style>
# #     """, unsafe_allow_html=True)

# # # Function to create a placeholder image
# # def create_placeholder_image(width=512, height=512, color=(100, 70, 150)):
# #     img = Image.new('RGB', (width, height), color=color)
# #     return img

# # # Function to generate image
# # def generate_image(prompt, style, context_mood, num_images=1):
# #     """
# #     Generate an image based on the prompt and settings
# #     """
# #     # Show progress indicators
# #     progress_bar = st.progress(0)
# #     status_text = st.empty()
    
# #     try:
# #         # Simulate progress while generating
# #         for i in range(101):
# #             progress_bar.progress(i)
# #             status_text.text(f"Generating your masterpiece: {i}%")
# #             time.sleep(0.02)
        
# #         # Create a random color based on the prompt
# #         r = (hash(prompt) % 150) + 50
# #         g = (hash(style) % 100) + 50
# #         b = (hash(prompt + style) % 200) + 50
        
# #         # Create the image
# #         img = create_placeholder_image(512, 512, (r, g, b))
    
# #     except Exception as e:
# #         st.error(f"Error generating image: {str(e)}")
# #         img = create_placeholder_image(512, 512, (100, 70, 150))
    
# #     # Clear the progress indicators
# #     progress_bar.empty()
# #     status_text.empty()
    
# #     return img

# # # Function to convert PIL Image to base64 for display
# # def get_image_base64(img):
# #     buffered = io.BytesIO()
# #     img.save(buffered, format="PNG")
# #     img_str = base64.b64encode(buffered.getvalue()).decode()
# #     return img_str

# # # Main application
# # def main():
# #     # Apply custom CSS
# #     apply_custom_css()
    
# #     # Sidebar
# #     with st.sidebar:
# #         st.markdown("""
# #         <div class="sidebar-header">
# #             <div class="sidebar-logo">
# #                 <span style="font-size: 30px;">🎨</span>
# #             </div>
# #             <h1 class="sidebar-title">Artisan AI</h1>
# #             <p class="sidebar-description">Transform your ideas into stunning visuals with our AI-powered image generator.</p>
# #         </div>
# #         """, unsafe_allow_html=True)
        
# #         st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
# #         # About section
# #         with st.expander("ℹ️ About", expanded=False):
# #             st.markdown("""
# #             <div style="background-color: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; border-left: 3px solid #BB86FC;">
# #             <strong style="color: #FF4081;">Artisan AI</strong> uses state-of-the-art machine learning models to generate images from text descriptions.
            
# #             <ul style="color: rgba(224, 224, 224, 0.8);">
# #                 <li>📝 Enter detailed prompts</li>
# #                 <li>🎯 Provide context for better results</li>
# #                 <li>🖼️ Generate multiple images at once</li>
# #                 <li>✨ Experiment with different styles</li>
# #             </ul>
# #             </div>
# #             """, unsafe_allow_html=True)
        
# #         # Tips & Tricks section
# #         with st.expander("🔧 Tips & Tricks", expanded=False):
# #             st.markdown("""
# #             <div style="background-color: rgba(0, 0, 0, 0.2); padding: 15px; border-radius: 8px; border-left: 3px solid #FF4081;">
# #             <strong style="color: #BB86FC;">For best results:</strong>
            
# #             <ol style="color: rgba(224, 224, 224, 0.8);">
# #                 <li>Be specific in your descriptions</li>
# #                 <li>Include details about style, mood, lighting</li>
# #                 <li>Use context to guide the aesthetic direction</li>
# #                 <li>Try different variations of the same prompt</li>
# #                 <li>Experiment with different quality settings</li>
# #             </ol>
# #             </div>
# #             """, unsafe_allow_html=True)
        
# #         st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
# #         # Connection settings
# #         with st.expander("⚙️ Connection Settings", expanded=False):
# #             use_backend = st.checkbox("Use Backend Service", value=True)
# #             backend_url = st.text_input("Backend URL", value="localhost:50051")
# #             st.caption("Change only if you know what you're doing")
        
# #         # Sample prompts
# #         st.markdown('<h3 class="sidebar-section-title">Sample Prompts</h3>', unsafe_allow_html=True)
        
# #         sample_prompts = [
# #             "A serene lake at sunset with mountains in the background",
# #             "Cyberpunk cityscape with neon lights and flying cars",
# #             "Enchanted forest with glowing mushrooms and fairy lights",
# #             "Abstract portrait made of geometric shapes and vibrant colors"
# #         ]
        
# #         # Create session state for prompt if it doesn't exist
# #         if 'prompt' not in st.session_state:
# #             st.session_state.prompt = ""
        
# #         # Function to update prompt
# #         def set_prompt(text):
# #             st.session_state.prompt = text
        
# #         # Display sample prompt buttons
# #         for i, prompt in enumerate(sample_prompts):
# #             st.markdown(
# #                 f"""<button class="sample-prompt-button" onclick="
# #                     document.querySelector('textarea').value = '{prompt}';
# #                     const event = new Event('input', {{ bubbles: true }});
# #                     document.querySelector('textarea').dispatchEvent(event);
# #                 ">Try Prompt {i+1}</button>""",
# #                 unsafe_allow_html=True
# #             )
        
# #         st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
# #         st.markdown("""
# #         <div style="text-align: center; color: rgba(224, 224, 224, 0.5); font-size: 0.8rem;">
# #             © 2023 Artisan AI | <a href="#" style="color: #BB86FC;">Documentation</a>
# #         </div>
# #         """, unsafe_allow_html=True)
    
# #     # Custom header
# #     st.markdown("""
# #     <div class="header-container">
# #         <div class="logo-container">
# #             <div class="logo-icon">
# #                 <span style="font-size: 20px;">✨</span>
# #             </div>
# #             <div class="logo-text">Artisan AI</div>
# #         </div>
# #         <div class="nav-links">
# #             <a href="#" class="nav-link">Gallery</a>
# #             <a href="#" class="nav-link">Styles</a>
# #             <a href="#" class="nav-link">Help</a>
# #             <button class="sign-in-button">Sign In</button>
# #         </div>
# #     </div>
# #     """, unsafe_allow_html=True)
    
# #     # Hero section
# #     st.markdown("""
# #     <div class="hero-container">
# #         <h1 class="hero-title">Transform Your Words Into Visual Masterpieces</h1>
# #         <p class="hero-subtitle">Enter your prompt below and watch as our AI brings your imagination to life with stunning visuals.</p>
# #     </div>
# #     """, unsafe_allow_html=True)
    
# #     # Tabs
# #     col1, col2, col3 = st.columns([1, 2, 1])
# #     with col2:
# #         st.markdown("""
# #         <div class="tab-container">
# #             <div class="tab active">
# #                 <span style="font-size: 16px;">📝</span> Create
# #             </div>
# #             <div class="tab">
# #                 <span style="font-size: 16px;">🖼️</span> Gallery
# #             </div>
# #         </div>
# #         """, unsafe_allow_html=True)
    
# #     # Main content container
# #     st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
# #     # Two column layout
# #     st.markdown('<div class="two-column-layout">', unsafe_allow_html=True)
    
# #     # Left column
# #     st.markdown('<div class="left-column">', unsafe_allow_html=True)
    
# #     # Prompt section
# #     st.markdown('<h3 class="section-title">Your Prompt</h3>', unsafe_allow_html=True)
# #     prompt = st.text_area("", 
# #                          value=st.session_state.get('prompt', ''),
# #                          placeholder="Describe what you want to see in detail... (e.g., A serene lake at sunset with mountains in the background and a small cabin by the shore)",
# #                          label_visibility="collapsed",
# #                          key="prompt_input")
    
# #     # Update session state
# #     st.session_state.prompt = prompt
    
# #     # Style and Context/Mood in two columns
# #     col1, col2 = st.columns(2)
    
# #     with col1:
# #         st.markdown('<label class="custom-label">Art Style</label>', unsafe_allow_html=True)
# #         style = st.selectbox("", 
# #                            ["Select style", "Digital Art", "Oil Painting", "Watercolor", "Sketch", 
# #                             "Pixel Art", "3D Render", "Anime", "Comic Book", "Fantasy", "Realistic"],
# #                            label_visibility="collapsed")
    
# #     with col2:
# #         st.markdown('<label class="custom-label">Context/Mood</label>', unsafe_allow_html=True)
# #         context_mood = st.text_input("", 
# #                                    placeholder="e.g., dreamy, cyberpunk, fantasy, realistic...",
# #                                    label_visibility="collapsed")
    
# #     # Number of images slider
# #     st.markdown('<label class="custom-label">Number of Images: 1</label>', unsafe_allow_html=True)
# #     num_images = st.slider("", 1, 4, 1, label_visibility="collapsed")
    
# #     # Advanced settings
# #     with st.expander("Advanced Settings"):
# #         col1, col2 = st.columns(2)
        
# #         with col1:
# #             aspect_ratio = st.selectbox("Aspect Ratio", 
# #                                       ["Square (1:1)", "Portrait (2:3)", "Landscape (3:2)", "Widescreen (16:9)"])
            
# #             negative_prompt = st.text_area("Negative Prompt", 
# #                                          placeholder="Elements to avoid in the image...",
# #                                          height=100)
        
# #         with col2:
# #             quality = st.select_slider("Quality", options=["Standard", "High", "Ultra"])
            
# #             seed = st.number_input("Seed (optional)", 
# #                                  min_value=0, 
# #                                  max_value=999999, 
# #                                  value=0, 
# #                                  help="Leave at 0 for random seed")
    
# #     # Generate button
# #     if 'generate_clicked' not in st.session_state:
# #         st.session_state.generate_clicked = False
        
# #     def click_generate():
# #         st.session_state.generate_clicked = True
    
# #     if st.button("✨ Generate Masterpiece", key="generate_btn", 
# #                 use_container_width=True, 
# #                 type="primary"):
# #         click_generate()
    
# #     st.markdown('</div>', unsafe_allow_html=True)
    
# #     # Right column
# #     st.markdown('<div class="right-column">', unsafe_allow_html=True)
    
# #     # Preview section
# #     st.markdown('<h3 class="section-title">Preview</h3>', unsafe_allow_html=True)
    
# #     # Display current image if generate was clicked, otherwise show placeholder
# #     if st.session_state.generate_clicked and prompt:
# #         # Generate the image
# #         generated_img = generate_image(prompt, style, context_mood, num_images)
        
# #         # Display the image
# #         st.image(generated_img, use_column_width=True)
        
# #         # Add download button
# #         img_buffer = BytesIO()
# #         generated_img.save(img_buffer, format="PNG")
# #         img_bytes = img_buffer.getvalue()
        
# #         st.download_button(
# #             label="⬇️ Download Image",
# #             data=img_bytes,
# #             file_name="artisan_ai_image.png",
# #             mime="image/png",
# #             use_container_width=True
# #         )
        
# #         # Reset the state
# #         st.session_state.generate_clicked = False
# #     else:
# #         # Show placeholder
# #         st.markdown("""
# #         <div class="preview-container">
# #             <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
# #                 <path d="M4 16L8.586 11.414C8.96106 11.0391 9.46967 10.8284 10 10.8284C10.5303 10.8284 11.0389 11.0391 11.414 11.414L16 16M14 14L15.586 12.414C15.9611 12.0391 16.4697 11.8284 17 11.8284C17.5303 11.8284 18.0389 12.0391 18.414 12.414L20 14M14 8H14.01M6 20H18C18.5304 20 19.0391 19.7893 19.4142 19.4142C19.7893 19.0391 20 18.5304 20 18V6C20 5.46957 19.7893 4.96086 19.4142 4.58579C19.0391 4.21071 18.5304 4 18 4H6C5.46957 4 4.96086 4.21071 4.58579 4.58579C4.21071 4.96086 4 5.46957 4 6V18C4 18.5304 4.21071 19.0391 4.58579 19.4142C4.96086 19.7893 5.46957 20 6 20Z" stroke="rgba(224, 224, 224, 0.3)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
# #             </svg>
# #             <p class="preview-placeholder">Your image will appear here</p>
# #         </div>
# #         """, unsafe_allow_html=True)
    
# #     st.markdown('</div>', unsafe_allow_html=True)
    
# #     # Close the two-column layout
# #     st.markdown('</div>', unsafe_allow_html=True)
    
# #     # Close the content container
# #     st.markdown('</div>', unsafe_allow_html=True)

# # # Run the application
# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# from PIL import Image
# import base64
# import io
# import time
# import random
# import asyncio
# import grpc
# import sys
# import os
# from io import BytesIO

# # Add path for protos
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from app.protos import text2image_pb2 as pb2
# from app.protos import text2image_pb2_grpc as pb2_grpc

# # Set page configuration
# st.set_page_config(
#     page_title="Artisan AI - Text to Image Generator",
#     page_icon="✨",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for styling with dark theme
# def apply_custom_css():
#     st.markdown("""
#     <style>
#         /* Main theme colors and fonts */
#         :root {
#             --primary: #BB86FC;
#             --primary-variant: #9D4EDD;
#             --secondary: #E0AAFF;
#             --secondary-variant: #F50057;
#             --background: #0F0A1E;
#             --surface: #1A1625;
#             --surface-variant: #231C34;
#             --error: #CF6679;
#             --on-primary: #FFFFFF;
#             --on-secondary: #000000;
#             --on-background: #E0E0E0;
#             --on-surface: #E0E0E0;
#             --on-error: #000000;
#             --card-border: #2D2640;
#             --card-shadow: rgba(0, 0, 0, 0.5);
#         }
        
#         /* Base styling */
#         .stApp {
#             background-color: var(--background);
#             background-image: linear-gradient(180deg, #0F0A1E 0%, #1A1625 100%);
#             font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, sans-serif;
#             color: var(--on-background);
#         }
        
#         /* Remove default Streamlit padding */
#         .main .block-container {
#             padding-top: 1rem;
#             padding-bottom: 1rem;
#             max-width: 100%;
#             padding-left: 1rem;
#             padding-right: 1rem;
#         }
        
#         /* Header styling */
#         .header-container {
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             padding: 1rem 2rem;
#             border-bottom: 1px solid var(--card-border);
#             background-color: rgba(15, 10, 30, 0.8);
#             backdrop-filter: blur(10px);
#             position: sticky;
#             top: 0;
#             z-index: 999;
#         }
        
#         .logo-container {
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             width: 60px;
#             height: 60px;
#             background: rgba(187, 134, 252, 0.1);
#             border-radius: 50%;
#             margin-right: 1rem;
#             box-shadow: 0 0 15px rgba(187, 134, 252, 0.3);
#         }
        
#         .logo-icon {
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             width: 40px;
#             height: 40px;
#             background: linear-gradient(135deg, #9D4EDD 0%, #C77DFF 100%);
#             border-radius: 50%;
#             margin-right: 0.75rem;
#         }
        
#         .logo-text {
#             font-size: 2.2rem;
#             font-weight: 700;
#             background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-left: 0.5rem;
#             letter-spacing: -0.5px;
#         }
        
#         .nav-links {
#             display: flex;
#             align-items: center;
#             gap: 2rem;
#         }
        
#         .nav-link {
#             color: var(--on-background);
#             text-decoration: none;
#             font-weight: 500;
#             transition: color 0.2s ease;
#         }
        
#         .nav-link:hover {
#             color: var(--primary);
#         }
        
#         .sign-in-button {
#             background: transparent;
#             color: var(--primary);
#             border: 1px solid var(--primary);
#             border-radius: 6px;
#             padding: 0.5rem 1rem;
#             font-weight: 600;
#             cursor: pointer;
#             transition: all 0.2s ease;
#         }
        
#         .sign-in-button:hover {
#             background-color: rgba(187, 134, 252, 0.1);
#         }
        
#         .subtitle {
#             font-size: 1.2rem;
#             color: rgba(224, 224, 224, 0.7);
#             margin-top: -0.5rem;
#             margin-bottom: 2rem;
#         }
        
#         /* Tab styling */
#         .tab-container {
#             display: flex;
#             max-width: 500px;
#             margin: 0 auto 2rem;
#             background-color: var(--surface-variant);
#             border-radius: 50px;
#             padding: 0.25rem;
#         }
        
#         .tab {
#             flex: 1;
#             text-align: center;
#             padding: 0.75rem 1rem;
#             cursor: pointer;
#             border-radius: 50px;
#             font-weight: 600;
#             transition: all 0.2s ease;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             gap: 0.5rem;
#         }
        
#         .tab.active {
#             background-color: var(--primary);
#             color: black;
#         }
        
#         .tab:not(.active) {
#             color: var(--on-background);
#         }
        
#         .tab:not(.active):hover {
#             background-color: rgba(187, 134, 252, 0.1);
#         }
        
#         /* Hero section */
#         .hero-container {
#             text-align: center;
#             padding: 3rem 1rem;
#         }
        
#         .hero-title {
#             font-size: 2.5rem;
#             font-weight: 700;
#             color: var(--primary);
#             margin-bottom: 1rem;
#             line-height: 1.2;
#         }
        
#         .hero-subtitle {
#             font-size: 1.1rem;
#             color: rgba(224, 224, 224, 0.8);
#             max-width: 700px;
#             margin: 0 auto 2rem;
#             line-height: 1.5;
#         }
        
#         /* Main content container */
#         .content-container {
#             background-color: var(--surface);
#             border-radius: 12px;
#             border: 1px solid var(--card-border);
#             max-width: 1200px;
#             margin: 0 auto;
#             padding: 2rem;
#         }
        
#         /* Two column layout */
#         .two-column-layout {
#             display: flex;
#             gap: 2rem;
#         }
        
#         .left-column {
#             flex: 3;
#         }
        
#         .right-column {
#             flex: 2;
#         }
        
#         /* Section styling */
#         .section-title {
#             font-size: 1.25rem;
#             font-weight: 600;
#             color: var(--on-background);
#             margin-bottom: 1rem;
#         }
        
#         /* Selectbox styling */
#         .stSelectbox > div > div {
#             background-color: var(--surface-variant);
#             border: 1px solid var(--card-border);
#             border-radius: 8px;
#         }
        
#         .stSelectbox > div > div > div {
#             color: var(--on-background);
#         }
        
#         /* Slider styling */
#         .stSlider > div > div > div > div > div {
#             background-color: var(--primary);
#         }
        
#         .stSlider > div > div > div > div > div > div {
#             background-color: var(--primary);
#             border-color: var(--primary);
#         }
        
#         /* Card styling */
#         .card {
#             background-color: var(--surface-variant);
#             border-radius: 12px;
#             padding: 1.5rem;
#             box-shadow: 0 8px 24px var(--card-shadow);
#             margin-bottom: 1.5rem;
#             border: 1px solid var(--card-border);
#             position: relative;
#             overflow: hidden;
#         }
        
#         .card::before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             right: 0;
#             height: 3px;
#             background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
#             border-radius: 12px 12px 0 0;
#         }
        
#         .card-title {
#             font-size: 1.25rem;
#             font-weight: 600;
#             color: var(--primary);
#             margin-bottom: 1.25rem;
#             display: flex;
#             align-items: center;
#         }
        
#         .card-title-icon {
#             margin-right: 0.5rem;
#             font-size: 1.5rem;
#         }
        
#         /* Input field styling */
#         .stTextInput > div > div > input, .stTextArea > div > div > textarea {
#             background-color: var(--surface-variant);
#             border-radius: 8px;
#             border: 1px solid rgba(187, 134, 252, 0.3);
#             padding: 0.75rem;
#             font-size: 1rem;
#             color: var(--on-background);
#             transition: all 0.3s ease;
#         }
        
#         .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
#             border-color: var(--primary);
#             box-shadow: 0 0 0 2px rgba(187, 134, 252, 0.2);
#         }
        
#         .stTextArea > div > div > textarea {
#             background-color: var(--surface-variant);
#             border: 1px solid var(--card-border);
#             border-radius: 8px;
#             color: var(--on-background);
#             font-size: 1rem;
#             padding: 0.75rem 1rem;
#         }
        
#         /* Remove Streamlit branding */
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
        
#         /* Hide default Streamlit elements */
#         .stDeployButton {
#             display: none !important;
#         }
        
#         /* Button styling */
#         .stButton > button {
#             background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
#             color: var(--on-primary);
#             border: none;
#             border-radius: 8px;
#             padding: 0.75rem 1.5rem;
#             font-weight: 600;
#             transition: all 0.3s ease;
#             width: 100%;
#             position: relative;
#             overflow: hidden;
#         }
        
#         .stButton > button:hover {
#             box-shadow: 0 4px 20px rgba(187, 134, 252, 0.4);
#             transform: translateY(-2px);
#         }
        
#         .stButton > button:active {
#             transform: translateY(0);
#         }
        
#         .stButton > button::after {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
#             transform: translateX(-100%);
#         }
        
#         .stButton > button:hover::after {
#             transform: translateX(100%);
#             transition: transform 0.6s ease;
#         }
        
#         /* Selectbox styling */
#         .stSelectbox > div > div {
#             background-color: rgba(15, 10, 30, 0.5);
#             border-radius: 8px;
#             border: 1px solid rgba(187, 134, 252, 0.3);
#             color: var(--on-background);
#         }
        
#         .stSelectbox > div > div:focus {
#             border-color: var(--primary);
#             box-shadow: 0 0 0 2px rgba(187, 134, 252, 0.2);
#         }
        
#         /* Image gallery styling */
#         .image-container {
#             position: relative;
#             border-radius: 12px;
#             overflow: hidden;
#             box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
#             transition: all 0.3s ease;
#             height: 100%;
#             border: 1px solid var(--card-border);
#         }
        
#         .image-container:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
#             border-color: rgba(187, 134, 252, 0.5);
#         }
        
#         .image-container img {
#             width: 100%;
#             height: 100%;
#             object-fit: cover;
#             border-radius: 12px;
#             transition: transform 0.5s ease;
#         }
        
#         .image-container:hover img {
#             transform: scale(1.05);
#         }
        
#         .image-overlay {
#             position: absolute;
#             bottom: 0;
#             left: 0;
#             right: 0;
#             background: linear-gradient(0deg, rgba(15,10,30,0.9) 0%, rgba(15,10,30,0) 100%);
#             padding: 1.5rem 1rem 1rem;
#             color: white;
#             border-radius: 0 0 12px 12px;
#             opacity: 0;
#             transition: opacity 0.3s ease;
#         }
        
#         .image-container:hover .image-overlay {
#             opacity: 1;
#         }
        
#         /* Placeholder styling */
#         .placeholder-container {
#             background-color: rgba(187, 134, 252, 0.05);
#             border: 2px dashed rgba(187, 134, 252, 0.2);
#             border-radius: 12px;
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             padding: 2rem;
#             height: 100%;
#             min-height: 300px;
#             transition: all 0.3s ease;
#         }
        
#         .placeholder-container:hover {
#             background-color: rgba(187, 134, 252, 0.08);
#             border-color: rgba(187, 134, 252, 0.3);
#         }
        
#         .placeholder-icon {
#             font-size: 3.5rem;
#             color: rgba(187, 134, 252, 0.4);
#             margin-bottom: 1rem;
#         }
        
#         .placeholder-text {
#             color: rgba(224, 224, 224, 0.6);
#             text-align: center;
#             font-size: 1.1rem;
#         }
        
#         /* Progress bar styling */
#         .stProgress > div > div > div {
#             background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
#         }
        
#         /* Sidebar styling */
#         [data-testid="stSidebar"] {
#             background-color: var(--surface-variant);
#             border-right: 1px solid var(--card-border);
#         }
        
#         .sidebar-header {
#             font-size: 1.5rem;
#             font-weight: 700;
#             color: var(--primary);
#             margin-bottom: 1.5rem;
#             padding-bottom: 0.5rem;
#             border-bottom: 1px solid rgba(187, 134, 252, 0.2);
#         }
        
#         .sidebar-logo {
#             width: 70px;
#             height: 70px;
#             background: linear-gradient(135deg, #9D4EDD 0%, #C77DFF 100%);
#             border-radius: 50%;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             margin-bottom: 1rem;
#             box-shadow: 0 0 20px rgba(157, 78, 221, 0.3);
#         }
        
#         /* Tabs styling */
#         .stTabs [data-baseweb="tab-list"] {
#             gap: 8px;
#             background-color: var(--surface-variant);
#             padding: 4px;
#             border-radius: 8px;
#         }
        
#         .stTabs [data-baseweb="tab"] {
#             background-color: transparent;
#             border-radius: 6px;
#             padding: 0.75rem 1rem;
#             color: rgba(224, 224, 224, 0.7);
#         }
        
#         .stTabs [aria-selected="true"] {
#             background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%) !important;
#             color: var(--on-primary) !important;
#             font-weight: 600;
#         }
        
#         /* Status messages */
#         .success-message {
#             background-color: rgba(76, 175, 80, 0.1);
#             border-left: 4px solid #4CAF50;
#             padding: 1rem;
#             border-radius: 4px;
#             margin-bottom: 1rem;
#             color: #A5D6A7;
#         }
        
#         .info-message {
#             background-color: rgba(187, 134, 252, 0.1);
#             border-left: 4px solid var(--primary);
#             padding: 1rem;
#             border-radius: 4px;
#             margin-bottom: 1rem;
#             color: var(--primary);
#         }
        
#         /* Expander styling */
#         .streamlit-expanderHeader {
#             background-color: var(--surface-variant);
#             border-radius: 8px;
#             color: var(--primary);
#             font-weight: 600;
#         }
        
#         /* Responsive adjustments */
#         @media (max-width: 768px) {
#             .logo-text {
#                 font-size: 1.8rem;
#             }
            
#             .subtitle {
#                 font-size: 1rem;
#             }
            
#             .card {
#                 padding: 1.25rem;
#             }
#         }
        
#         /* Footer styling */
#         .footer {
#             text-align: center;
#             padding: 2rem 0;
#             color: rgba(224, 224, 224, 0.5);
#             font-size: 0.875rem;
#             margin-top: 2rem;
#             border-top: 1px solid var(--card-border);
#         }
        
#         /* Animation for loading */
#         @keyframes pulse {
#             0% {
#                 opacity: 0.6;
#             }
#             50% {
#                 opacity: 1;
#             }
#             100% {
#                 opacity: 0.6;
#             }
#         }
        
#         .loading-animation {
#             animation: pulse 1.5s infinite ease-in-out;
#         }
        
#         /* Glow effect for elements */
#         .glow-effect {
#             box-shadow: 0 0 15px rgba(187, 134, 252, 0.4);
#         }
        
#         /* Download button styling */
#         .download-button {
#             display: inline-block;
#             background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
#             color: var(--on-primary);
#             text-align: center;
#             padding: 0.75rem 1.5rem;
#             margin-top: 1rem;
#             border-radius: 8px;
#             text-decoration: none;
#             font-weight: 600;
#             transition: all 0.3s ease;
#             width: 100%;
#             position: relative;
#             overflow: hidden;
#         }
        
#         .download-button:hover {
#             box-shadow: 0 4px 20px rgba(187, 134, 252, 0.4);
#             transform: translateY(-2px);
#         }
        
#         .download-button::after {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
#             transform: translateX(-100%);
#         }
        
#         .download-button:hover::after {
#             transform: translateX(100%);
#             transition: transform 0.6s ease;
#         }
        
#         /* Custom checkbox styling */
#         .stCheckbox > div > div > div > div {
#             border-color: var(--primary) !important;
#         }
        
#         /* Custom radio button styling */
#         .stRadio > div > div > div > div {
#             border-color: var(--primary) !important;
#         }
        
#         /* Custom number input styling */
#         .stNumberInput > div > div > input {
#             background-color: rgba(15, 10, 30, 0.5);
#             border-radius: 8px;
#             border: 1px solid rgba(187, 134, 252, 0.3);
#             color: var(--on-background);
#         }
        
#         /* Custom divider */
#         .custom-divider {
#             height: 1px;
#             background: linear-gradient(90deg, transparent, rgba(187, 134, 252, 0.3), transparent);
#             margin: 1.5rem 0;
#         }
        
#         /* Tooltip styling */
#         .tooltip {
#             position: relative;
#             display: inline-block;
#             cursor: pointer;
#         }
        
#         .tooltip .tooltiptext {
#             visibility: hidden;
#             width: 120px;
#             background-color: var(--surface-variant);
#             color: var(--on-surface);
#             text-align: center;
#             border-radius: 6px;
#             padding: 5px;
#             position: absolute;
#             z-index: 1;
#             bottom: 125%;
#             left: 50%;
#             margin-left: -60px;
#             opacity: 0;
#             transition: opacity 0.3s;
#             border: 1px solid var(--card-border);
#         }
        
#         .tooltip:hover .tooltiptext {
#             visibility: visible;
#             opacity: 1;
#         }
        
#         /* Label styling */
#         label {
#             color: var(--primary) !important;
#             font-weight: 500 !important;
#         }
        
#         /* Caption styling */
#         .caption {
#             font-size: 0.85rem;
#             color: rgba(224, 224, 224, 0.6);
#             margin-top: 0.5rem;
#         }
        
#         /* Badge styling */
#         .badge {
#             display: inline-block;
#             padding: 0.25rem 0.5rem;
#             background-color: rgba(187, 134, 252, 0.2);
#             color: var(--primary);
#             border-radius: 4px;
#             font-size: 0.75rem;
#             font-weight: 600;
#             margin-right: 0.5rem;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # Backend connection functions
# async def generate_image_backend(client, text, context):
#     """
#     Send request to the gRPC backend service to generate an image
#     """
#     request = pb2.ImageRequest(text=text, context=context)
#     try:
#         response = await client.GenerateImage(request)
#         if response.status == 200:
#             img_data = base64.b64decode(response.image_base64)
#             return Image.open(BytesIO(img_data))
#         else:
#             st.error(f"Failed: {response.message}")
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#     return None

# async def generate_images_backend(prompts):
#     """
#     Generate multiple images by sending requests to the backend service
#     """
#     channel = grpc.aio.insecure_channel("localhost:50051")
#     #BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost:50051")
#     #channel = grpc.aio.insecure_channel(BACKEND_HOST)
#     client = pb2_grpc.Text2ImageServiceStub(channel)

#     tasks = [generate_image_backend(client, text, ctx) for text, ctx in prompts]
#     return await asyncio.gather(*tasks)

# # Function to create a placeholder image (fallback if backend fails)
# def create_placeholder_image(width=512, height=512, color=(100, 70, 150)):
#     img = Image.new('RGB', (width, height), color=color)
#     return img

# # Function to generate image - connects to backend or uses fallback
# def generate_image(prompt, style, quality, seed=None, use_backend=True):
#     """
#     Generate an image using the backend service or fallback to placeholder
#     """
#     # Show progress indicators
#     progress_bar = st.progress(0)
#     status_text = st.empty()
    
#     try:
#         if use_backend:
#             # Prepare for backend request
#             context = style  # Use style as context
            
#             # Setup event loop for async operation
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
            
#             # Simulate progress while waiting for backend
#             for i in range(101):
#                 progress_bar.progress(i)
#                 status_text.text(f"Generating your masterpiece: {i}%")
#                 time.sleep(0.02)
            
#             # Call backend service
#             results = loop.run_until_complete(generate_images_backend([(prompt, context)]))
            
#             # Get the result
#             if results and results[0] is not None:
#                 img = results[0]
#             else:
#                 # Fallback to placeholder if backend fails
#                 img = create_fallback_image(prompt, style, quality, seed)
#         else:
#             # Use fallback method
#             img = create_fallback_image(prompt, style, quality, seed)
            
#             # Simulate progress
#             for i in range(101):
#                 progress_bar.progress(i)
#                 status_text.text(f"Generating your masterpiece: {i}%")
#                 time.sleep(0.02)
    
#     except Exception as e:
#         st.error(f"Error generating image: {str(e)}")
#         img = create_fallback_image(prompt, style, quality, seed)
    
#     # Clear the progress indicators
#     progress_bar.empty()
#     status_text.empty()
    
#     return img

# # Fallback image generation if backend fails
# def create_fallback_image(prompt, style, quality, seed=None):
#     """
#     Create a fallback image if the backend service fails
#     """
#     # Create a random color based on the prompt
#     if seed is not None:
#         random.seed(seed)
    
#     # Generate a color based on the prompt and style
#     r = (hash(prompt) % 150) + 50
#     g = (hash(style) % 100) + 50
#     b = (hash(prompt + style) % 200) + 50
    
#     # Adjust color based on quality
#     brightness = 0.5 + (quality / 20)
#     r = min(255, int(r * brightness))
#     g = min(255, int(g * brightness))
#     b = min(255, int(b * brightness))
    
#     # Create the image
#     return create_placeholder_image(512, 512, (r, g, b))

# # Function to convert PIL Image to base64 for display
# def get_image_base64(img):
#     buffered = io.BytesIO()
#     img.save(buffered, format="PNG")
#     img_str = base64.b64encode(buffered.getvalue()).decode()
#     return img_str

# # Main application
# def main():
#     # Apply custom CSS
#     apply_custom_css()
    
#     # Sidebar
#     with st.sidebar:
#         st.markdown("""
#         <div style="text-align: center; margin-bottom: 20px;">
#             <div style="background: rgba(187, 134, 252, 0.1); border-radius: 50%; width: 80px; height: 80px; margin: 0 auto; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 20px rgba(187, 134, 252, 0.3);">
#                 <span style="font-size: 40px;">🎨</span>
#             </div>
#             <h1 style="margin-top: 10px; color: #BB86FC; font-weight: bold;">Artisan AI</h1>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("<p style='color: rgba(224, 224, 224, 0.7); text-align: center;'>Transform your ideas into stunning visuals with our AI-powered image generator.</p>", unsafe_allow_html=True)
        
#         st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
        
#         with st.expander("ℹ️ About", expanded=False):
#             st.markdown("""
#             <div style="background-color: rgba(15, 10, 30, 0.5); padding: 15px; border-radius: 8px; border-left: 3px solid #BB86FC;">
#             <strong style="color: #FF4081;">Artisan AI</strong> uses state-of-the-art machine learning models to generate images from text descriptions.
            
#             <ul style="color: rgba(224, 224, 224, 0.8);">
#                 <li>📝 Enter detailed prompts</li>
#                 <li>🎯 Provide context for better results</li>
#                 <li>🖼️ Generate multiple images at once</li>
#                 <li>✨ Experiment with different styles</li>
#             </ul>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with st.expander("🔧 Tips & Tricks", expanded=False):
#             st.markdown("""
#             <div style="background-color: rgba(15, 10, 30, 0.5); padding: 15px; border-radius: 8px; border-left: 3px solid #FF4081;">
#             <strong style="color: #BB86FC;">For best results:</strong>
            
#             <ol style="color: rgba(224, 224, 224, 0.8);">
#                 <li>Be specific in your descriptions</li>
#                 <li>Include details about style, mood, lighting</li>
#                 <li>Use context to guide the aesthetic direction</li>
#                 <li>Try different variations of the same prompt</li>
#                 <li>Experiment with different quality settings</li>
#             </ol>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
        
#         # Connection settings
#         with st.expander("⚙️ Connection Settings", expanded=False):
#             use_backend = st.checkbox("Use Backend Service", value=True, key="sidebar_use_backend")
#             backend_url = st.text_input("Backend URL", value="localhost:50051", key="sidebar_backend_url")
#             st.caption("Change only if you know what you're doing")
        
#         # Sample prompts
#         st.markdown("<h3 style='color: #BB86FC;'>Sample Prompts</h3>", unsafe_allow_html=True)
        
#         sample_prompts = [
#             "A serene lake at sunset with mountains in the background",
#             "Cyberpunk cityscape with neon lights and flying cars",
#             "Enchanted forest with glowing mushrooms and fairy lights",
#             "Abstract portrait made of geometric shapes and vibrant colors"
#         ]
        
#         for i, prompt in enumerate(sample_prompts):
#             if st.button(f"Try Prompt {i+1}", key=f"sample_{i}"):
#                 if 'prompt_input' not in st.session_state:
#                     st.session_state.prompt_input = prompt
#                 else:
#                     st.session_state.prompt_input = prompt
#                 st.rerun()
        
#         st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
#         st.markdown("""
#         <div style="text-align: center; color: rgba(224, 224, 224, 0.5); font-size: 0.8rem;">
#             © 2025 Artisan AI | <a href="#" style="color: #BB86FC;">Documentation</a>
#         </div>
#         """, unsafe_allow_html=True)
    
#     # Header
#     st.markdown("""
#     <div class="header-container">
#         <div class="logo-container">
#             <div class="logo-icon">
#                 <span style="font-size: 20px;">✨</span>
#             </div>
#             <div class="logo-text">Artisan AI</div>
#         </div>
#         <div class="nav-links">
#             <a href="#" class="nav-link">Styles</a>
#             <a href="#" class="nav-link">Help</a>
#             <button class="sign-in-button">Sign In</button>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Hero section
#     st.markdown("""
#     <div class="hero-container">
#         <h1 class="hero-title">Transform Your Words Into Visual Masterpieces</h1>
#         <p class="hero-subtitle">Enter your prompt below and watch as our AI brings your imagination to life with stunning visuals.</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Create tabs for different sections
#     tabs = st.tabs(["✨ Create", "🖼️ Gallery", "⚙️ Settings"])
    
#     with tabs[0]:  # Create tab
#         # Create two columns for input and preview
#         col1, col2 = st.columns([3, 2])
        
#         with col1:
#             # Input card
#             st.markdown('<div class="card">', unsafe_allow_html=True)
#             st.markdown('<div class="card-title"><span class="card-title-icon">✏️</span> Describe Your Vision</div>', unsafe_allow_html=True)
            
#             # Text prompt input
#             prompt_value = st.session_state.get('prompt_input', '')
#             prompt = st.text_area(
#                 "Enter your prompt",
#                 value=prompt_value,
#                 placeholder="Describe the image you want to create in detail... (e.g., A serene lake at sunset with mountains in the background and a small cabin by the shore)",
#                 height=150,
#                 key="prompt_area"
#             )
            
#             # Style and settings
#             col_style, col_quality = st.columns(2)
            
#             with col_style:
#                 style = st.selectbox(
#                     "Art Style",
#                     ["Digital Art", "Oil Painting", "Watercolor", "Sketch", 
#                      "Pixel Art", "3D Render", "Anime", "Comic Book", "Fantasy", "Realistic"],
#                     key="style_select"
#                 )
            
#             with col_quality:
#                 quality = st.slider("Image Quality", 1, 10, 7, key="quality_slider")
#                 st.markdown('<p class="caption">Higher quality may take longer to generate</p>', unsafe_allow_html=True)
            
#             # Advanced options in an expander
#             with st.expander("Advanced Options"):
#                 col_aspect, col_seed = st.columns(2)
                
#                 with col_aspect:
#                     aspect_ratio = st.selectbox(
#                         "Aspect Ratio",
#                         ["Square (1:1)", "Portrait (2:3)", "Landscape (3:2)", "Widescreen (16:9)"],
#                         key="aspect_ratio_select"
#                     )
                
#                 with col_seed:
#                     use_seed = st.checkbox("Use Seed", value=False, key="use_seed_checkbox")
#                     seed = st.number_input("Seed Value", value=42, disabled=not use_seed, key="seed_input")
                
#                 st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
                
#                 col_mood, col_detail = st.columns(2)
                
#                 with col_mood:
#                     mood = st.selectbox(
#                         "Mood",
#                         ["Any", "Happy", "Sad", "Mysterious", "Energetic", "Calm", "Dramatic"],
#                         key="mood_select"
#                     )
                
#                 with col_detail:
#                     detail_level = st.select_slider(
#                         "Detail Level",
#                         options=["Low", "Medium", "High", "Ultra"],
#                         key="detail_slider"
#                     )
            
#             # Generate button
#             if st.button("✨ Generate Masterpiece", key="generate_btn"):
#                 if prompt:
#                     # Store the prompt and settings in session state
#                     if 'history' not in st.session_state:
#                         st.session_state.history = []
                    
#                     # Get backend setting from sidebar
#                     use_backend_service = st.session_state.get('use_backend', True)
                    
#                     # Generate the image
#                     seed_value = seed if use_seed else None
#                     generated_img = generate_image(prompt, style, quality, seed_value, use_backend=use_backend_service)
                    
#                     # Store in session state
#                     st.session_state.current_image = generated_img
                    
#                     # Add to history
#                     st.session_state.history.append({
#                         'prompt': prompt,
#                         'style': style,
#                         'quality': quality,
#                         'image': generated_img
#                     })
                    
#                     # Display success message
#                     st.markdown("""
#                     <div class="success-message">
#                         <strong>Success!</strong> Your masterpiece has been created.
#                     </div>
#                     """, unsafe_allow_html=True)
#                 else:
#                     st.warning("Please enter a prompt to generate an image.")
            
#             st.markdown('</div>', unsafe_allow_html=True)
        
#         with col2:
#             # Preview card
#             st.markdown('<div class="card">', unsafe_allow_html=True)
#             st.markdown('<div class="card-title"><span class="card-title-icon">🖼️</span> Image Preview</div>', unsafe_allow_html=True)
            
#             # Display current image if available, otherwise show placeholder
#             if 'current_image' in st.session_state:
#                 st.image(st.session_state.current_image, use_container_width=True)
                
#                 # Image actions
#                 col1, col2 = st.columns(2)
                
#                 with col1:
#                     # Download button
#                     img_base64 = get_image_base64(st.session_state.current_image)
#                     download_link = f'<a href="data:image/png;base64,{img_base64}" download="artisan_ai_image.png" class="download-button">⬇️ Download</a>'
#                     st.markdown(download_link, unsafe_allow_html=True)
                
#                 with col2:
#                     # Regenerate button
#                     if st.button("🔄 Regenerate", key="regenerate_btn"):
#                         # Generate a new image with the same parameters
#                         if 'history' in st.session_state and st.session_state.history:
#                             last_item = st.session_state.history[-1]
#                             seed_value = seed if use_seed else None
#                             use_backend_service = st.session_state.get('use_backend', True)
#                             new_img = generate_image(last_item['prompt'], last_item['style'], last_item['quality'], seed_value, use_backend=use_backend_service)
#                             st.session_state.current_image = new_img
#                             st.session_state.history.append({
#                                 'prompt': last_item['prompt'],
#                                 'style': last_item['style'],
#                                 'quality': last_item['quality'],
#                                 'image': new_img
#                             })
#                             st.experimental_rerun()
#             else:
#                 # Placeholder
#                 st.markdown("""
#                 <div class="placeholder-container">
#                     <div class="placeholder-icon">✨</div>
#                     <div class="placeholder-text">Your generated masterpiece will appear here</div>
#                     <p style="color: rgba(224, 224, 224, 0.5); font-size: 0.9rem; margin-top: 1rem;">Enter a prompt and click "Generate Masterpiece" to create an image</p>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             st.markdown('</div>', unsafe_allow_html=True)
    
#     with tabs[1]:  # Gallery tab
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="card-title"><span class="card-title-icon">🖼️</span> Your Generated Masterpieces</div>', unsafe_allow_html=True)
        
#         if 'history' in st.session_state and st.session_state.history:
#             # Create a grid layout for the gallery
#             num_cols = 3
#             rows = [st.columns(num_cols) for _ in range((len(st.session_state.history) + num_cols - 1) // num_cols)]
            
#             for i, item in enumerate(st.session_state.history):
#                 col_idx = i % num_cols
#                 row_idx = i // num_cols
                
#                 with rows[row_idx][col_idx]:
#                     # Create a container for each image
#                     st.markdown('<div class="image-container">', unsafe_allow_html=True)
#                     st.image(item['image'], use_container_width=True)
#                     st.markdown("""
#                     <div class="image-overlay">
#                         <p style="font-weight: 600; margin-bottom: 0.5rem;">Image {}</p>
#                         <p style="font-size: 0.9rem; margin-bottom: 0.5rem; opacity: 0.8;">{}</p>
#                         <div>
#                             <span class="badge">{}</span>
#                             <span class="badge">Quality: {}</span>
#                         </div>
#                     </div>
#                     """.format(i+1, item['prompt'][:50] + "..." if len(item['prompt']) > 50 else item['prompt'], 
#                               item['style'], item['quality']), unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                    
#                     # Caption below the image
#                     st.markdown(f"<p style='text-align: center; color: rgba(224, 224, 224, 0.7); font-size: 0.9rem; margin-top: 0.5rem;'>Image {i+1}</p>", unsafe_allow_html=True)
#         else:
#             st.markdown("""
#             <div style="background-color: rgba(15, 10, 30, 0.5); padding: 2rem; border-radius: 12px; text-align: center;">
#                 <div style="font-size: 3rem; margin-bottom: 1rem;">🖼️</div>
#                 <h3 style="color: rgba(224, 224, 224, 0.8); margin-bottom: 1rem;">Your Gallery is Empty</h3>
#                 <p style="color: rgba(224, 224, 224, 0.6);">Generate some images to see them here!</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with tabs[2]:  # Settings tab
#         st.markdown('<div class="card">', unsafe_allow_html=True)
#         st.markdown('<div class="card-title"><span class="card-title-icon">⚙️</span> Application Settings</div>', unsafe_allow_html=True)
        
#         # Theme settings
#         st.subheader("Theme")
#         theme = st.radio("Select Theme", ["Dark", "Darker", "System Default"], horizontal=True, key="theme_radio")
        
#         # Backend settings
#         st.subheader("Backend Configuration")
#         use_backend = st.checkbox("Use Backend Service", value=True, key="settings_use_backend")
#         if use_backend:
#             backend_url = st.text_input("Backend URL", value="localhost:50051", key="settings_backend_url")
#             st.session_state['use_backend'] = True
#         else:
#             st.session_state['use_backend'] = False
#             st.info("Using local fallback image generation (for demo purposes only)")
        
#         # Image settings
#         st.subheader("Default Image Settings")
#         default_quality = st.slider("Default Quality", 1, 10, 7, key="default_quality_slider")
#         default_style = st.selectbox(
#             "Default Style",
#             ["Digital Art", "Oil Painting", "Watercolor", "Sketch", 
#              "Pixel Art", "3D Render", "Anime", "Comic Book", "Fantasy", "Realistic"],
#             key="default_style_select"
#         )
        
#         st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
        
#         # User preferences
#         st.subheader("User Preferences")
        
#         col1, col2 = st.columns(2)
#         with col1:
#             auto_save = st.checkbox("Auto-save generated images", value=True, key="auto_save_checkbox")
#             show_tooltips = st.checkbox("Show tooltips", value=True, key="show_tooltips_checkbox")
        
#         with col2:
#             enable_animations = st.checkbox("Enable animations", value=True, key="enable_animations_checkbox")
#             high_contrast = st.checkbox("High contrast mode", value=False, key="high_contrast_checkbox")
        
#         # Save settings button
#         if st.button("💾 Save Settings", key="save_settings_btn"):
#             st.success("Settings saved successfully!")
        
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Footer
#     st.markdown("""
#     <div class="footer">
#         <p>Powered by Artisan AI • Made with ❤️</p>
#         <p style="margin-top: 0.5rem; font-size: 0.8rem;">© 2025 Artisan AI • All rights reserved</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Run the application
# if __name__ == "__main__":
#     main()