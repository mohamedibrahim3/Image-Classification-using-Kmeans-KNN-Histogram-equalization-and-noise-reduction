import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import re

# Create a class to classify the image using K-means clustering
class KMeans:
    
    # Create a method to classify the image using K-means clustering
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

        # Apply K-means clustering to the pixels
        num_clusters = 6
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        
        _, labels, palette = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Convert the labels to 32-bit integers
        labels = np.uint8(labels)

        # Create array with colors corresponding the cluster label for each pixel in the image
        res = palette[labels.flatten()]

        # Reshaping the res array into the same shape as the original image
        clustered_image = res.reshape((image.shape))
        clustered_image = np.clip(clustered_image, 0, 255).astype(np.uint8)
        
        # Create a figure with two subplots
        fig, ax = plt.subplots(1, 2, facecolor='#242424')

        # Display the original image in the first subplot
        ax[0].imshow(image)
        ax[0].set_title('Original Image', color='white')
        ax[0].tick_params(colors='white')

        # store the output of the resulting image
        output = os.getcwd() + '/output'
        clustered_image = cv2.cvtColor(clustered_image, cv2.COLOR_BGR2RGB)
        cv2.imwrite(output + '/KMeans-img'+ number +'.png', clustered_image)

        # Display the mean color image in the second subplot
        clustered_image = cv2.cvtColor(clustered_image, cv2.COLOR_RGB2BGR)
        ax[1].imshow(clustered_image)
        ax[1].set_title('Clustered Image', color='white')
        ax[1].tick_params(colors='white')

        # Show the figure
        plt.show()