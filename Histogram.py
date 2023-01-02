import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import re


# Create a clase to equalize the histogram of the image
class Histogram:
    
    # Create a method to equalize the histogram of the image
    def histogram_equalization(image_path):
        # read image and convert it to gray scale image
        if "Gray" in image_path:
            src = cv2.imread(image_path)
            
            match = re.search(r'\d+', image_path)
            number = match.group()
            
            src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            
            dst = cv2.equalizeHist(src)
            
            # store the output of the equalized image
            output = os.getcwd() + '/output'
            cv2.imwrite(output + '/equalized-img-Gray'+ number +'.png', dst)
            
            # show the histogram of the source image
            srcHistogram = cv2.calcHist([src], [0], None, [256], [0, 256])

            # show the histogram of the equalized image
            dstHistogram = cv2.calcHist([dst], [0], None, [256], [0, 256])
            
            fig = plt.figure(figsize=(12, 9), facecolor='#242424')
            
            ax1 = fig.add_subplot(2, 2, 1)
            src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB) 
            ax1.imshow(src)
            ax1.set_title('Input Image', color='white')
            ax1.tick_params(axis='both', colors='white')
            
            ax2 = fig.add_subplot(2, 2, 2)
            dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
            ax2.imshow(dst)
            ax2.set_title('Equalized Image', color='white')
            ax2.tick_params(axis='both', colors='white')
            
            ax3 = fig.add_subplot(2, 2, 3)
            plt.plot(srcHistogram)
            ax3.set_title('histogram of the source image', color='white')
            ax3.tick_params(axis='both', colors='white')
            
            ax4 = fig.add_subplot(2, 2, 4)
            plt.plot(dstHistogram)
            ax4.set_title('histogram of the equalized image', color='white')
            ax4.tick_params(axis='both', colors='white')    
            
        else:
        
            # read image and convert it to gray scale image
            src = cv2.imread(image_path)
            
            # Get the number of the image
            match = re.search(r'\d+', image_path)
            number = match.group()
            
            # split the image into its channels
            b, g, r = cv2.split(src)
            
            # Apply histogram equalization to each channel
            equ_b = cv2.equalizeHist(b)
            equ_g = cv2.equalizeHist(g)
            equ_r = cv2.equalizeHist(r)
            # Merge the equalized channels back into a single image
            dst = cv2.merge((equ_b, equ_g, equ_r))
            
            # show the histogram of the source image
            srcRhistogram = cv2.calcHist([r], [0], None, [256], [0, 256])
            srcGhistogram = cv2.calcHist([g], [0], None, [256], [0, 256])
            srcBhistogram = cv2.calcHist([b], [0], None, [256], [0, 256])
            
            # show the histogram of the equalized image
            dstRhistogram = cv2.calcHist([equ_r], [0], None, [256], [0, 256])
            dstGhistogram = cv2.calcHist([equ_g], [0], None, [256], [0, 256])
            dstBhistogram = cv2.calcHist([equ_b], [0], None, [256], [0, 256])
            
            # Create a figure to show the results
            fig = plt.figure(figsize=(12, 9), facecolor='#242424')
            
            # store the output of the equalized image
            output = os.getcwd() + '/output'
            cv2.imwrite(output + '/equalized-img'+ number +'.png', dst)
            
            # show the histogram of the source image
            ax1 = fig.add_subplot(2, 4, 1)
            src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
            ax1.imshow(src)
            ax1.set_title('Input Image', color='white')
            ax1.tick_params(axis='both', colors='white')
            
            # show the histogram of the equalized image
            ax2 = fig.add_subplot(2, 4, 3)
            dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
            ax2.imshow(dst)
            ax2.set_title('Equalized Image', color='white')
            ax2.tick_params(axis='both', colors='white')
            
            # show the histogram of the source image
            ax3 = fig.add_subplot(2, 4, 5)
            plt.plot(srcRhistogram, color="red")
            plt.plot(srcGhistogram, color="green")
            plt.plot(srcBhistogram, color="blue")
            ax3.set_title('histogram of the source image', color='white')
            ax3.tick_params(axis='both', colors='white')
            
            # show the histogram of the red equalized image
            ax4 = fig.add_subplot(2, 4, 6)
            plt.plot(dstRhistogram, color='red')
            ax4.set_title('Red Histogram', color='white')
            ax4.tick_params(axis='both', colors='white')
            
            # show the histogram of the green equalized image
            ax5 = fig.add_subplot(2, 4, 7)
            plt.plot(dstGhistogram, color='green')
            ax5.set_title('Green Histogram', color='white')
            ax5.tick_params(axis='both', colors='white')
            
            # show the histogram of the blue equalized image
            ax6 = fig.add_subplot(2, 4, 8)
            plt.plot(dstBhistogram, color='blue')
            ax6.set_title('Blue Histogram', color='white')
            ax6.tick_params(axis='both', colors='white')
            
        plt.show()