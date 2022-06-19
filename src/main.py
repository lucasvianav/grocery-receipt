import cv2

import utils

if __name__ == "__main__":
    input_img = cv2.imread("receipts/no-shadow.jpg", cv2.IMREAD_GRAYSCALE)

    img1 = utils.binarize(input_img, 105)
    img2 = utils.otsu(input_img)
    _, img3 = cv2.threshold(
        input_img,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    img4 = cv2.adaptiveThreshold(
        input_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 2
    )
    img5 = cv2.adaptiveThreshold(
        input_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2
    )

    utils.plot(
        [
            {"title": "Original image", "image": input_img},
            {"title": "Binary Image (arbitrary threshold = 105)", "image": img1},
            {"title": "Scratch Otsu", "image": img2},
            {"title": "OpenCV Otsu", "image": img3},
            {"title": "OpenCV Adaptive Mean Thresholding", "image": img4},
            {"title": "OpenCV Adaptive Gaussian Thresholding", "image": img5},
        ],
        1,
        6,
        False,
    )
