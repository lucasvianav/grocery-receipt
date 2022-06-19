import cv2
import imageio
from matplotlib import pyplot as plt

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

    plt.subplot(141)
    plt.axis("off")
    plt.title("Original image")
    plt.imshow(input_img, cmap="gray")
    plt.subplot(142)
    plt.axis("off")
    plt.title("Binary image (threshold = 105)")
    plt.imshow(img1, cmap="gray")
    plt.subplot(143)
    plt.axis("off")
    plt.title("Otsu")
    plt.imshow(img2, cmap="gray")
    plt.subplot(144)
    plt.axis("off")
    plt.title("CV2 Otsu")
    plt.imshow(img3, cmap="gray")
    plt.show()
