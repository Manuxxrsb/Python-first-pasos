import requests
from bs4 import BeautifulSoup

#url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

#response = requests.get(url)
# lets check the status
#status = response.status_code
#print(status) # 200 significa que la busqueda fue exitosa

url = 'https://www.farmaciasahumada.cl/ahumada/vitaminas/esenciales'

response = requests.get(url) #obtengo el codigo de operaion
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
productos = soup.find_all('div',class_ = "col-6 col-sm-4 col-lg-3")
print("Productos encontrados:",len(productos))


#muestro los productos de manera ordenada
for i in range(len(productos)):
    print("----------------------------------------------")
    laboratorio = productos[i].find('span',class_="link")
    nombre_producto = productos[i].find('a',class_="link")
    precio = productos[i].find('span',class_="d-block default-price")
    
    print("Laboratorio: " + laboratorio.text.strip() + "\nNombre producto: ",nombre_producto.text.strip() + "\nPrecio producto: ",precio.text.strip())









    
    





 

