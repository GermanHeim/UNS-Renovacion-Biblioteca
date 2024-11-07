import requests
from bs4 import BeautifulSoup
import os

login_url = "http://catalogo.uns.edu.ar/vufind/MyResearch/Home"
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

if username and password:
    print("Datos de inicio de sesión cargados correctamente")
else:
    print("No se encontraron datos de inicio de sesión")
    exit()

session = requests.Session()

login_page = session.get(login_url)
soup = BeautifulSoup(login_page.content, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf'}).get('value')

if not csrf_token:
    print("No se encontro el token CSRF.")
    exit()

login_payload = {
    'username': username,
    'password': password,
    'auth_method': 'ILS',
    'csrf': csrf_token,
    'processLogin': 'Entrar'
}

login_response = session.post(login_url, data=login_payload)
if login_response.status_code == 200:
    print("Sesión iniciada.")
else:
    print("Error al iniciar sesión.")
    exit()

renew_page_url = "http://catalogo.uns.edu.ar/vufind/MyResearch/Home?redirect=0"
renew_page = session.get(renew_page_url)
soup = BeautifulSoup(renew_page.content, 'html.parser')

forms = soup.find_all('form', class_="form-renovar")
renew_count = 0

endpoint_renovar = "http://catalogo.uns.edu.ar/vufind/MyResearch/renovar"

for form in forms:
    library_code = form.find('input', {'name': 'library_code'}).get('value')
    inventarios = form.find('input', {'name': 'inventarios[]'}).get('value')

    renew_payload = {
        'library_code': library_code,
        'inventarios[]': inventarios
    }

    renew_response = session.post(endpoint_renovar, data=renew_payload)
    if renew_response.status_code == 200:
        renew_count += 1
    else:
        print(f"Error al renovar {inventarios}.")

print(f"Se renovaron {renew_count} libros.")
