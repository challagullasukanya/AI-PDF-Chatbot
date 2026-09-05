def create_chunks(text, chunk_size=500, overlap=100):

    print("\n" + "=" * 60)
    print("STEP 2 : CREATING CHUNKS")
    print("=" * 60)

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    print(f"\nChunk Size : {chunk_size}")

    print(f"Overlap : {overlap}")

    print(f"Total Chunks : {len(chunks)}")

    for index, chunk in enumerate(chunks):

        print("\n" + "-" * 60)

        print(f"Chunk {index+1}")

        print("-" * 60)

        print(chunk)

    return chunks