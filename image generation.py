# Step 1: Install dependencies
!pip install diffusers transformers accelerate safetensors torch torchvision pillow

# Step 2: Import libraries
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Step 3: Load pre-trained Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"

if torch.cuda.is_available():
    # Use GPU with float16
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
else:
    # Use CPU with float32 (safer)
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")

# Step 4: Ask user for prompt at runtime
prompt = input("Enter the text prompt for image generation: ")

# Step 5: Generate image
image = pipe(prompt).images[0]

# Step 6: Show and save
image.show()
image.save("stable_diffusion_output.png")
print("✅ Image saved as stable_diffusion_output.png")
