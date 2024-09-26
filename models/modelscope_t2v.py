import torch
from diffusers import DiffusionPipeline
from utils.video_exporter import export_to_video

def generate_video():
    pipeline = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
    pipeline.enable_model_cpu_offload()
    pipeline.enable_vae_slicing()

    prompt = "Confident teddy bear surfer rides the wave in the tropics"
    video_frames = pipeline(prompt).frames[0]
    export_to_video(video_frames, "output/modelscope_t2v.mp4", fps=10)
