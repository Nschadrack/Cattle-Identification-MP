import json
import os
import numpy as np
import shutil

from low_resolution_and_lighting import (
    apply_gaussian_blur_and_subsampling,
    apply_gaussian_noise,
    run_brightness_contrast_adjustment)

from helpers import read_image_to_pil, height_width_checks

if __name__ == "__main__":
    ROOT_DATA_PATH = os.path.join(os.path.dirname(os.getcwd()), "data")
    OG_DATA = os.path.join(ROOT_DATA_PATH, "OG")
    AUG_LIGHTING_DATA = os.path.join(ROOT_DATA_PATH, "AUG_LIGHTING")
    AUG_RESOLUTION_DATA = os.path.join(ROOT_DATA_PATH, "AUG_RESOLUTION")

    os.makedirs(AUG_LIGHTING_DATA, exist_ok=True)
    os.makedirs(AUG_RESOLUTION_DATA, exist_ok=True)

    if len(os.listdir(AUG_LIGHTING_DATA)) > 0:  # delete already created images
        shutil.rmtree(AUG_LIGHTING_DATA)

    if len(os.listdir(AUG_RESOLUTION_DATA)) > 0:  # delete already created images
        shutil.rmtree(AUG_RESOLUTION_DATA)

    ALL_OG_CATTLE = os.listdir(OG_DATA)
    SAVE_IMAGE = True  # set it to True if you want to save images instead of displaying
    max_og_images = 0
    max_cattle_name = ""
    SUMMARY_STATISTICS = {
        "Cattle": {

        },
        "max_cattle": {
            "cattle_name": None,
            "number_of_og_images": 0
        }
    }
    min_og_images = float("inf")
    # Looking for cattle with small number of images
    for cattle in ALL_OG_CATTLE:
        cattle_images = os.listdir(os.path.join(OG_DATA, cattle))

        if len(cattle_images) < min_og_images:
            min_og_images = len(cattle_images)

    # Reading individual cow images
    for cattle in ALL_OG_CATTLE:
        cattle_images = os.listdir(os.path.join(OG_DATA, cattle))

        # Keeping the number of images for each cattle
        SUMMARY_STATISTICS["Cattle"][cattle] = {}
        SUMMARY_STATISTICS["Cattle"][cattle]["number_of_og_images"] = len(cattle_images)
        if max_og_images < len(cattle_images):
            max_og_images = len(cattle_images)
            max_cattle_name = cattle
        # Reading individual image for each cow
        low_light_mages, low_reso = 0, 0
        count_images = 0
        for cattle_image in cattle_images:
            count_images += 1
            image_path = os.path.join(OG_DATA, cattle, cattle_image)
            filename, extension = os.path.splitext(cattle_image)
            ENHANCE_FACTORS = [
                # brightness enhancement
                (0.2, os.path.join(AUG_LIGHTING_DATA, cattle, filename + "_bright_02" + extension)),
                (0.3, os.path.join(AUG_LIGHTING_DATA, cattle, filename + "_bright_03" + extension)),
                (0.4, os.path.join(AUG_LIGHTING_DATA, cattle, filename + "_bright_04" + extension)),

                # contrast enhancement
                (0.6, os.path.join(AUG_LIGHTING_DATA, cattle, filename + "_bright_06" + extension)),
                (0.7, os.path.join(AUG_LIGHTING_DATA, cattle, filename + "_bright_07" + extension)),
                (0.8, os.path.join(AUG_LIGHTING_DATA, cattle, filename + "_bright_08" + extension))
            ]
            # Reading to PIL image
            image = read_image_to_pil(image_path)

            # Running for lowering lighting
            low_light_mages += run_brightness_contrast_adjustment(image, ENHANCE_FACTORS, save_image=SAVE_IMAGE)
            SUMMARY_STATISTICS["Cattle"][cattle]["low_lighting_images"] = low_light_mages

            # Running for lowering resolution
            image = np.array(image)
            height, width, _ = image.shape
            height = height_width_checks(height)
            width = height_width_checks(width)

            # Running gaussian blur and averaging pixels
            low_reso = apply_gaussian_blur_and_subsampling(image, (width, height), save_image=SAVE_IMAGE,
                                                           save_path=os.path.join(AUG_RESOLUTION_DATA,
                                                                                  cattle,
                                                                                  filename + "_blur" + extension))

            # Running Gaussian noisy
            stddev_paths = [
                (50, os.path.join(AUG_RESOLUTION_DATA, cattle, filename + "_gauss_noisy_std50" + extension)),
                (30, os.path.join(AUG_RESOLUTION_DATA, cattle, filename + "_gauss_noisy_std30" + extension))
            ]
            low_reso += apply_gaussian_noise(image, save_image=SAVE_IMAGE, stddev_paths=stddev_paths)

            SUMMARY_STATISTICS["Cattle"][cattle]["low_resolution_images"] = low_reso
            # comment this line if you want to run for all images for a cattle
            # break

            #  comment this line of you want to run for all cattle
            if count_images == min_og_images:  # take only images for each cattle equal to min images for the cattle
                break

        del low_reso, low_light_mages  # release the memory
        # break

    SUMMARY_STATISTICS["max_cattle"] = {
        "cattle_name": max_cattle_name,
        "number_of_og_images": max_og_images
    }

    with open(os.path.join(os.path.dirname(os.getcwd()), "summary_images_statistics.json"), 'w+') as f:
        json.dump(SUMMARY_STATISTICS, f)
