import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.naukri.com/data-scientist-jobs?k=data%20scientist'


def get_jobs():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_elements = soup.select(".jobTuple.bgWhite.br4.mb-8 .jobTupleHeader .info.fleft a.title.fw500.ellipsis")

    job_titles = [job.text for job in job_elements]

    return job_titles


if __name__ == '__main__':
    jobs = get_jobs()
    for job in jobs:
        print(job)
    print(f"\nFound {len(jobs)} job titles.")
