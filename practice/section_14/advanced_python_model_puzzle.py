import re
import os
from typing import Dict, List


def find_all_txt_files_in_folder(folder_to_search: str) -> Dict[str, List[str]]:
    """
    Finds all .txt files within subfolders of the specified directory.
    Param:
        folder_to_search (str) – Path to the main folder to search in.
    Returns:
        Dict[str, List[str]] – Dictionary where the key is the subfolder name and
        the value is a list of paths to .txt files.
    """
    search_folder = rf"{folder_to_search}"
    text_files_by_folder: Dict[str, List[str]] = {}

    for foldername, subfolders, filenames in os.walk(search_folder):
        txt_files = [
            os.path.join(foldername, f) for f in filenames if f.endswith(".txt")
        ]
        if txt_files:
            folder_key = os.path.basename(foldername)
            text_files_by_folder[folder_key] = txt_files

    return text_files_by_folder


def search_word_in_text_file(word: str, txt_file: str) -> bool:
    """
    Checks if a specific word exists in a text file
    Param:
        word (str) – The word to search for.
        txt_file (str) – Path to the .txt file.
    Returns:
        bool – True if the word is found, False otherwise.
    """
    with open(txt_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if word.lower() in line.lower():
                return True
    return False


def search_phone_number_in_text_file(txt_file: str) -> List[str]:
    """
    Extracts phone numbers from a text file. Matches formats like 123-456-7890, etc
    Param:
        txt_file (str) – Path to the .txt file.
    Returns:
        List[str] – List of found phone numbers.
    """
    phone_pattern = r"\(?\d{3}\)?[-.\s]+\d{3}[-.\s]+\d{4}"
    phone_numbers: List[str] = []

    with open(txt_file, "r", encoding="utf-8") as file:
        content = file.read()
        matches = re.findall(phone_pattern, content)
        if matches:
            phone_numbers.extend(matches)

    return phone_numbers


def program() -> None:
    """
    Main program that searches for .txt files and extracts phone numbers from them
    Returns:
        None
    """
    folder_to_search_path = r"C:\Users\miros\Desktop\extracted_content"
    dict_with_folders_and_files = find_all_txt_files_in_folder(folder_to_search_path)

    for folder, txt_files in dict_with_folders_and_files.items():
        for txt_file in txt_files:
            phone_numbers = search_phone_number_in_text_file(txt_file)
            if phone_numbers:
                print(
                    f"--- Found phone numbers: {', '.join(phone_numbers)} "
                    f"in Folder: {folder} -> File: {txt_file}"
                )
            # else:
            #     print(f"0 phone numbers found in Folder: {folder} -> File: {txt_file}")


# Run the program
program()
