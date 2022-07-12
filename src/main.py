import re

import cv2
import pytesseract
from numpy.typing import NDArray

import utils

if __name__ == "__main__":
    original_img: NDArray = cv2.imread(
        "receipts/cropped/cropped.jpg", cv2.IMREAD_GRAYSCALE
    )

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

    # utils.plot(
    #     [
    #         {"title": "Original image", "image": original_img},
    #         {"title": "Otsu", "image": otsu_img},
    #     ],
    #     1,
    #     2,
    #     False,
    # )

    text: str = pytesseract.image_to_string(
        otsu_img, lang="por", config="--oem 2 --psm 3"
    )
    items_indexes = re.findall(r"^\d{3}\s{1,}", text, re.IGNORECASE + re.MULTILINE)
    total = re.findall(
        r"^Total\s*R\$\s*(\d{1,},\d{2}).*$", text, re.IGNORECASE + re.MULTILINE
    )[0]
    start, _ = re.search(
        r"^Total\s*R\$\s*(\d{1,},\d{2}).*$", text, re.IGNORECASE + re.MULTILINE
    ).span()

    arr = text[:start]
    for i in items_indexes:
        arr = arr.replace(i, "#########")
    arr = arr.split("#########")
    arr = arr[1:-1]
    for i in range(len(arr)):
        arr[i] = re.sub(r"^[\w\d]*\s*", "", arr[i].strip().replace("\n", " "))

    print(f"Number of items: {len(items_indexes)}")
    for i, item in enumerate(arr):
        print(f"Item {i}: {item}")
    print(f"Total value: R${total}")
