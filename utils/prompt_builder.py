def build_prompt(question, retrieved_chunks):

    print("\n" + "=" * 60)
    print("STEP 7 : BUILDING PROMPT")
    print("=" * 60)

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an intelligent AI Assistant.

Answer ONLY using the context below.

If the answer is not available,
reply:

"I couldn't find the answer in the provided PDF."

====================

Context

{context}

====================

Question

{question}

====================

Answer

"""

    print("\nPrompt Created Successfully!")

    print("\nPrompt Preview\n")

    print(prompt[:1200])

    return prompt