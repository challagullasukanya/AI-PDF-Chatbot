from config import embedding_model


def semantic_search(collection, question):

    print("\n" + "=" * 60)
    print("STEP 6 : SEMANTIC SEARCH")
    print("=" * 60)

    print("\nUser Question:")
    print(question)

    print("\nGenerating Query Embedding...")

    query_embedding = embedding_model.encode(question).tolist()

    print("\nQuery Embedding Generated Successfully!")

    print("\nSearching ChromaDB...")

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=3,

        include=["documents", "distances"]

    )

    documents = results["documents"][0]

    distances = results["distances"][0]

    print("\nTop Retrieved Chunks\n")

    for i in range(len(documents)):

        similarity = 1 - distances[i]

        print("-" * 60)

        print(f"Result {i+1}")

        print(f"Similarity Score : {similarity:.4f}")

        print()

        print(documents[i])

        print()

    return documents