

# Diffusion-Based Video Generation Toolkit

This project provides an end-to-end solution for generating videos using advanced diffusion models. It includes examples of popular models such as Stable Video Diffusion, I2VGen-XL, AnimateDiff, and ModelScopeT2V. Whether you're interested in generating videos from text prompts, initial images, or combining images with text, this project covers various techniques and provides clear examples.

## Overview

- **Stable Video Diffusion (SVD)**: Generates short clips (2-4 seconds) from an initial image using a three-stage training process.
- **I2VGen-XL**: Produces high-resolution videos from text prompts or images, utilizing hierarchical encoders for detailed results.
- **AnimateDiff**: Animates static images by inserting a motion module into a pretrained diffusion model.
- **ModelScopeT2V**: Uses spatial and temporal convolutions for text-to-video generation, with options for watermark-free models.

## File and Folder Structure

Here is the structure of the project:

```
Diffusion-Based Video Generation Toolkit/
│
├── models/
│   ├── stable_video_diffusion.py
│   ├── i2vgen_xl.py
│   ├── animatediff.py
│   └── modelscope_t2v.py
│
├── assets/
│   ├── images/
│   │   └── rocket.png
│
├── utils/
│   ├── video_exporter.py
│   └── image_loader.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/video_generation_project.git
cd video_generation_project
```

### 2. Install Dependencies

Install the necessary Python packages using pip. This will ensure you have all the required libraries for running the scripts:

```bash
pip install -r requirements.txt
```

## Usage

The `main.py` script allows you to choose and run different video generation models. Follow these steps to generate a video:

1. **Prepare Inputs**: Ensure you have the initial image or text prompt ready. Place any images you want to use in the `assets/sample_images` directory.

2. **Run the Script**: Execute the `main.py` script. This script will guide you through selecting the model and specifying the necessary parameters. You can generate videos using:

   - **Stable Video Diffusion**: Generates a video from an initial image.
   - **I2VGen-XL**: Produces a video from a text prompt or an image.
   - **AnimateDiff**: Animates an image based on a text prompt.
   - **ModelScopeT2V**: Creates a video from a text prompt.

   ```bash
   python main.py
   ```

3. **Follow Prompts**: The script will prompt you for the model choice and input parameters. Provide the necessary information as required.

4. **Check Outputs**: Generated videos will be saved in the `outputs/` directory with names corresponding to the model used.

## Example

Here's an example of generating a video with the Stable Video Diffusion model:

1. Place an image in the `assets/sample_images/` directory.
2. Run the script:

   ```bash
   python main.py
   ```

3. Choose "Stable Video Diffusion" and provide the image file path.
4. The script will generate a video and save it to `outputs/`.

---

This README provides a clear structure, setup instructions, usage guidelines, and information about the project components.
