import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageTransform, ImageEnhance


def show_or_save_pil_image(pil_image, save_image=False, save_path=None):
    if save_image:
        if save_path is not None:
            path, filename = os.path.split(save_path)
            os.makedirs(path, exist_ok=True)  # Create directory if does not exist
            pil_image.save(save_path)
        else:
            raise ValueError("Save_path cannot be None if save_image is true, or check if path is correct!")
    else:
        pil_image.show()


def apply_brightness_and_contrast_adjustment(pil_image, enhance_factor, save_image=False, save_path=None):
    """
    This function that decreases the brightness and contrast of an image
    to make it appear dimmer and lower in quality.

    :param pil_image: the PIL image to modify
    :param save_image: parameter which shows whether to save image or not
    :param enhance_factor: factoring changing the contrast and brightness of image
    :param save_path: the path where to save the image if save_image is true
    :return: None
    """
    enhancer = ImageEnhance.Brightness(pil_image)
    img_low_light = enhancer.enhance(enhance_factor)  # Adjust the enhancement factor as needed

    show_or_save_pil_image(img_low_light, save_image=save_image, save_path=save_path)


def run_brightness_contrast_adjustment(image, enhance_factors_names, save_image=False):
    count_images = 0
    for factor, save_image_path in enhance_factors_names:
        print(f"Saving image at {save_image_path}")
        apply_brightness_and_contrast_adjustment(image, enhance_factor=factor, save_image=save_image,
                                                 save_path=save_image_path)  # brightness enhancement
        count_images += 1
    return count_images


def apply_gaussian_blur_and_subsampling(cv2_image, desired_size, save_image=False, save_path=None):
    """
        Function  which applies box sampling by averaging pixels and gaussian blur
        :param cv2_image: the image read using cv2 -> numpy array
        :param desired_size: the target image size
        :param save_image: whether to save or display
        :param save_path: path where to save image
        :return: number of images generated
    """
    # Resize using pixel averaging (Box Sampling)
    resized_image = cv2.resize(cv2_image, desired_size, interpolation=cv2.INTER_AREA)

    # Apply Gaussian blur and then resize
    blurred_image = cv2.GaussianBlur(resized_image, (0, 0), sigmaX=5)
    resized_image = cv2.resize(blurred_image, desired_size, interpolation=cv2.INTER_LINEAR)

    # Show or save image
    show_or_save_pil_image(Image.fromarray(resized_image), save_image=save_image, save_path=save_path)

    return 1


def apply_gaussian_noise(numpy_image, stddev_paths, mean=0, save_image=False):
    """
    Function for applying gaussian noisy to the image
    :param numpy_image: ndarray for image
    :param stddev_paths: std deviation with image path
    :param mean: the mean which is always zero but feel free to experiment
    :param save_image: flag to indicate whether to save or display image
    :return: number of images generated
    """

    # Generate Gaussian noise with the same shape as the image
    count_images = 0
    for stddev, image_path in stddev_paths:
        gaussian_noise = np.random.normal(mean, stddev, numpy_image.shape).astype(np.uint8)

        # Add the noise to the image
        noisy_image = np.clip(numpy_image + gaussian_noise, 0, 255).astype(np.uint8)

        # Convert the noisy NumPy array back to a PIL image
        noisy_image = Image.fromarray(noisy_image)
        count_images += 1
        # Save or display the noisy image
        show_or_save_pil_image(noisy_image, save_image=save_image, save_path=image_path)

    return count_images

