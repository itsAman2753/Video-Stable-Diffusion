from models import stable_video_diffusion, i2vgen_xl, animatediff, modelscope_t2v
import sys

def main():
    print("Choose a model to generate video:")
    print("1. Stable Video Diffusion")
    print("2. I2VGen-XL")
    print("3. AnimateDiff")
    print("4. ModelScopeT2V")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        stable_video_diffusion.generate_video()
    elif choice == '2':
        i2vgen_xl.generate_video()
    elif choice == '3':
        animatediff.generate_video()
    elif choice == '4':
        modelscope_t2v.generate_video()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
