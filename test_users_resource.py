from requests import post, delete, get

# Правильный запрос
print(get("http://127.0.0.1:5000/api/v2/users").json())

# Правильный запрос
print(get("http://127.0.0.1:5000/api/v2/users/5").json())

# Не существующий такого id
print(get("http://127.0.0.1:5000/api/v2/users/12312312").json())

# Передаём в поле age вместо Integer - String
print(post("http://127.0.0.1:5000/api/v2/users", json={
    "name": "Nazar",
    "surname": "Paketik",
    "age": "16",
    "address": "Гайдара 6",
    "email": "slameryt4@gmail.com",
    "position": "IT-Engineer",
    "speciality": "Web programming",
    "hashed_password": "test1"
}).json())

# Правильный запрос
print(post("http://127.0.0.1:5000/api/v2/users", json={
    "name": "Nazar",
    "surname": "Paketik",
    "age": 16,
    "address": "Гайдара 6",
    "email": "slameryt4@gmail.com",
    "position": "IT-Engineer",
    "speciality": "Web programming",
    "hashed_password": "test1"
}).json())

# Правильный запрос
print(delete("http://127.0.0.1:5000/api/v2/users/5").json())

# Не существующий такого id
print(delete("http://127.0.0.1:5000/api/v2/users/5324234").json())