# MCQ Generator

A streamlined and interactive application that utilizes the Gemini API to dynamically generate high-quality Multiple Choice Questions (MCQs) from PDF documents or topics provided by the user.

## Features

- **PDF Input**: Generate MCQs by extracting text from uploaded PDF files.  
- **Topic-Based Generation**: Enter a topic to instantly create tailored MCQs.  
- **Gemini API Integration**: Ensures accuracy and contextual relevance of generated questions.  
- **Streamlit Interface**: Clean and intuitive user interface for a seamless experience.

## How to Use

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/MCQ-Generator.git  
   cd mcq-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   streamlit run app.py  
   ```

4. **Upload a PDF or type a topic, and view the generated MCQs along with answer keys.**

## Technologies Used

- **Python**: Core development language.
- **Streamlit**: Framework for building the application interface.
- **Gemini API**: Powers question generation with advanced NLP capabilities.
- **PyPDF2**: Handles PDF text extraction.
