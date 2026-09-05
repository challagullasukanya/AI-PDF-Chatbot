import chromadb


def store_in_chromadb(chunks, embeddings):

    print("\n" + "=" * 60)
    print("STEP 4 : STORING DATA IN CHROMADB")
    print("=" * 60)

    client = chromadb.PersistentClient(path="./chroma_db")

    try:
        client.delete_collection("pdf_chatbot")
    except:
        pass

    collection = client.create_collection("pdf_chatbot")

    collection.add(

        ids=[str(i) for i in range(len(chunks))],

        documents=chunks,

        embeddings=embeddings.tolist()

    )

    print("\nVector Database Created Successfully!")

    print("Collection Name : pdf_chatbot")

    print("Database Path : ./chroma_db")

    return collection


def show_database(collection):

    print("\n" + "=" * 60)
    print("STEP 5 : SHOWING STORED DATA")
    print("=" * 60)

    data = collection.get(include=["documents", "embeddings"])

    total = len(data["ids"])

    print(f"\nTotal Stored Records : {total}")

    for i in range(total):

        print("\n" + "=" * 60)

        print(f"Document ID : {data['ids'][i]}")

        print("\nStored Chunk\n")

        print(data["documents"][i])

        print("\nEmbedding Dimension :",
              len(data["embeddings"][i]))

        print("\nFirst 10 Values")

        print(data["embeddings"][i][:10])

    print("\n" + "=" * 60)
    print("END OF DATABASE")
    print("=" * 60)