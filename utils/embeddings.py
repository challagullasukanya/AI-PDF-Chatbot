from config import embedding_model


def generate_embeddings(chunks):

    print("\n" + "=" * 60)
    print("STEP 3 : GENERATING EMBEDDINGS")
    print("=" * 60)

    embeddings = embedding_model.encode(chunks)

    print(f"\nEmbedding Model : all-MiniLM-L6-v2")
    print(f"Total Embeddings : {len(embeddings)}")

    for index, embedding in enumerate(embeddings):

        print("\n" + "-" * 60)
        print(f"Chunk {index + 1}")

        print(f"Embedding Dimension : {len(embedding)}")

        print("\nFirst 10 Values")

        print(embedding[:10])

    return embeddings