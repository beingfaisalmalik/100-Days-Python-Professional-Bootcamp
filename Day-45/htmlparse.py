from bs4 import BeautifulSoup
with open('Day-45/index.html','r') as f:
     d = f.read()


soup = BeautifulSoup(d, 'html.parser')
print(soup.title.string)

print(soup.prettify())

tags = soup.find_all(name="a")
print(tags)

for tage in tags:
    print(tage.getText())
    print(tage.get('href'))
