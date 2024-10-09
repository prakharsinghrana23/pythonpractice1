# print twinkle twinkle little star poem 
print('''Twinkle, twinkle, little star 
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

#''' is used for printing multiple lines in python 

# 2 use repel and print the table of 5 using it 
print (" done in CMD ")

# 3 install an exxternal module and use it to perform an operation of your interest 
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Prakhar Singh Rana I am here for you tell me what work you want to give me ")
engine.runAndWait()

#4 Write a python program to print the contents of a directory using the OS module . search online for the function which does that 
# by chat GPT because in this era we have to know how to use the AI 
import os

def print_directory_contents(directory):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(directory)
        
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the directory you want to check
directory_path = ("/")
print_directory_contents(directory_path)

#5 Label the program written in promblem 4 with comments 
import os  # Import the os module to interact with the operating system

def list_directory_contents(directory):
    """Function to list the contents of a specified directory."""
    try:
        # Get the list of all files and directories in the specified directory
        contents = os.listdir(directory)
        
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            # Print each item in the directory
            print(item)
    except FileNotFoundError:
        # Handle the case where the directory does not exist
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        # Handle the case where permission is denied
        print(f"You do not have permission to access the directory '{directory}'.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

# Prompt the user to enter the directory path they want to list
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)  # Call the function to list the contents

