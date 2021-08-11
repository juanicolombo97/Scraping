from bs4 import BeautifulSoup

with open('WebScrapingFreeCodeCampTutorial/home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    
    # Find elements
    tags = soup.find_all('h5')
    
    elements = soup.find_all('div', class_='card')
    for element in elements:
        course_name = element.h5.text
        course_price = element.a.text

        print(f"Course name: {course_name}, Price: {course_price}")

        