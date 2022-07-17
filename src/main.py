import cv2
import pytesseract
from numpy.typing import NDArray

from receipt import Receipt
from utils import clean, image_exists, prompt

if __name__ == "__main__":
    image_filepath = prompt(
        "What is the path (relative or absolute) to the grocery receipt photo?",
        image_exists,
        "The filepath must be of a PNG or JPG image and the file must exist.",
    )
    original_img: NDArray = cv2.imread(image_filepath, cv2.IMREAD_GRAYSCALE)

    # apply otsu binarization to the pre-processed image
    otsu_img: NDArray
    _, otsu_img = cv2.threshold(
        clean(original_img),
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    # apply morphological opening in order to close gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    otsu_img = cv2.morphologyEx(otsu_img, cv2.MORPH_OPEN, kernel)

    # apply OCR and print output
    text: str = pytesseract.image_to_string(
        otsu_img, lang="por+grocery+eng", config="--oem 1 --psm 1"
    )
    try:
        print(Receipt(text))
    except RuntimeError as err:
        print(err)
