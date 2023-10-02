from orientation_transformations import saving_transformed_image, aug_flip, aug_rotation, aug_perspective
import os

if __name__ == "__main__":
    ROOT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), "data")


    # Saving transformed rotation images
    saving_transformed_image(aug_rotation, ROOT_DATA_PATH)

    # Saving transformed random perspective images
    saving_transformed_image(aug_perspective, ROOT_DATA_PATH)

    # Saving transformed horizontally flipped images
    saving_transformed_image(aug_flip, ROOT_DATA_PATH)