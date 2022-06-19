# Report

## Summary

- [Goal](#goal)
- [Initial Development](#initial-development)
- [Input Images](#input-images)

## <a id="goal"></a> Goal

The project's main goal is to provide convenient and fast means for someone to split grocery purchases between a group of people. Basically a [Splitwise](http://www.splitwise.com/)-like software that extracts the products' data from the grocery receipts' photos and works in batch.

## <a id="initial-development"></a> Initial Development

Our first action was to try and apply different methods of image segmentation and compare results, based on which we'll be able to determine what kinds of image enchanement and/or restoration are necessary to make the photos more readable.

We initially tried using a static thresholding/binarization method with an arbitrary threshold of `105` but soon resorted to trying adaptive methods. We then tried applying the Otsu Thresholding method provided in class (implemented from scratch), but but had some unexpected errors with it, as well as a not so great binary image in which the receipt's data isn't readable.

The next step was to add OpenCV as a dependency and try some of it's methods:

1. Otsu Thresholding (Global)
2. Adaptive Mean Thresholding (Regional)
3. Adaptive Gaussian Thresholding (Regional)

These methods outputted the best results, specially Otsu and Adaptive Gaussian, so we'll focus the development on them.

We also tried comparing the results between photos with a shadow over the receipt and some without it and found that while the Adaptive Gaussian Thresholding provided very similar results (very readable image) for both types of photos, the Otsu Thresholding got the best result for the photo with the evenly lit receipt, but in the other one it incorrectly blacked out the darker section of the receipt. The comparison can be seen in the [input images section](#input-images).

The next step is to try and find some method of making the Otsu Thresholding satisfactory for the shadowy photo (considering it produces the cleanest binary image) - otherwise, we'd have to focus on the Adaptive Guassian Thresholding. We're planning on either applying some sort of image enhancement filter (either contrast or brightness manipulation) or edge-detection algorithm in order to cut the whole receipt out of the picture before applying the binarization.

## <a id="input-images"></a> Input Images

All of the input images are [grocery receipt photos](../receipts) taken by the students in this group. Based on the professor's feedback, we initially intend to work with simple and clean images (with no shadow or distortions) in order to segment the background and highlighting the text.

### Without shadow

![](../.github/images/no-shadow-comparison.png)

### With shadow

![](../.github/images/shadow-comparison.png)
