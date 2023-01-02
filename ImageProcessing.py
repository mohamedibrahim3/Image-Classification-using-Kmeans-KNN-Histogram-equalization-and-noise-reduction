from tkinter.font import BOLD               # import the functions from the other files
from matplotlib.colors import cnames        #  import the functions from the other files
import os                                   # import the functions from the other files
from tkinter import *                       # import the functions from the other files
from tkinter import filedialog              # import the functions from the other files
from tkinter import messagebox              # import the functions from the other files
from numpy.lib.type_check import imag       # import the functions from the other files
from Histogram import*                      # import the functions from the other files
from KMeans import *                        # import the functions from the other files
from KNN import *                           # import the functions from the other files
from ReduceNoise import *                   # import the functions from the other files
import tkinter as tk                        # for the GUI
from tkinter import ttk                     # for the style of the button
import customtkinter                        # for the GUI
from PIL import Image, ImageTk              # for displaying the image

# Set the appearance mode to dark and the default color theme to blue
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Global variables
photoChosen = 0
isGray = 0

# GUI using tkinter libirary
# start of the GUI main loop
root = customtkinter.CTk()

# Create a style for the button
style = ttk.Style(root)

# Create the button using the "My.TButton" style
root.title('Image Processing')
root.resizable(width=False, height=False)
root.geometry("650 * 500")

# Functions
# function to open an image from a dirctory
def open():
    localDir = os.getcwd() + '/images'
    root.filename = filedialog.askopenfilename(initialdir=localDir, title="Select A File", filetypes=(
        ("png files", "*.png"), ("jpeg files", "*.jpeg"), ("jpg files", "*.jpg")))
    if root.filename:  # if a photo was selected
        enableFilterButtons()  # enable the filter buttons   
        refresh()
        
        if "Gray" in root.filename:
            global isGray
            isGray = 1
            enableReduceNoiseButton(isGray)
        else:
            isGray = 0
            enableReduceNoiseButton(isGray)
        
        image = Image.open(root.filename)  # open the image
    
        createImageLabel(image)  # create a label to display the image

# function to refresh the frames
def refresh():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack(pady=30, padx=30)
    frame2.pack()
    frame3.pack(pady=30, padx=30)

# function to enable the filter buttons
def enableFilterButtons():
    openButton.configure(text="Change photo")  # change the text of the open button 
    KNNButton.configure(state="normal")  # enable the KNN filter button
    KMeansButton.configure(state="normal")  # enable the KMeans filter button
    HistogramButton.configure(state="normal")  # enable the Histogram filter button
        
def enableReduceNoiseButton(gray):
    if gray:
        ReduceNoiseButton.configure(state="normal")  # enable the ReduceNoise filter button
    else:
        ReduceNoiseButton.configure(state="disabled")  # disable the ReduceNoise filter button
 
# function to create a label to display the image
def createImageLabel(image):
    image = image.resize((200, 200))  # resize the image
    image = ImageTk.PhotoImage(image)  # convert the image to PhotoImage
    imageLabel = Label(frame2, image=image)  # create a label to display the image
    imageLabel.image = image  # keep a reference to the image to prevent garbage collection
    imageLabel.grid(row=0, column=0, columnspan=5)  # add the label to the interface
 
# function to run the KNN filter
def runKNN():
    KNN.classify_image(root.filename)

# function to run the ReduceNoise filter
def runReduceNoise():
    ReduceNoise.reduce(root.filename)

# function to run the KMeans filter
def runKMeans():
    KMeans.classify_image(root.filename)

# function to run the Histogram filter
def runHistoGramFilter():
    Histogram.histogram_equalization(root.filename)

# Frames
# Create a frame for select a photo
frame1 = customtkinter.CTkFrame(root)
frame1.pack(pady=30, padx=30)

# Create a frame for display the photo
frame2 = customtkinter.CTkFrame(root)
frame2.pack_forget()

# Create a frame for select a filter
frame3 = customtkinter.CTkFrame(root)
frame3.pack(pady=30, padx=30)

# Labels
# Select a photo label
photoSelect = customtkinter.CTkLabel(frame1, text="Please Select a photo to apply the filters to it.", font=("Helvetica", 24))
photoSelect.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

# Select a filter label
filterSelect = customtkinter.CTkLabel(frame3, text="Apply the filter you want from the buttons below.", font=("Helvetica", 24))
filterSelect.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

# Buttons
# Open the image from the directory button
openButton = customtkinter.CTkButton(frame1, text="Open File", command=open, font=("Helvetica", 16), width=200, height=40)
openButton.grid(row=1, column=2, padx=10, pady=10)

# Apply the KNN filter to the image button
KNNButton = customtkinter.CTkButton(frame3, text="KNN Classification", command=runKNN, font=("Helvetica", 16), width=200, height=40, state="disabled")
KNNButton.grid(row=1, column=3)

# Apply the KMeans filter to the image button
KMeansButton = customtkinter.CTkButton(frame3, text="K-Means Classification", command=runKMeans, font=("Helvetica", 16), width=200, height=40, state="disabled")
KMeansButton.grid(row=1, column=1, padx=10, pady=10)

# Apply the Reduce Noise filter to the image button
ReduceNoiseButton = customtkinter.CTkButton(frame3, text="Noise Reduction", command=runReduceNoise, font=("Helvetica", 16), width=200, height=40, state="disabled")
ReduceNoiseButton.grid(row=3, column=1, padx=10, pady=10)

# Apply the Histogram filter to the image button
HistogramButton = customtkinter.CTkButton(frame3, text="Histogram Equalization", command=runHistoGramFilter, font=("Helvetica", 16), width=200, height=40, state="disabled")
HistogramButton.grid(row=3, column=3, padx=10, pady=10)

# Run the GUI main loop
root.mainloop()
# End of the GUI main loop