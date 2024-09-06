import requests
from bs4 import BeautifulSoup

#url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

#response = requests.get(url)
# lets check the status
#status = response.status_code
#print(status) # 200 significa que la busqueda fue exitosa

url = 'https://www.farmaciasahumada.cl/ahumada/vitaminas/esenciales'

response = requests.get(url) #obtengo el codigo de operacion
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
productos = soup.find_all('div',class_ = "col-6 col-sm-4 col-lg-3")
print("Productos encontrados:",len(productos))

#ahora accedo a los datos especificos que quiero

proveedores = soup.find_all('span' , class_="link")
nombre = soup.find_all('div',class__="pdp-link")
#print(titulo[0])

#texto = proveedores[0].get_text() #guardo el texto del span

for i in range(len(productos)): #accedo a todos los productos
    print(proveedores[i].get_text())
    print(nombre[i].get_text())
    
    





 

