import numpy as np
from matplotlib import pyplot as plt
from numpy.typing import NDArray


def norm(img: NDArray[np.number], new_max: float) -> NDArray[np.number]:
    """
    Normalize a matrix.

    Parameters
    ----------
    img (NDArray[np.number]): the image to be normalized
    new_max (float): the largest value in the normalized image

    Returns
    -------
    NDArray[np.number]: the normalized matrix
    """
    max_matrix = np.max(img)
    min_matrix = np.min(img)

    # in case all elements are the same
    # (prevents dividing by zero)
    if min_matrix == max_matrix:
        img[:, :] = new_max
        return img

    # normalize the image so that min becomes 0 and max becomes `new_largest`
    return ((img - min_matrix) / (max_matrix - min_matrix)) * new_max


def grayscale(img: NDArray) -> NDArray[np.number]:
    """
    Convert a RGB image to grayscale, considering color sensors of the eye are
    divided in red cones (65%), green cones (33%) and blue cones (2%).

    Parameters
    ----------
    img (NDArray): the image to be normalized

    Returns
    -------
    NDArray[np.number]: the grayscale image
    """
    grayscale_transform = [0.65, 0.33, 0.02]
    return img.dot(grayscale_transform)


def binarize(img: NDArray[np.number], threshold: int | np.number) -> NDArray[np.number]:
    """
    Convert an image to binary - all pixels with value below a threshold are black (0) and all above it are white (1).

    Parameters
    ----------
    img (NDArray): the image to be converted to binary.

    Returns
    -------
    NDArray[np.number]: the binary image
    """
    binary_image = np.ones(img.shape).astype(np.uint8)
    binary_image[img < threshold] = 0
    return binary_image


def otsu(img: NDArray[np.number]) -> NDArray[np.number]:
    n_pixels = np.product(img.shape)
    variances = []
    histogram, _ = np.histogram(img, bins=256, range=(0, 256))

    for threshold in range(1, 255):
        bin_img_i = binarize(img, threshold)

        # weights
        weight_black = np.sum(histogram[:threshold]) / n_pixels
        weight_white = np.sum(histogram[threshold:]) / n_pixels

        # variances
        var_black = np.var(img[bin_img_i == 0])
        var_white = np.var(img[bin_img_i == 1])

        if not np.isnan((var := weight_black * var_black + weight_white * var_white)):
            variances.append(var)

    return binarize(img, np.argmin(variances))


