def merge_files(output_file, input_dir, base_filename):
    """
    Merges all file parts into a single file.

    :param output_file: Path to save the merged file.
    :param input_dir: Directory containing the file parts.
    :param base_filename: Base name of the split files.
    """
    import os
    import glob

    # Find all part files and sort them
    part_files = sorted(glob.glob(os.path.join(input_dir, f"{base_filename}.part*")))

    if not part_files:
        print("No part files found!")
        return

    print(f"Found {len(part_files)} parts. Merging into: {output_file}")

    # Merge parts into the final file
    with open(output_file, "wb") as merged_file:
        for part in part_files:
            print(f"Merging: {part}")
            with open(part, "rb") as part_file:
                merged_file.write(part_file.read())

    print(f"File merged successfully into: {output_file}")


# Usage
input_directory = "./split_files"  # Directory with the split files
merged_output_file = "models--ds4sd--docling-models_merged.zip"  # Name of the merged file
base_file_name = "models--ds4sd--docling-models.zip"  # Base name of the original file

merge_files(merged_output_file, input_directory, base_file_name)
