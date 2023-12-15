# Importing libraries
import torchvision
import os
from PIL import Image

from low_resolution_and_lighting import show_or_save_pil_image

""" Applying Transformations to Images """


# Function to add image distortion
def aug_perspective(imageFile, distortion_scale=0.2):
    transform = torchvision.transforms.RandomPerspective(distortion_scale=distortion_scale)
    distorted_image = transform(imageFile)
    return distorted_image


# Function to flip image horizontally
def aug_flip(imageFile):
    transform = torchvision.transforms.RandomHorizontalFlip()
    flipped_image = transform(imageFile)
    return flipped_image


# Function to rotate the image
def aug_rotation(imageFile, rotation_prob=10):
    transform = torchvision.transforms.RandomRotation(rotation_prob)
    rotated_image = transform(imageFile)

    return rotated_image


# Applying transformations
def saving_transformed_image(transformation_function, og_path, cattle_names, target_path, min_images=4):
    # Reading individual cow images
    for cattle in cattle_names:
        cattle_images = os.listdir(os.path.join(og_path, cattle))

        count_images = 0
        for cattle_image in cattle_images:
            count_images += 1
            image_path = os.path.join(og_path, cattle, cattle_image)
            filename, extension = os.path.splitext(cattle_image)
            img = Image.open(image_path)
            # Iterate over all files in the subdirectory and add images to the list
            transformed_image = transformation_function(img)
            if transformation_function.__name__ == "aug_rotation":
                show_or_save_pil_image(transformed_image, save_image=True,
                                       save_path=os.path.join(target_path, cattle, filename + "_rot" + extension))

            elif transformation_function.__name__ == "aug_flip":
                show_or_save_pil_image(transformed_image, save_image=True,
                                       save_path=os.path.join(target_path, cattle, filename + "_flip" + extension))

            elif transformation_function.__name__ == "aug_perspective":
                show_or_save_pil_image(transformed_image, save_image=True,
                                       save_path=os.path.join(target_path, cattle, filename + "_pers" + extension))

            if count_images == min_images:l
                break
