from PIL import Image
import imageio

def export_to_video(frames, output_path, fps=10):
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=1000 // fps,
        loop=0,
    )

def export_to_gif(frames, output_path):
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=50,
        loop=0,
    )
