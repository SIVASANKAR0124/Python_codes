import os

# Directory containing the files
directory = 'C:\\Users\\sivas\\OneDrive\\Desktop\\Day_data'
new_file = 1
# Iterate through each file in the directory
for filename in os.listdir(directory):
    # Specify the current and new file names
    current_name = os.path.join(directory, filename)
    new_name = os.path.join(directory, 'DAY_IMAGE_' + str(new_file)+".jpg")  # Add prefix 'DAY_IMAGE_' to each file
    new_file += 1  # Corrected incrementing

    # Rename the file
    os.rename(current_name, new_name)

