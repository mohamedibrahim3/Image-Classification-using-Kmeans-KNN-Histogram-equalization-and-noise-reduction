# Image Classification

This is an image classification application that uses machine learning techniques to classify images. The application includes four different filters: 

- K-Means Clustering
- K-Nearest Neighbors (KNN)
- Histogram Equalization
- Noise Reduction

## Dependencies

* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html) (for the GUI)

## How to use

1. Install the dependencies by running `pip install -r requirements.txt`
2. Run the script with `python main.py`
3. Use the "Open" button to select an image file to classify. Supported file types include PNG, JPEG, and JPG.
4. Select one of the four filters from the "Filters" menu to apply to the image.
5. The filtered image will be displayed in the application.

## Features

- K-Means Clustering: This filter uses the K-Means Clustering algorithm to divide the image into a specified number of clusters.
- K-Nearest Neighbors (KNN): This filter uses the KNN algorithm to classify the image based on the features of its neighboring pixels.
- Histogram Equalization: This filter adjusts the contrast of the image by stretching the intensity values of the pixels.
- Noise Reduction: This filter uses a median filter to reduce noise in grayscale images.

## Notes

- The Noise Reduction filter is only available for grayscale images.
- The KNN filter may take a while to process on large images.
