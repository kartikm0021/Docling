import os

def split_file(file_path, output_dir, chunk_size=20 * 1024 * 1024):
    """
    Splits a file into smaller parts of given size.

    :param file_path: Path to the input file to be split.
    :param output_dir: Directory where the chunks will be saved.
    :param chunk_size: Size of each chunk in bytes (default 20 MB).
    """
    

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get base filename
    base_filename = os.path.basename(file_path)

    # Start splitting
    part_num = 1
    with open(file_path, "rb") as input_file:
        while chunk := input_file.read(chunk_size):
            chunk_filename = os.path.join(output_dir, f"{base_filename}.part{part_num:03}")
            with open(chunk_filename, "wb") as chunk_file:
                chunk_file.write(chunk)
            print(f"Created: {chunk_filename}")
            part_num += 1

    print("File splitting completed!")


# Usage
file_to_split = "models--ds4sd--docling-models.zip"  # Path to the file you want to split
output_directory = "./split_files"  # Directory to store the split files
split_file(file_to_split, output_directory)
