#        BEAUTIFUL SOUP
'''
Used to handle and access html page content is a easy way.
Need to be installed before using it.
html data are considered as semi structured data.


pip instal bs4
'''

# import requests
# from bs4 import BeautifulSoup

# #
# url = 'https://books.toscrape.com/'

# response = requests.get(url).text

# print(response)

# soup = BeautifulSoup(response, 'html.parser') # html.parser used to access needed html content from a url

# books = soup.find_all('article', class_='product_pod')  # list that contains all article tag info.

# print(len(books))

# for book in books:
#     print(book.h3.a.text)

#     price = book.find('p', class_='price_color').text
#     print(price[2:])




#  https://wellfound.com/role/l/data-engineer/united-states

''''

### 💼 Job websites

1. [LinkedIn Jobs](https://www.linkedin.com/jobs/?utm_source=chatgpt.com) — job title, company, location, experience
2. [Indeed](https://www.indeed.com/?utm_source=chatgpt.com) — jobs, locations, salary information where displayed
3. [Glassdoor Jobs](https://www.glassdoor.com/Job/?utm_source=chatgpt.com) — jobs, companies, locations
4. [Wellfound](https://wellfound.com/jobs?utm_source=chatgpt.com) — startup/technology jobs
5. [Remote OK](https://remoteok.com/?utm_source=chatgpt.com) — remote jobs, tags, salaries
6. [We Work Remotely](https://weworkremotely.com/?utm_source=chatgpt.com) — remote job listings
7. [Remotive](https://remotive.com/?utm_source=chatgpt.com) — remote technology and other jobs
8. [Himalayas](https://himalayas.app/jobs?utm_source=chatgpt.com) — remote jobs
9. [Naukri](https://www.naukri.com/?utm_source=chatgpt.com) — Indian job listings
10. [Foundit](https://www.foundit.in/?utm_source=chatgpt.com) — Indian jobs
11. [Internshala](https://internshala.com/jobs/?utm_source=chatgpt.com) — internships and entry-level jobs
12. [Cutshort](https://cutshort.io/jobs?utm_source=chatgpt.com) — technology/startup jobs in India

### 🧑‍💻 Good scraping project fields

For each listing, try extracting:

```text
Job Title
Company
Location
Salary
Experience
Job Type
Skills
Posted Date
Job URL
Company URL


'''
import requests
from bs4 import BeautifulSoup

url='https://quotes.toscrape.com/'
response= requests.get(url).text

soup=BeautifulSoup(response,  'html.parser')
quotes= soup.find_all('div',class_='quote')
print(len(quotes))
for quote in quotes:
    print(quote.span.text)
    word= quote. find('span',class_='text').text
    print(word)