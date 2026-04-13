import PyPDF2
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text

# Analyze resume using AI
def analyze_resume(text):
    prompt = f"""
    You are an expert ATS resume evaluator.

    Analyze the resume and provide:
    1. ATS Score (out of 100)
    2. Key Strengths
    3. Weaknesses
    4. Suggestions for improvement

    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content