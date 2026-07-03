# Text-to-Image Generation using Stable Diffusion

## Internship Task 2

This project uses a pre-trained **Stable Diffusion** model to generate images from text prompts. The model is loaded using the Hugging Face `diffusers` library and run on Google Colab.

---

## What this project does

- Takes a text prompt as input from the user
- Uses a pre-trained Stable Diffusion model (`runwayml/stable-diffusion-v1-5`) to generate an image based on that prompt
- Saves and displays the generated image

---

## Model Used

**Stable Diffusion v1.5** (`runwayml/stable-diffusion-v1-5`)

Stable Diffusion is a generative AI model that creates images from text by starting with random noise and gradually refining it into an image that matches the given prompt.

---

## Libraries Used

| Library | Purpose |
|---|---|
| `diffusers` | Loads and runs the Stable Diffusion pipeline |
| `transformers` | Required by diffusers for text encoding |
| `accelerate` | Speeds up model loading and inference |
| `safetensors` | Safer format for loading model weights |
| `torch`, `torchvision` | Deep learning framework used to run the model |
| `pillow` | For handling and saving images |

---

## How to Run (Google Colab)

1. Open [Google Colab](https://colab.research.google.com) and create a new notebook.
2. Go to **Runtime → Change runtime type → Hardware accelerator → GPU (T4)**.
3. Copy the code into a cell and run it.
4. When prompted, type your text prompt (example: `"a cricket player hitting a six, stadium background, digital art"`).
5. The generated image will be displayed and saved as `stable_diffusion_output.png`.

---

## Example Prompts

- "a cute puppy playing in a garden, digital art"
- "a bowler running in to bowl, cricket ground, sunset lighting, digital art"
- "a futuristic city at sunset, cyberpunk style"

---

## Output

The generated image is:
- Displayed directly in the notebook
- Saved to the Colab working directory as `stable_diffusion_output.png`

---

## Notes

- Using a **GPU runtime** is recommended. On CPU, image generation is much slower.
- The first run will take a few minutes since it downloads the model weights (~4 GB).
- This model is used only for generating images and does not require any training.

---

## Author

B.Tech Student — Internship Task 2 (Generative AI / Image Generation)
