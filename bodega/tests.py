from django.test import TestCase
import requests
import json

# Create your tests here.
def test_add_new_producto():
    App_URL="http://127.0.0.1:8080/api/bodega"
    f = open('D:/PC/FER/Proyectos/Pruebas/Django test/apiRest/TestCases/create.json','r')
    request_json=json.loads(f.read())
    response = requests.post(App_URL,request_json)
    print(response.text)

def test_update_producto():
    App_URL="http://127.0.0.1:8080/api/bodega/4"
    f = open('D:/PC/FER/Proyectos/Pruebas/Django test/apiRest/TestCases/update.json','r')
    request_json=json.loads(f.read())
    response = requests.put(App_URL,request_json)
    print(response.text)

def test_delete_producto():
    App_URL="http://127.0.0.1:8080/api/bodega/4"
    response = requests.delete(App_URL)
    print(response.text)

def test_get_productos():
    App_URL="http://127.0.0.1:8080/api/bodega"
    response = requests.get(App_URL)
    print(response.text)

def test_get_productos_E():
    App_URL="http://127.0.0.1:8080/api/bodega/E"
    response = requests.get(App_URL)
    print(response.text)

def test_get_productos_S():
    App_URL="http://127.0.0.1:8080/api/bodega/S"
    response = requests.get(App_URL)
    print(response.text)

def test_get_productos_D():
    App_URL="http://127.0.0.1:8080/api/bodega/D"
    response = requests.get(App_URL)
    print(response.text)
