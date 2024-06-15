# data_handling.py

# data_handling.py

import pandas as pd


import pandas as pd

def load_projects_dataset(file_path):
    df = pd.read_csv(file_path)
    return df
# Example usage
# if __name__ == '__main__':
#     dataset = load_arxiv_dataset('arxiv-metadata-oai-snapshot.json')
#     print(f"Number of documents in dataset: {len(dataset)}")
