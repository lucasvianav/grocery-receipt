import cv2
import pytesseract

import utils

if __name__ == "__main__":
    original_img = cv2.imread("receipts/no-shadow.jpg", cv2.IMREAD_GRAYSCALE)

    # arbitrary_img = utils.binarize(original_img, 105)
    # scratch_otsu_img = utils.otsu(original_img)
    _, cv2_otsu_img = cv2.threshold(
        original_img,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    # adaptive_mean_img = cv2.adaptiveThreshold(
    #     original_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 2
    # )
    adaptive_gaussian_img = cv2.adaptiveThreshold(
        original_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2
    )
    blurred_adaptive_gaussian_img = cv2.medianBlur(adaptive_gaussian_img, 7)

    utils.plot(
        [
            {"title": "Original image", "image": original_img},
            # {
            #     "title": "Binary Image (arbitrary threshold = 105)",
            #     "image": arbitrary_img,
            # },
            # {"title": "Scratch Otsu", "image": scratch_otsu_img},
            {"title": "OpenCV Otsu", "image": cv2_otsu_img},
            # {"title": "OpenCV Adaptive Mean Thresholding", "image": adaptive_mean_img},
            {
                "title": "OpenCV Adaptive Gaussian Thresholding",
                "image": adaptive_gaussian_img,
            },
            {
                "title": "OpenCV Adaptive Gaussian Thresholding (blurred)",
                "image": blurred_adaptive_gaussian_img,
            },
        ],
        1,
        4,
        False,
    )

    print(pytesseract.image_to_string(cv2_otsu_img, lang="por"))
