import cv2
import imageio

import utils

if __name__ == "__main__":
    input_img = utils.grayscale(imageio.imread("receipts/camera_capture1.jpg"))

    img1 = utils.binarize(input_img, 105)
    img2 = utils.otsu(input_img)
    _, img3 = cv2.threshold(
        cv2.imread("receipts/camera_capture1.jpg", cv2.IMREAD_GRAYSCALE),
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    utils.plot(
        [
            {"title": "Original image", "image": input_img},
            {"title": "Binary Image (arbitrary threshold = 105)", "image": img1},
            {"title": "Scratch Otsu", "image": img2},
            {"title": "OpenCV Otsu", "image": img3},
        ],
        1,
        4,
        False,
    )
