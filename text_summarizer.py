import os
import sys
from dotenv import load_dotenv
import PyPDF2
from transformers import pipeline

# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv('HF_API_KEY')

PDF_PATH = sys.argv[1] if len(sys.argv) > 1 else 'sample_report.pdf'
OUTPUT_PATH = 'summary.txt'

# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

# Step 2: Summarize text using Hugging Face pipeline
def get_summary(text, hf_api_key):
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn', token=hf_api_key)
    # Hugging Face models have a max token limit, so chunk if needed
    max_chunk = 1024
    text_chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ''
    for chunk in text_chunks:
        input_length = len(chunk.split())
        max_length = min(130, input_length - 5) if input_length > 35 else input_length
        min_length = min(30, max_length)
        result = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summary += result[0]['summary_text'] + ' '
    return summary

def get_five_sentence_summary(summary_text):
    import re
    sentences = re.split(r'(?<=[.!?]) +', summary_text)
    five_sentences = ' '.join(sentences[:5])
    return five_sentences

if __name__ == '__main__':
    print('Extracting text from PDF...')
    text = extract_text_from_pdf(PDF_PATH)
    print('Summarizing text...')
    summary = get_summary(text, HF_API_KEY)
    print('Structuring summary...')
    five_sentence_summary = get_five_sentence_summary(summary)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('Executive Summary:\n')
        f.write(five_sentence_summary + '\n')
    print(f'Summary written to {OUTPUT_PATH}')
