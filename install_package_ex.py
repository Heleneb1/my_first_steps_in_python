#pip freeze permet de lister les packages installés
#pour installer un package on utilise pip install nom_du_package
#pour désinstaller un package on utilise pip uninstall nom_du_package
#pour mettre à jour un package on utilise pip install --upgrade nom_du_package
#exemple
#pip install requests
#pip freeze
#pip uninstall requests
#pip freeze
#pip install --upgrade requests
#pip freeze

#Pour utiliser le package installer
import requests
from bs4 import BeautifulSoup

# url="https://www.google.com"
# response = requests.get(url) 

# print(response.status_code) #200


#ETL
#Extract, Transform, Load

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title)
class_name = "gem-c-document-list__item"
titres= soup.find_all(class_=class_name)
# print(soup.find_all('a', class_=class_name))
# print(titres)
titres_text = []
for titre in titres:
    titres_text.append(titre.text)
print(titres_text)