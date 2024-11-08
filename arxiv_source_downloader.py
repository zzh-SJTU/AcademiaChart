import os
import io
import requests
import zipfile
import tarfile
from bs4 import BeautifulSoup


def fetch_arxiv_ids(search_url, base_url="https://arxiv.org/abs/"):
    """
    Fetches arXiv IDs from the search results page.

    Parameters:
    - search_url (str): The URL of the arXiv search results page.
    - base_url (str): The base URL to identify arXiv abstract links (default is arXiv's base URL).

    Returns:
    - List[str]: A list of arXiv IDs extracted from the search results.
    """
    response = requests.get(search_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", href=True)
    arxiv_ids = [
        link["href"].split("/")[-1] for link in links if base_url in link["href"]
    ]

    return arxiv_ids


def download_arxiv_source(arxiv_id, output_folder):
    """
    Downloads and extracts the source files for a given arXiv paper.

    Parameters:
    - arxiv_id (str): The unique identifier for the arXiv paper.
    - output_folder (str): The directory where the source files will be extracted.

    Returns:
    - None
    """
    url = f"https://arxiv.org/e-print/{arxiv_id}"
    response = requests.get(url)
    response.raise_for_status()

    content_type = response.headers.get("content-type")
    if content_type == "application/x-eprint-tar":
        # Handle tarball extraction
        with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as tar:
            tar.extractall(output_folder)
    elif content_type == "application/x-eprint":
        # Handle zip file extraction
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(output_folder)
    else:
        print(f"Unknown content type for arXiv ID {arxiv_id}: {content_type}")


def main():
    # You can change the following url based on which conference's paper you want to
    search_url = "https://arxiv.org/search/?searchtype=all&query=ICDM&abstracts=show&size=200&order=-announced_date_first&start=200"

    # You can specify the output directory of the downloaded latex sourse code
    output_folder = "icdm"

    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Fetch arXiv IDs
    arxiv_ids = fetch_arxiv_ids(search_url)
    print(f"Found {len(arxiv_ids)} arXiv papers.")

    # Download each paper's source
    for arxiv_id in arxiv_ids:
        download_path = os.path.join(output_folder, arxiv_id)
        if os.path.exists(download_path):
            print(f"Folder for {arxiv_id} already exists. Skipping download.")
            continue
        print(f"Downloading source for arXiv ID: {arxiv_id}")
        download_arxiv_source(arxiv_id, download_path)


if __name__ == "__main__":
    main()
