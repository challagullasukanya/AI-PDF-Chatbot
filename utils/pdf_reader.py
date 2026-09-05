import PyPDF2


def read_pdf(pdf_path):

    print("\n" + "=" * 60)
    print("STEP 1 : READING PDF")
    print("=" * 60)

    reader = PyPDF2.PdfReader(pdf_path)

    text = ""

    print(f"\nTotal Pages : {len(reader.pages)}")

    for index, page in enumerate(reader.pages):

        print(f"Reading Page {index + 1}")

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    print("\nPDF Loaded Successfully!")

    print("\nTotal Characters :", len(text))

    print("\nPreview\n")

    print(text[:500])

    return text