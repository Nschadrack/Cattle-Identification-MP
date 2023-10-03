# Importing libraries
import torchvision
import os
from PIL import Image

# Defining paths

ROOT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), "data")
OG_DATA = os.path.join(ROOT_DATA_PATH, "OG")
AUG_ROTATION_DATA = os.path.join(ROOT_DATA_PATH, "aug_rotation")
AUG_PERSPECTIVE_DATA = os.path.join(ROOT_DATA_PATH, "aug_perspective")
AUG_FLIP_DATA = os.path.join(ROOT_DATA_PATH, "aug_flip")


""" Applying Transformations to Images """

# Function to add image distortion
def aug_perspective(imageFile, distortion_scale = 0.2):
    transform = torchvision.transforms.RandomPerspective(distortion_scale=distortion_scale)
    distorted_image = transform(imageFile)
    return distorted_image

# Function to flip image horizontally
def aug_flip(imageFile):
    transform = torchvision.transforms.RandomHorizontalFlip()
    flipped_image = transform(imageFile)
    return flipped_image

# Function to rotate the image
def aug_rotation(imageFile, rotation_prob = 10):
    transform = torchvision.transforms.RandomRotation(rotation_prob)
    rotated_image = transform(imageFile)
    return rotated_image

# Applying transformations
def saving_transformed_image(transformation_function, root_path):

    if not os.path.exists(AUG_ROTATION_DATA):
            os.mkdir(AUG_ROTATION_DATA)
    if not os.path.exists(AUG_FLIP_DATA):
        os.mkdir(AUG_FLIP_DATA)
    if not os.path.exists(AUG_PERSPECTIVE_DATA):
        os.mkdir(AUG_PERSPECTIVE_DATA)
    
    for subdirectory in os.listdir(OG_DATA):
        # Construct the path to the subdirectory
        subdirectory_path = os.path.join(OG_DATA, subdirectory)
        
        
        # Iterate over all files in the subdirectory and add images to the list
        for filename in os.listdir(subdirectory_path):
            img_path = os.path.join(subdirectory_path, filename)
            img = Image.open(img_path)
            transformed_image = transformation_function(img)
            if transformation_function.__name__ == "aug_rotation":
                if  not os.path.exists(os.path.join(AUG_ROTATION_DATA, subdirectory)):
                    os.mkdir(os.path.join(AUG_ROTATION_DATA, subdirectory))
                transformed_image.save(os.path.join(AUG_ROTATION_DATA, subdirectory, filename + "_rot.png"))

            elif transformation_function.__name__ == "aug_flip":
                if  not os.path.exists(os.path.join(AUG_FLIP_DATA, subdirectory)):
                    os.mkdir(os.path.join(AUG_FLIP_DATA, subdirectory))
                transformed_image.save(os.path.join(AUG_FLIP_DATA, subdirectory, filename + "_flip.png"))

            elif transformation_function.__name__ == "aug_perspective":
                if  not os.path.exists(os.path.join(AUG_PERSPECTIVE_DATA, subdirectory)):
                    os.mkdir(os.path.join(AUG_PERSPECTIVE_DATA, subdirectory))
                transformed_image.save(os.path.join(AUG_PERSPECTIVE_DATA, subdirectory, filename + "_pers.png"))

