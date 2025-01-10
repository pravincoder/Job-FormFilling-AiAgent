# Form-Filling AI Agent

Form-Filling AI Agent is an intelligent tool designed to automate the process of answering job-related form questions. By leveraging state-of-the-art AI models and a modular task-based approach, the agent analyzes resumes, understands job descriptions, and generates accurate, context-aware responses to questions asked by recruiters or HR professionals.

## Features

- **Resume Analysis**: Extracts key information from resumes to match job requirements.
- **Question Answering**: Provides accurate and contextually appropriate answers to job-related questions.
- **Job Description Matching**: Matches user profiles with job descriptions to craft tailored responses.
- **Crew AI Integration**: Implements multi-agent systems using Crew AI for modular and scalable processing.
- **Groq LLM Support**: Uses the Groq LLM for high-quality natural language understanding and generation.

## Prerequisites

Before running the project, ensure the following are installed:
- **Python**: Version 3.8 or higher.
- **Required Python Libraries**: Install dependencies using the `requirements.txt` file.
- **API Key**: A Groq API Key is required for the ChatGroq LLM.

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/form-filling-ai-agent.git  
cd form-filling-ai-agent  
```
### Step 2: Install Dependencies
```bash
pip install -r requirements.txt  
```
### Step 3: Set Up Environment Variables
Create a .env file in the project root with the following content:

GROQ_API_KEY=your_groq_api_key


## Usage

### Step 1: Provide Resume and Job Details
1. Save your resume in PDF format.  
2. Update the file path in the script:
   ```python
   file_path = 'path_to_your_resume.pdf'
   ```

### Step 2: Run the Script
Run the main script using the following command:  
```bash
python main.py
```

### Step 3: Review Outputs
- **Profile Analysis**: Compares your resume with job requirements and extracts relevant details.  
- **Question Answering**: Provides precise answers to the specified questions.  
