import random
from PIL import Image

def generate_pattern_images(image_files):
    # shuffle the image files
    random.shuffle(image_files)
    
    # create a list to hold the pattern images
    pattern_images = []
    
    # generate the pattern images using the shuffled image files
    for i in range(len(image_files)):
        # load the image file
        img = Image.open(image_files[i])
        
        # add the image to the pattern image list
        pattern_images.append(img)
        
    # return the pattern images
    return pattern_images

def authenticate_user(pattern_images):
    # show the pattern images to the user
    for img in pattern_images:
        img.show()
        
    # get the user's input pattern
    user_pattern = input("Enter the pattern (in order): ")
    
    # check if the user's input matches the original pattern
    if user_pattern == " ".join([img.filename for img in pattern_images]):
        print("Authentication successful!")
    else:
        print("Authentication failed.")

# specify the image files to use for the pattern
image_files = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN", "NFLX"]

# generate the pattern images
pattern_images = generate_pattern_images(image_files)

# authenticate the user
authenticate_user(pattern_images)
