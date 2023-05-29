import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

def search_for_output_path ():
    curredir = os.getcwd()
    tdir = filedialog.askdirectory(parent=root, initialdir=curredir, title='Please select a directory')
    if len(tdir) > 0:
        print ("You chose: %s" % tdir)
    return tdir

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(include_top=True, weights='imagenet')

# Function to tag an image and save the outputs to a text file
def tag_image(image_path, output_path):
    # Load and preprocess the image
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    # Run the image through the model
    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=10)[0]

######################################
    # Display the predictions
    #for _, label, probability in decoded_predictions:
    #    print(f"{label}: {probability:.2%}")

    # Display the image
    #    plt.imshow(img)
    #    plt.axis('off')
    #    plt.show()
#####################################

    # Save the predictions to a text file
    with open(output_path, 'w') as file:
        for _, label, probability in decoded_predictions:
            file.write(f"{label}: {probability:.2%}\n")

# Provide the path to the image you want to tag
image_path = search_for_file_path()
print ("\nfile_path_variable = ", image_path)
# Provide the path to the output text file
output_path = search_for_output_path()+"/output.txt"
print ("\nfile_path_variable = ", output_path)

tag_image(image_path, output_path)
