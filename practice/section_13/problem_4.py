def read_large_file(file_path):
    """
    Generator function to read a large file line by line.

    Parameters:
        file_path (str): Path to the file to be read.
    Yields:
        str: The next line from the file.
    """
    with open(file_path, "r") as file:
        for line in file:
            yield line


# Example usage:
for line in read_large_file("large.txt"):
    print(line)
