import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
#finding all job cards
job_cards = soup.find_all("div", class_="card-content")
jobs_list = {}

    #open csv file
with open("jobs.csv", mode="w", newline="", encoding="utf-8") as file:
    job_file = csv.writer(file)
    job_file.writerow(['Job Title', 'Company', 'Location', 'Apply_Link'])
    # Extract data
    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        apply_link = job.find("a", string="Apply")

        jobs_list['Job title'] = title
        jobs_list["Company"] = company
        jobs_list['Location'] = location
        jobs_list['Apply_Link'] = apply_link

        print(jobs_list)

        #write row to csv
        job_file.writerow([title, company, location, apply_link])

jobs_file = pd.read_csv('jobs.csv')
jobs_file = jobs_file.dropna()
print(jobs_file)

