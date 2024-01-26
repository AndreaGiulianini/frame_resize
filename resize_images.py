import argparse
from PIL import Image
import os

def resize_with_white_border(input_path, output_path, percentage_increase):
    # Open image
    img = Image.open(input_path)

    # Border to add
    border_size = int(max(img.size) * (percentage_increase / 100))

    # New image blank
    new_size = (img.width, img.height)
    new_img = Image.new("RGB", new_size, "white")

    # Resize old image
    img = img.resize((img.width - border_size, img.height - border_size)) 

    # Get position for centering old image in new image
    paste_position = ((new_img.width - img.width) // 2, (new_img.height - img.height) // 2)
    
    # Paste old image in new image
    new_img.paste(img, paste_position)

    # Save image
    new_img.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resize images with added white borders.')
    parser.add_argument('--input_folder', type=str, required=True, help='Path to the input folder.')
    parser.add_argument('--output_folder', type=str, required=True, help='Path to the output folder.')
    parser.add_argument('--percentage_increase', type=int, default=20, help='Percentage increase for white borders.')

    args = parser.parse_args()
    input_folder = args.input_folder
    output_folder = args.output_folder
    percentage_increase = args.percentage_increase

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        print("filename: ", filename)
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".JPEG") or filename.endswith(".PNG"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            resize_with_white_border(input_path, output_path, percentage_increase)

    print("Complete.")
