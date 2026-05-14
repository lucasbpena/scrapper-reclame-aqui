from pathlib import Path
import csv


def save_dicts_to_csv(data, filename):
    """
    Save a list of dictionaries into a CSV file.

    Parameters
    ----------
    data : list[dict]
        List of dictionaries with same keys.
    filename : str
        Output filename inside data/ folder.
    """

    if not data:
        raise ValueError("Data list is empty")

    # Root/data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    filepath = data_dir / filename

    # Use keys from first dict as CSV columns
    fieldnames = data[0].keys()

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    return filepath

def read_dicts_from_csv(filename):
    """
    Read a CSV file into a list of dictionaries.

    Parameters
    ----------
    filename : str
        Input filename inside data/ folder.

    Returns
    -------
    list[dict]
        List of dictionaries, one per row.
    """

    data_dir = Path("data")
    filepath = data_dir / filename

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)