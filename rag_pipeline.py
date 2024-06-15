# rag_pipeline.py

from transformers import pipeline

# Initialize text generation pipeline
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

def generate_response(query):
    # Example function to generate response using GPT-Neo model
    response = generator(query, max_length=100)[0]['generated_text']
    return response

# Example usage
# if __name__ == '__main__':
#     # Example query and response generation
#     query = "What is the impact of AI on society?"
#     response = generate_response(query)
#     print(f"Generated response: {response}")
