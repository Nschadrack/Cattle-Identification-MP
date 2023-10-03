"""
This module contains functions for helping to implement some tasks
in the dataset
"""
import cv2
from PIL import Image


def read_image_to_pil(image_path):
    """
    this functions reads the image from a path
    :param image_path: the path to the image to read
    :return: PIL image
    """
    return Image.open(image_path)


def read_image_to_cv2(image_path):
    """
        this functions reads the image from a path
        :param image_path: the path to the image to read
        :return: CV2 image
    """
    return cv2.imread(image_path)


def height_width_checks(value):
    if value > 1000:
        value *= 40 / 100
    elif value >= 400:
        value *= 60 / 100

    return int(value)
