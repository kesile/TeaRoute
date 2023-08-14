import openai

def embed(inp):
    response = openai.Embedding.create(
        input=inp,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings