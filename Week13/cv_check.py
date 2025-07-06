import os
from together import Together
from tkinter import Tk, filedialog

# Together API key
TOGETHER_API_KEY = "please enter your own key here"
client = Together(api_key=TOGETHER_API_KEY)

def select_cv_file():
    """Open file dialog to select CV."""
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select your CV file",
        filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word files", "*.docx")]
    )
    return file_path

def extract_text_from_file(file_path):
    """Extract plain text from supported CV formats."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        import PyPDF2
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join(page.extract_text() for page in reader.pages)
    elif ext == ".docx":
        import docx
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        raise ValueError("Unsupported file type.")

def generate_cv_comment(cv_text):
    """Send CV to Together AI for improvement suggestions."""
    prompt = f"""
I am applying for tech jobs. Please analyze the following CV content and provide constructive feedback or suggestions to improve clarity, relevance, and alignment with modern industry standards.

CV:
{cv_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[
            {"role": "system", "content": "You are a helpful career assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

def main():
    print("AI CV Comment Tool")
    file_path = select_cv_file()

    if not file_path:
        print("No file selected.")
        return

    try:
        cv_text = extract_text_from_file(file_path)
        print("CV loaded successfully. Generating feedback...\n")
        comment = generate_cv_comment(cv_text)
        print("AI Feedback on Your CV:\n")
        print(comment)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
