import torch
from diffusers import StableVideoDiffusionPipeline
from utils.image_loader import load_image
from utils.video_exporter import export_to_video

def generate_video():
    pipeline = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16"
    )
    pipeline.enable_model_cpu_offload()

    image = load_image("assets/images/rocket.png", (1024, 576))

    generator = torch.manual_seed(42)
    frames = pipeline(image, decode_chunk_size=8, generator=generator).frames[0]
    export_to_video(frames, "output/generated_stable_video.mp4", fps=7)
