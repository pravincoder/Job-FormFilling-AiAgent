import os
from textwrap import dedent
from crewai import Agent, Task


class FormFillingAgents:
    """Agents for form-filling tasks."""

    def resume_analysis_agent(self,llm):
        """Creates an agent to analyze resumes and match job descriptions."""
        return Agent(
            role="Resume Analysis Agent",
            llm=llm,
            goal="Analyse the resume and extract the required information.",
            backstory=dedent("""You are a Resume Analysis Agent that analysis provided resume
                             and extract the required information from it.Seach for the best matching job online
                             so that it can be used for further processes like Job Form Filling."""),
        )

    def question_answering_agent(self,llm):
        """Creates an agent to answer user questions."""
        return Agent(
            role="Question Answering Agent",
            llm=llm,
            goal="Answer user-provided questions accurately and correctly.",
            backstory=dedent("""You are a Question Answering Agent
                    and you have been assigned to answer the questions asked by the users.
                    You have to make sure that the answers are correct and accurate."""),
        )

class FormFillingTasks:
    """Tasks for form-filling processes."""

    def profile_analysis_task(self, agent, resume_data, job_desc):
        """Creates a task for analyzing resumes against job descriptions."""
        return Task(
            name="Profile Analysis Task",
            description=dedent(f"""
        Your Task: Analyze the provided resume and job description to identify key matches and insights.  
        
        **Objectives:**  
        - Understand the company's requirements and expectations for the role by reviewing the job description.  
        - Compare and match the user's resume data to the job description, highlighting relevant skills, achievements, and experiences.  
        - Extract actionable insights from the resume that align with the role's requirements.  

        **Input Data:**  
        - User-provided resume: {resume_data}  
        - Job description for the role: {job_desc}  
        
        Your output should demonstrate a clear understanding of the job's demands and the user's suitability based on their resume."""),
            expected_output=dedent(f"""You have successfully understand the companies requirement and the job description 
                try to match the resume with the job description and extract the required information."""),
            agent=agent,
        )

    def question_answering_task(self, agent, questions):
        """Creates a task for answering questions from hiring personnel."""
        return Task(
            name="Question Answering Task",
            description=dedent(f"""
        Your Task: Respond to job application or HR-related questions by providing answers that maximize the user's chances of securing the job.  
        
        **Objectives:**  
        - Leverage the user's resume and the job description to craft tailored responses.  
        - Provide accurate, thoughtful, and professional answers that reflect the user's actual skills, experiences, and qualifications.  
        - Ensure that the answers align with the role's requirements and highlight the user's suitability.  

        **Guidelines:**  
        - Do **not** fabricate skills or qualifications not present in the resume.  
        - Emphasize the user's strengths, achievements, and relevance to the role.  
        - Focus on creating responses that fulfill job application requirements or address HR queries effectively.  

        **Input Data:**  
        - List of questions from HR or hiring personnel: {questions}  

        Your responses will directly impact the user's success in the application process. Aim for precision, professionalism, and alignment with the provided data."""),           
                               
            expected_output="You final output must include all questions asked and their answers .",
            agent=agent,
        )

