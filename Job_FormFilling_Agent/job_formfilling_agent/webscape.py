from bs4 import BeautifulSoup
import requests
def form_links(link):
    """Extract all the form questions from the given URL"""
    # URL of the page to scrape
    html_code = requests.get(link).text

    # Parse the HTML code
    soup = BeautifulSoup(html_code, 'html.parser')

    # Find all form tags and id = 'assessment_questions'  
    forms = soup.find_all('div', id='details_container')


    # Extract questions (assumes they are in <label> tags)
    for form in forms:
        questions = form.find_all('label')
        for question in questions:
            print(question.get_text(strip=True))


# Test the function
if __name__ == '__main__':
    form_links('https://internshala.com/internship/details/work-from-home-artificial-intelligence-ai-internship-at-testline1734753060?referral=similar_internships&aid=232438948&iid=2667238')