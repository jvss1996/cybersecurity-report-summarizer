# Cybersecurity Report Summarizer

A Python tool to **summarize PDF cybersecurity threat reports** into concise executive summaries using Hugging Face’s `facebook/bart-large-cnn` model.

---

## 🚀 Features
- Extracts text from PDF reports  
- Summarizes text into short, readable insights  
- Generates a 5-sentence executive summary  
- Saves summary to `summary.txt`  

---

## 📂 Project Structure
```
cybersecurity-report-summarizer/
├── text_summarizer.py                         # Main script for summarization
├── requirements.txt                           # Python dependencies with versions
├── ibm-threat-intelligence-2025-report.pdf    # Report PDF
├── summary.txt                                # Output summary file (generated)
└── README.md                                  # Project documentation
```
---

## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/jvss1996/cybersecurity-report-summarizer.git
   cd cybersecurity-report-summarizer
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
3. Create a .env file with your Hugging Face API key:
   ```bash
   echo "HF_API_KEY=hf_your_api_key_here" > .env

---

## ▶️ Usage
Run the summarizer with:
```bash
python3 main.py sample_report.pdf
```
If no argument is given, it defaults to sample_report.pdf.

Output -> (summary.txt)

---

## 🛠 Requirements
- Python 3.8+
- Hugging Face account & API key (free tier available)
