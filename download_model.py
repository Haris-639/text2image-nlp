from diffusers import StableDiffusionPipeline
import torch

def load_model():
    model_id = "CompVis/stable-diffusion-v1-4"
    cache_dir = "./model_cache"  # Specify custom cache directory
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.float16,
            cache_dir=cache_dir  # Use custom cache directory for storing model weights
        )
        pipe = pipe.to("cuda")  # Move model to GPU
        pipe.save_pretrained("./models/stable-diffusion-v1-4")  # Save locally (v1.4)
        print("Model downloaded and saved successfully.")
        return pipe
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Download the model and save it locally
pipe = load_model()
