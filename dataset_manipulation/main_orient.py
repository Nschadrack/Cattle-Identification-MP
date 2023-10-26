import os
from orientation_transformations import (saving_transformed_image,
                                         aug_flip,
                                         aug_rotation,
                                         aug_perspective)

if __name__ == "__main__":
    ROOT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), "data")
    OG_DATA = os.path.join(ROOT_DATA_PATH, "OG")
    AUG_ROTATION_DATA = os.path.join(ROOT_DATA_PATH, "AUG_ROTATION")
    AUG_PERSPECTIVE_DATA = os.path.join(ROOT_DATA_PATH, "AUG_PERSPECTIVE")
    AUG_FLIP_DATA = os.path.join(ROOT_DATA_PATH, "AUG_FLIP")

    os.makedirs(ROOT_DATA_PATH, exist_ok=True)
    os.makedirs(OG_DATA, exist_ok=True)
    os.makedirs(AUG_ROTATION_DATA, exist_ok=True)
    os.makedirs(AUG_PERSPECTIVE_DATA, exist_ok=True)
    os.makedirs(AUG_FLIP_DATA, exist_ok=True)

    ALL_OG_CATTLE = os.listdir(OG_DATA)
    min_og_images = float("inf")
    for cattle in ALL_OG_CATTLE:
        cattle_images = os.listdir(os.path.join(OG_DATA, cattle))

        if len(cattle_images) < min_og_images:
            min_og_images = len(cattle_images)

    # Saving transformed rotation images
    saving_transformed_image(aug_rotation, OG_DATA, ALL_OG_CATTLE, AUG_ROTATION_DATA, min_og_images)

    # Saving transformed random perspective images
    saving_transformed_image(aug_perspective, OG_DATA, ALL_OG_CATTLE, AUG_PERSPECTIVE_DATA, min_og_images)

    # Saving transformed horizontally flipped images
    saving_transformed_image(aug_flip, OG_DATA, ALL_OG_CATTLE, AUG_FLIP_DATA, min_og_images)
