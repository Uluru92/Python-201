'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

body = {
    "id": 12762,
    "email": "Sharon92@hotmail.com",
    "first_name": "Sharon",
    "last_name": "Fonseca Araya",
    "created_at": 1750104729000,
    "updated_at": 1750104729000
}

user_id = body['id'] # Tomamos el id del user para agregarlo al final de la URL

base_url = f"http://demo.codingnomads.co:8080/tasks_api/users/{user_id}" # Formamos la URL completa del usuario que queremos modificar

put_response = requests.put(base_url, json=body) # Solicitud PUT para actualizar el usuario

response = requests.get(base_url)

print(f'Your information has been updated: \n{response.content}')


if put_response.status_code == 200: # Verificar si el PUT fue exitoso
    print("✅ Información actualizada exitosamente.")
else:
    print(f"❌ Error al actualizar: {put_response.status_code}")
    print(put_response.text)

# Hacer la solicitud GET para confirmar que se guardó la información
get_response = requests.get(base_url)

# Verificar si el GET fue exitoso
if get_response.status_code == 200:
    user_data = get_response.json()['data']  # Acceder al contenido de la respuesta
    print("\n📋 Información actual del usuario:")
    print(f"Nombre: {user_data['first_name']} {user_data['last_name']}")
    print(f"Email: {user_data['email']}")
else:
    print(f"❌ Error al obtener los datos: {get_response.status_code}")
    print(get_response.text)