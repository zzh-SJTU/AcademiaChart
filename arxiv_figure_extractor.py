import os
import re
import shutil
import json
from tqdm import tqdm


def extract_figures_and_captions(src_folder, dest_folder, extracted_info):
    """
    Extracts figures and their captions from .tex files in the source folder, saving figures to the destination folder
    and appending figure information to the extracted_info list.

    Parameters:
    - src_folder (str): Path to the source folder containing .tex files.
    - dest_folder (str): Path to the destination folder where figures will be saved.
    - extracted_info (list): A list to store information about extracted figures and captions.

    Returns:
    - None
    """
    figure_pattern = re.compile(
        r"\\begin{figure}.*?\\includegraphics.*?{(.*?)}.*?\\caption{([^}]*)}.*?\\end{figure}",
        re.DOTALL,
    )

    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".tex"):
                with open(
                    os.path.join(root, file), "r", encoding="utf-8", errors="ignore"
                ) as f:
                    content = f.read()

                    # Remove comments and clean the content
                    cleaned_content = "\n".join(
                        [line.split("%")[0] for line in content.split("\n")]
                    )

                    # Find and process each figure and its caption
                    for match in figure_pattern.findall(cleaned_content):
                        figure_path, caption = match
                        caption = " ".join(caption.split()).strip()

                        # Skip captions with unprocessed braces
                        if "{" in caption or "}" in caption:
                            continue

                        figure_full_path = os.path.join(root, figure_path).replace(
                            "\\", "/"
                        )
                        if os.path.exists(
                            figure_full_path
                        ) and figure_full_path.endswith((".png", ".jpg", ".jpeg")):
                            os.makedirs(
                                dest_folder, exist_ok=True
                            )  # Create destination folder if valid figure found
                            shutil.copy(figure_full_path, dest_folder)

                            extracted_info.append(
                                {
                                    "figure_path": os.path.join(
                                        dest_folder, os.path.basename(figure_path)
                                    ).replace("\\", "/"),
                                    "caption": caption,
                                    "source": os.path.join(root, file).replace(
                                        "\\", "/"
                                    ),
                                    "arxiv_id": os.path.basename(src_folder),
                                }
                            )


def save_extracted_info_to_json(extracted_info, output_json):
    """
    Saves the extracted information about figures and captions to a JSON file.

    Parameters:
    - extracted_info (list): List containing information about extracted figures and captions.
    - output_json (str): Path to the JSON file where information will be saved.

    Returns:
    - None
    """
    with open(output_json, "w") as json_file:
        json.dump(extracted_info, json_file, indent=4)


def main():
    top_folder = "icdm"
    output_json = "icdm_figures_and_captions.json"
    output_figure_path = "icdm_figures"

    # Load existing JSON data if available
    if os.path.exists(output_json):
        with open(output_json, "r") as f:
            extracted_info = json.load(f)
    else:
        extracted_info = []

    # Process each arXiv ID folder
    for arxiv_id in tqdm(os.listdir(top_folder), desc="Processing arXiv Papers"):
        src_folder_path = os.path.join(top_folder, arxiv_id)
        dest_folder_path = os.path.join(output_figure_path, arxiv_id)

        if os.path.isdir(src_folder_path):
            print(f"Processing {arxiv_id}")
            extract_figures_and_captions(
                src_folder_path, dest_folder_path, extracted_info
            )

    # Save extracted information to JSON
    save_extracted_info_to_json(extracted_info, output_json)


if __name__ == "__main__":
    main()
