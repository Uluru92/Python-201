'''
Write a program that makes a DELETE request to remove the user your create in a previous example.
Again, make a GET request to confirm that information has been deleted.
'''

import requests

body = {
    "id": 12762
}

# Datos del usuario a eliminar
user_id = body['id'] # Tomamos el id del user para agregarlo al final de la URL

# Construimos la URL del recurso
base_url = f"http://demo.codingnomads.co:8080/tasks_api/users/{user_id}"

# Realizamos la solicitud DELETE
delete_response = requests.delete(base_url)

# Verificamos si la eliminación fue exitosa
if delete_response.status_code == 200:
    print("🗑️ Usuario eliminado exitosamente.")
else:
    print(f"❌ Error al eliminar el usuario")

# Intentamos obtener el usuario nuevamente para confirmar que ya no existe
get_response = requests.get(base_url)

try:
    response_json = get_response.json()

    if response_json.get("data") is None:
        print("✅ Confirmación: el usuario ya no existe.")
    else:
        print("⚠️ El usuario aún existe. Algo falló en el intento de eliminarlo.")
        print(response_json)

except ValueError:
    print("❌ Error al convertir la respuesta en JSON.")
    print(get_response.text)