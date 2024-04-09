# Import the os module for interacting with the operating system
import os

# Define a function to get user inputs for file name, suffix, max number, and min size
def menu():
    a = input('Type file name (ENTER to skip)<< ')
    b = input('Type file suffix (ENTER to skip)<< ')
    c = input('Type file max number (ENTER to skip)<< ')
    d = input('Type file min size (ENTER to skip)<< ')
    # Convert the max number and min size inputs to integers and return all inputs
    return a, b, int(c), int(d)

# Call the menu function and unpack its return values into four variables
file_name, file_suffix, file_max_number, file_min_size = menu()

# Initialize a dictionary to store file metadata
file_metadata = {}
# Initialize a counter for the number of files processed
file_cnt = 0
# Use os.walk to iterate over all files in the current directory and its subdirectories
for root, directories, files in os.walk('.'):
    for _file in files:
        # If the maximum number of files has been processed, break the loop
        if file_cnt >= file_max_number: break
        # Construct the full path of the file
        full_path = os.path.join(root, _file)
        # Get the size of the file
        size = os.path.getsize(full_path)
        # If the file size is greater than the minimum size, and the file name and suffix match the user's inputs, add the file to the metadata dictionary
        if (size > file_min_size) and (_file.startswith(file_name)) and (_file.rstrip().endswith(file_suffix)): 
            file_metadata[full_path] = size
        # Increment the file counter
        file_cnt += 1
# Print the file metadata dictionary, sorted by file size in descending order
print(dict(sorted(file_metadata.items(), key=lambda item: item[1], reverse=True)))
