# Setup

A quick and simple guide of how to setup and run the project.

## Dependencies

- Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Install [OpenCV](https://opencv.org/releases/)
- `pip install -r requirements.txt`
- Copy the trained model [grocery.traineddata](../ocr-training/grocery.traineddata) to your `tessdata` directory (in ArchLinux, it's `/usr/share/tessdata`)
- Copy `por.traineddata` and `eng.traineddata` from [tesseract-ocr/tessdata_best](https://github.com/tesseract-ocr/tessdata_best) to your `tessdata` directory

## Running

You can run the project either by `make` or `python src/main.py`.

You'll then be asked to name a grocery receipt photo. If you wish, you can use ours, in [receipts/cropped](../receipts/cropped).
