import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import re

# Create a class to reduce noise from the image
class ReduceNoise:
    
    # Create a method to reduce noise from the image
    def reduce(image_path):
        
        # Load the image from the given path
        input_image = cv2.imread(image_path)
        
        # Get the number of the image
        match = re.search(r'\d+', image_path)
        number = match.group()
        
        # Convert the image to the grayscale color space
        image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

        # Apply median blur to the image
        image = cv2.medianBlur(image, 5)

        # store the output of the resulting image
        output = os.getcwd() + '/output'
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(output + '/noiseReduced-img'+ number +'.png', image)

        # Create a figure with two subplots
        fig, ax = plt.subplots(1, 2, facecolor='#242424')
        
        # Display the original image in the first subplot
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
        ax[0].imshow(input_image)
        ax[0].set_title('Original Image', color='white')
        ax[0].tick_params(colors='white')

        # Display the noise-reduced image in the second subplot
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax[1].imshow(image)
        ax[1].set_title('Noise Reduced Image', color='white')
        ax[1].tick_params(colors='white')

        # Show the figure
        plt.show()