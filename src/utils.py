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
