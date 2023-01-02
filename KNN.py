import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import re

# Create a class to classify the image using KNN algorithm
class KNN:
    
    # Create a method to classify the image using KNN algorithm
    def classify_image(image_path):
        
        # Load the image from the given path
        image = cv2.imread(image_path)

        # Get the number of the image
        match = re.search(r'\d+', image_path)
        number = match.group()
        
        # Convert the image to the RGB color space
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Flatten the image into a 1D array of pixels
        pixels = image.reshape((-1, 3))
        
        # Convert the pixels to float type
        pixels = np.float32(pixels)

        # Create a KNN classifier
        knn = cv2.ml.KNearest_create()

        # Train the classifier with the pixels
        knn.train(pixels, cv2.ml.ROW_SAMPLE, np.zeros((pixels.shape[0], 1), dtype=np.int32))

        # Find the KNN neighbors for each pixel
        num_neighbors = 4
        neighbors = knn.findNearest(pixels, num_neighbors)

        # Count the number of pixels in each cluster
        cluster_counts = np.bincount(np.int64(neighbors[1]).flatten())

        # Find the cluster with the most pixels
        dominant_cluster = np.argmax(cluster_counts)

        # Create a mask for the dominant cluster
        mask = neighbors[1].flatten() == dominant_cluster

        # Get the pixel values for the dominant cluster
        dominant_pixels = pixels[mask]

        # Calculate the mean color of the dominant cluster
        mean_color = np.mean(dominant_pixels, axis=0)

        # Create a figure with two subplots
        fig, ax = plt.subplots(1, 2, facecolor='#242424')

        # Display the original image in the first subplot
        ax[0].imshow(image)
        ax[0].set_title('Original Image', color='white')
        ax[0].tick_params(colors='white')

        # Create a solid color image with the mean color of the dominant cluster
        mean_color_image = np.full((50, 50, 3), mean_color, dtype=np.uint8)

        # store the output of the resulting image
        output = os.getcwd() + '/output'
        cv2.imwrite(output + '/KNN-img' + number + '.png', mean_color_image)

        # Display the mean color image in the second subplot
        ax[1].imshow(mean_color_image)
        ax[1].set_title('Mean Color of Dominant Cluster', color='white')
        ax[1].tick_params(colors='white')

        # Show the figure
        plt.show()