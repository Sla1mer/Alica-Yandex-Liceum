from requests import post, get, delete

# Правильный запрос
print(get("http://127.0.0.1:5000/api/v2/jobs").json())

# Правильный запрос
print(get("http://127.0.0.1:5000/api/v2/jobs/5").json())

# Не существует такого id
print(get("http://127.0.0.1:5000/api/v2/jobs/12312312").json())

# id тип данных Integer, а передаём String
print(get("http://127.0.0.1:5000/api/v2/jobs/asdas").json())

# id в БД такой уже имеется
print(post("http://127.0.0.1:5000/api/v2/jobs", json={
    "id": 1,
    "team_leader": "dasd",
    "job": "dsada",
    "work_size": 12,
    "collaborators": "sada",
    "start_date": "1999-02-13 12:11:02",
    "end_date": "1999-02-13 13:11:02",
    "is_finished": True
}).json())

# work_size имеет тип данных Integer, а передаём String
print(post("http://127.0.0.1:5000/api/v2/jobs", json={
    "id": 1345,
    "team_leader": "dasd",
    "job": "dsada",
    "work_size": "вфы",
    "collaborators": "sada",
    "start_date": "1999-02-13 12:11:02",
    "end_date": "1999-02-13 13:11:02",
    "is_finished": True
}).json())

# is_finished имеет тип данных Boolean, а передаём String
print(post("http://127.0.0.1:5000/api/v2/jobs", json={
    "id": 1321,
    "team_leader": "dasd",
    "job": "dsada",
    "work_size": 12,
    "collaborators": "sada",
    "start_date": "1999-02-13 12:11:02",
    "end_date": "1999-02-13 13:11:02",
    "is_finished": "dsad"
}).json())

# is_finished имеет тип данных Boolean, а передаём String
print(post("http://127.0.0.1:5000/api/v2/jobs", json={
    "id": 1554,
    "team_leader": "dasd",
    "job": "dsada",
    "work_size": 12,
    "collaborators": "sada",
    "start_date": "1999-02-13 12:11:02",
    "end_date": "1999-02-13 13:11:02",
    "is_finished": True
}).json())

# Правильный запрос
print(delete("http://127.0.0.1:5000/api/v2/jobs/5").json())

# Не существует такого id
print(delete("http://127.0.0.1:5000/api/v2/jobs/5324234").json())
