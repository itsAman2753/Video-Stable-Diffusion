from PIL import Image
import requests
from io import BytesIO

def load_image(image_path, size=None):
    if image_path.startswith("http"):
        response = requests.get(image_path)
        image = Image.open(BytesIO(response.content))
    else:
        image = Image.open(image_path)

    if size:
        image = image.resize(size)
    
    return image.convert("RGB")
