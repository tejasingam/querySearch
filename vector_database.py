# vector_database.py

from weaviate.client import Client

# Initialize Weaviate client (replace with your Weaviate server URL)
client = Client("http://localhost:8080")

def insert_document_vector(doc_id, vector):
    # Example function to insert document vector into Weaviate
    client.create("Document", {"id": doc_id, "vector": vector})
    print(f"Document vector inserted for document {doc_id}")

# Example usage
# if __name__ == '__main__':
#     # Example vector insertion
#     insert_document_vector("123456", [0.1, 0.2, 0.3])  # Replace with actual vector
