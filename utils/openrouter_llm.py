from config import client, MODEL_NAME


def generate_answer(prompt):

    print("\n" + "=" * 60)
    print("STEP 8 : OPENROUTER GENERATING ANSWER")
    print("=" * 60)

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        answer = response.choices[0].message.content

        print("\nOpenRouter Response\n")
        print(answer)

        return answer

    except Exception as e:

        print(
            f"\nError generating response: {e}"
        )

        return (
            "Sorry, an error occurred while "
            "generating the response."
        )