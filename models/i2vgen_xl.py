import torch
from diffusers import I2VGenXLPipeline
from utils.image_loader import load_image
from utils.video_exporter import export_to_gif

def generate_video():
    pipeline = I2VGenXLPipeline.from_pretrained("ali-vilab/i2vgen-xl", torch_dtype=torch.float16, variant="fp16")
    pipeline.enable_model_cpu_offload()

    image = load_image("assets/images/img_0009.png")

    prompt = "Papers were floating in the air on a table in the library"
    negative_prompt = "Distorted, discontinuous, Ugly, blurry, low resolution, motionless, static, disfigured, disconnected limbs, Ugly faces, incomplete arms"
    generator = torch.manual_seed(8888)

    frames = pipeline(
        prompt=prompt,
        image=image,
        num_inference_steps=50,
        negative_prompt=negative_prompt,
        guidance_scale=9.0,
        generator=generator
    ).frames[0]
    export_to_gif(frames, "output/generated_i2v.gif")
