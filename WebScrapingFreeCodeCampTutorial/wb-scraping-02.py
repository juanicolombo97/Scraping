from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    URL_PAGINA = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    #Filtramos skills no deseadas
    print('Put some skill your not familiar with')
    unfamiliar_skill = input('>')
    print(f'Filtering out: {unfamiliar_skill}')
    # Obtenemos la pagina
    pagina_web = requests.get(URL_PAGINA).text

    soup = BeautifulSoup(pagina_web, 'lxml')

    # Buscamos los trabajos que hay
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text.replace(' ','')
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','').strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as file:
                    more_info = job.header.h2.a['href']
                    file.write(f'Compania: {company_name}\nSkills: {skills}\nPublished date: {published_date}\nMoreInfo: {more_info}\n')
                    print('Job saved.')


find_jobs()