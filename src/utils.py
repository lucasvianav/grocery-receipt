from os.path import exists
from typing import Callable

import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.typing import NDArray


def plot(
    imgs: list[dict[str, NDArray | str]], n_rows: int, n_cols: int, axis=True
) -> None:
    """
    Plot a list of images using MatPlotLib.

    Parameters
    ----------
    imgs: images to be plotted
    n_rows: number of rows in the grid
    n_cols: number of columns in the grid
    axis: should the axis be shown in the subplots
    """
    actual_n_rows = len(imgs) // n_cols
    n_cols_last_row = len(imgs) - (actual_n_rows - 1) * n_cols

    for i in range(1, actual_n_rows + 1):
        for j in range(1, n_cols_last_row + 1):
            img = imgs[(index := (i - 1) * n_cols + j) - 1]
            plt.subplot(int(f"{n_rows}{n_cols}{index}"))
            plt.axis("on" if axis else "off")
            plt.title(img["title"])
            plt.imshow(img["image"], cmap=img["cmap"] if "cmap" in img else "gray")

    plt.show()


def clean(img: NDArray) -> NDArray:
    """
    Apply a cleaning (image procesing) pipeline to an image. The pipeline's core
    consists in morphological dilation and image subtraction.

    Parameters
    ----------
    img: the image to be processed

    Returns
    -------
    The processed image
    """
    # remove text using dilatation and median blur - this
    # leaves only the background (including noise and shadows)
    dilated_img = cv2.dilate(img, np.ones((7, 7)))
    background_img = cv2.medianBlur(dilated_img, 21)

    # subtract the background + noise + shadow from
    # the original image - this leaves only the text
    foreground_img = 255 - cv2.absdiff(img, background_img)

    # normalize the image
    normalized_img = foreground_img
    cv2.normalize(
        normalized_img,
        normalized_img,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
    )

    # truncate image and normalize again
    _, truncated_img = cv2.threshold(normalized_img, 230, 0, cv2.THRESH_TRUNC)
    cv2.normalize(
        truncated_img,
        truncated_img,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
    )

    return truncated_img


def parse_float(number: str) -> float:
    """Parse a comma-separated decimal number to a float rounded to 2 decimal places."""
    return round(float(number.replace(",", ".")), 2)


def get_n_leading_zeros(length: int) -> int:
    """
    Calculate the necessary number of leading zeros to consistently enumerate all elements in a list of given length.

    Parameters
    ----------
    length: how many elements there are in the list to be enumerated

    Returns
    -------
    Number of leading zeros necessary.
    """
    return len(str(length))


def image_exists(filepath: str) -> bool:
    """Check if a filepath refers to a PNG or JPG file that exists."""
    return (filepath.endswith(".png") or filepath.endswith(".jpg")) and exists(filepath)


def prompt(
    text: str,
    validate: Callable | None = None,
    err: str = "Invalid input, try again.",
) -> str:
    """
    Prompt user for input and only return when the input is valid.

    Parameters
    ----------
    text: input prompt.
    validate?: validator for the input - if none is provided, all input is considered valid.
               It should receive a string to validate as parameter and return a bool.
    err error message in case validation fails. Defaults to: "Invalid input, try again."

    Returns
    -------
    The user's validated input.
    """
    if not text.endswith("\n"):
        text += " "
    r = input(text)
    if validate:
        is_valid = validate(r)
        while not is_valid:
            r = input(f"\n{err} {text}")
            is_valid = validate(r)
    return r
