from bs4 import BeautifulSoup
import requests
c = 'listicleItem_listicle-item__title__hW_Kn'
response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text,'html.parser')
movies = soup.find_all(name='h3',class_=c)


movies_list = []

for movie in movies:
    movies_list.append(movie.getText())
    
t = movies_list[0]
print(t)
    
for i in reversed(range(len(movies_list))):
    with open('Day-45/m.txt','a') as f:
        f.writelines(f" {movies_list[i]} \n")
         
