import pandas as pd
from PyPDF2 import PdfReader

def analyze_file(file):

    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
        return df.head().to_string()

    elif file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text[:1500]

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")[:1500]

    return "Unsupported file type"