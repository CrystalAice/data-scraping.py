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
job_table = []
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

  jobs_list = {
        'Job title' : title,
        "Company" : company,
        'Location' : location,
        'Apply_Link' : apply_link["href"] if apply_link else "N/A"
    }

        job_table.append(jobs_list)

        #write row to csv
        job_file.writerow([title, company, location, apply_link])

job_final = pd.DataFrame(job_table)
print(job_final)

jobs_file = pd.read_csv('jobs.csv')
jobs_file = jobs_file.dropna()
print(jobs_file)

