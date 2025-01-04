import os
from textwrap import dedent
from crewai import Agent, Crew, Process, Task
import logging
import time
from resume import DocData
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    # Add Your API Key from (https://console.groq.com/keys)
    api_key=os.environ['GROQ_API_KEY'],
)


class form_filling_agents:
    """ALL the agents for form filling task"""

    def resume_analysis_agent(self):
        """Resume Analysis Agent"""
        return Agent(
            role="Resume Analysis Agent",
            llm=llm,
            goal="Extract the required information from the resume provided by the user.",
            backstory=dedent(f"""You are a Resume Analysis Agent that analysis provided resume
                             and extract the required information from it.
                             so that it can be used for further processes like Job Form Filling."""),
        )

    def question_answering_agent(self):
        """Question Answering Agent"""
        return Agent(
            role="Question Answering Agent",
            llm=llm,
            goal="To answer the questions asked by the users.",
            backstory=dedent(f"""You are a Question Answering Agent
                             and you have been assigned to answer the questions asked by the users.
                    You have to make sure that the answers are correct and accurate."""),
        )


class FormFillingTask:
    def Profile_analysis_task(self, agent, data, job_desc):
        """Understand Companies requirement Task"""
        return Task(
            name="Form Filling Task",
            description=dedent(f"""Your Task is to understand the Understand Companies requirement match it with the users resume
                               and try to use the resume and other provided data to understand more about the user and compared to the job.
                               the user provided resume :- {data}
                               job description of the company for the role :- {job_desc}
                            we will use this information to fill the form in the next task.
                            
            """),
            expected_output=dedent(
                f"""You have successfully understand the companies requirement and the job description 
                try to match the resume with the job description and extract the required information."""),
                
            agent=agent)

    def question_answering_task(self, agent, questions):
        """Question Answering Task"""
        return Task(
            name="Question Answering Task",
            description=dedent(f"""Your Task is to answer the questions asked by the HR or hiring personal 
                               you should answer the question for the user so that the user gets the job.
                               the list of questions asked by the HR or hiring personal :- {questions} answer them one by one.
                            if the user is selected you will recieve a commission of 100$.
                            you must answer the questions correctly and accurately considering the resume of the user 
                            don't add skills just on your own only mention skill that are present in the resume.
            """),
            expected_output=dedent(
                f"""You final output must include all the questions and their answers .
                """),
            agent=agent,
        )


# Test or crew on a sample data
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    file_path = 'Job_FormFilling_Agent/job_formfilling_agent/Pravin Maurya.pdf'  # Add your resume path here pdf
    data = DocData(file_path).extract_pdf_text()
    questions =[ "Describe a project you are most proud of and why.","Why should you be hired for this role?"]
    job_desc = dedent("""About the work from home job/internship

Join us as an AI Intern at Testline and be part of shaping the future of education! You'll work on exciting projects that use the power of AI to revolutionize how students learn, engage, and succeed. From crafting intelligent tools to delivering personalized learning experiences, your work will directly impact the next generation of learners. Collaborate with passionate teams across product, tech, and content to build scalable, game-changing solutions that redefine education.

Key Responsibilities:

1. Develop and deploy innovative solutions leveraging advanced AI/ML models for recommendation systems, adaptive learning, and personalized lessons.
2. Analyze data to derive insights and improve student performance.
3. Work with cross-functional teams to integrate AI features into the platform.
Skill(s) required

Artificial Intelligence
Data Science
Machine Learning
Python
SQL
Teaching
Earn certifications in these skills
Learn Python
Learn Voice App Development
Learn SQL
Learn Machine Learning
Learn Data Science
Who can apply

Only those candidates can apply who:
1. are available for the work from home job/internship
2. can start the work from home job/internship between 21st Dec'24 and 25th Jan'25
3. are available for duration of 2 months
4. have relevant skills and interests
* Women wanting to start/restart their career can also apply.""")
    analysis_agent = form_filling_agents().resume_analysis_agent()
    question_answering_agent = form_filling_agents().question_answering_agent()
    profile_analysis_task = FormFillingTask().Profile_analysis_task(analysis_agent, data, job_desc)
    question_answering_task = FormFillingTask().question_answering_task(question_answering_agent, questions)
    form_filling_crew = Crew(
        agents=[analysis_agent, question_answering_agent],
        tasks=[profile_analysis_task,question_answering_task],
        verbose=True,
        max_rpm=29,
    )
    form_filling_crew.kickoff()
