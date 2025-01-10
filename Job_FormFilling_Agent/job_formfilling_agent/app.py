import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from crewai import Crew
from langchain_groq import ChatGroq
import gradio as gr
from resume import extract_text_from_file
from crew import FormFillingAgents, FormFillingTasks


def build_gradio_app():
    """Builds the Gradio interface for the form-filling app."""
    logging.basicConfig(level=logging.INFO)

    # Define input elements
    resume_input = gr.File(label="Upload Resume", file_types=[".pdf", ".docx", ".txt"])
    job_desc_input = gr.Textbox(label="Job Description", placeholder="Enter job description here")
    questions_input = gr.Textbox(label="Questions", placeholder="Enter questions, separated by commas")
    api_key_input = gr.Textbox(label="GROQ API Key", placeholder="Enter your GROQ API Key")
    
    # Define output elements
    answers = gr.Textbox(label="Tailored Answer to the Question Based on Your Resume", interactive=False)

    # Processing function
    def process_inputs(api_key, resume_input, job_desc, questions):
        try:
            # Debugging
            logging.info("Received API Key, Resume, Job Description, and Questions.")
            logging.info(f"API Key: {api_key}")
            # Save API key to .env file it the user has session active 
            if api_key:
                env_path = Path(__file__).parent / ".env"
                with open(env_path, "w") as env_file:
                    env_file.write(f"GROQ_API_KEY={api_key}")
                logging.info("API Key saved to .env file.")
            else:
                logging.warning("No API Key provided.")

            load_dotenv()
            
            # Initialize language model
            llm = ChatGroq(
                model="groq/llama-3.1-8b-instant",
                api_key=os.getenv("GROQ_API_KEY"),
            )
            logging.info("Language model initialized successfully.")

            # Extract text from resume
            resume_text = extract_text_from_file(resume_input)
            logging.info("Resume text extracted.")

            # Initialize agents and tasks
            agents = FormFillingAgents()
            analysis_agent = agents.resume_analysis_agent(llm)
            qa_agent = agents.question_answering_agent(llm)
            tasks = FormFillingTasks()
            profile_task = tasks.profile_analysis_task(analysis_agent, resume_text, job_desc)
            qa_task = tasks.question_answering_task(qa_agent, questions)

            # Run Crew pipeline
            crew = Crew(
                agents=[analysis_agent, qa_agent],
                tasks=[profile_task, qa_task],
                verbose=True,
                max_rpm=29,
            )
            results = crew.kickoff()
            logging.info("Pipeline executed successfully.")
            return str(results)

        except Exception as e:
            logging.error(f"Error during processing: {e}")
            return f"Error during processing: {str(e)}"
    # Gradio interface
    interface = gr.Interface(
        fn=process_inputs,
        inputs=[api_key_input, resume_input, job_desc_input, questions_input],
        outputs=[answers],
        title="Form Filling Assistant",
        description="Upload a resume, provide a job description, input API key, and ask questions to get tailored responses.",
    )
    interface.launch()

if __name__ == '__main__':
    build_gradio_app()
