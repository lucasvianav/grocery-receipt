import cv2
import pytesseract
from numpy.typing import NDArray

import utils

if __name__ == "__main__":
    original_img: NDArray = cv2.imread("receipts/cropped/cropped.jpg", cv2.IMREAD_GRAYSCALE)

    # apply otsu binarization to the pre-processed image
    otsu_img: NDArray
    _, otsu_img = cv2.threshold(
        utils.clean(original_img),
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    # apply morphological opening in order to close gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    otsu_img = cv2.morphologyEx(otsu_img, cv2.MORPH_OPEN, kernel)

    utils.plot(
        [
            {"title": "Original image", "image": original_img},
            {"title": "Otsu", "image": otsu_img},
        ],
        1,
        2,
        False,
    )

    print(pytesseract.image_to_string(otsu_img, lang="por", config="--oem 2 --psm 3"))
