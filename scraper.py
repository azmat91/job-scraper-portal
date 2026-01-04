import requests
from bs4 import BeautifulSoup
from models import db, Job

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"  # demo site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")

    for job_element in job_elements[:10]:  # limit to 10 for demo
        title = job_element.find("h2", class_="title").text.strip()
        company = job_element.find("h3", class_="company").text.strip()
        location = job_element.find("p", class_="location").text.strip()
        link = job_element.find("a")["href"]

        job = Job(title=title, company=company, location=location, link=link)
        db.session.add(job)

    db.session.commit()
