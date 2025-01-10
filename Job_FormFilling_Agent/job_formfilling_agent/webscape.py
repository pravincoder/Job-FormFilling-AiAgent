import requests
from bs4 import BeautifulSoup

def scrape_job_questions(url, keywords=None):
    """
    Scrapes job-related questions or links from a given website.

    Args:
        url (str): The website URL to scrape.
        keywords (list): List of keywords to identify job-related content (default is predefined).
    """
    try:
        # Default job-related keywords
        if keywords is None:
            keywords = ["What", "How", "Why", "When", "Where", "Which", "Who", "Job", "Role", "Responsibilities", "Skills", "Experience", "Qualifications","Name","Mobile","Email","Address","City","State","Country","Pincode"]

        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the page with Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Collect relevant links and texts
        job_related_data = []

        # Find all anchor tags
        for link in soup.find_all('a', href=True):
            text = link.get_text(strip=True).lower()
            href = link['href']
            
            # Check if any keyword is in the anchor text
            if any(keyword in text for keyword in keywords):
                full_url = href if href.startswith('http') else requests.compat.urljoin(url, href)
                job_related_data.append({"question": text, "link": full_url})
        
        # Display the extracted data
        if job_related_data:
            print("Job-related Questions and Links:")
            for item in job_related_data:
                print(f"Question: {item['question']}")
                print(f"Link: {item['link']}")
                print("-" * 40)
        else:
            print("No job-related questions found on the page.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

# Example usage
url = "https://coditas.com/careers/job-apply-form?jobId=31162000022709366"  # Replace with the target URL
scrape_job_questions(url)