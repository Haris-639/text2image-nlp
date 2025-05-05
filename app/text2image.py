from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import os
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
import uuid
import random
import threading
generation_lock = threading.Lock()


# Load the model only once at startup
model_path = "./models/stable-diffusion-v1-4"

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:32"
# Initialize pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float16
).to("cuda")


print("Tokenizer vocab size:", len(pipe.tokenizer))

# ThreadPoolExecutor to handle image generation concurrently
executor = ThreadPoolExecutor(max_workers=3)  # You can adjust the number of workers based on your system's capacity

def generate_image_sync(text, context):
    try:
        full_prompt = f"{text}. Context: {context}"
        print(f"[INFO] Generating image for: {full_prompt[:50]}...")

        with generation_lock:
            with torch.autocast("cuda"):
                result = pipe(full_prompt, guidance_scale=7.5, num_inference_steps=10)

        # Check if image was generated
        if not result or not result.images or result.images[0] is None:
            raise ValueError("Image generation returned None or empty result.")

        image = result.images[0]
        
        # Create a unique filename using timestamp and random number
        timestamp = int(time.time())
        rand_suffix = random.randint(1000, 9999)
        # output_path = f"generated_image_{timestamp}_{rand_suffix}.png"
        # output_dir = r"C:\Users\emadh\OneDrive\Desktop\text2image nlp project\generated_images"
        # filename = f"generated_image_{timestamp}_{rand_suffix}.png"
        # output_path = os.path.join(output_dir, filename)
        # image.save(output_path, format="PNG")
        # print(f"[SUCCESS] Image saved as '{filename}'.")
        output_dir = r"C:\Users\emadh\OneDrive\Desktop\text2image nlp project\generated_AImages"
        os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

        filename = f"generated_image_{timestamp}_{rand_suffix}.png"
        output_path = os.path.join(output_dir, filename)

        image.save(output_path, format="PNG")
        print(f"[SUCCESS] Image saved as '{filename}'.")


        # Save image to buffer for base64 encoding
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        torch.cuda.empty_cache()
        
        return buffered.getvalue()

    except Exception as e:
        print(f"[ERROR] Failed to generate image: {e}")
        torch.cuda.empty_cache()
        return None


# Wrapper function to run the blocking image generation in a thread pool
async def generate_image_from_text(text, context):
    loop = asyncio.get_event_loop()

    # Run the image generation function in a thread pool to avoid blocking the event loop
    image_bytes = await loop.run_in_executor(executor, generate_image_sync, text, context)

    return image_bytes
