from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["eduPlatform"]
courses = db["courses"]

courses.delete_many({})

courses_data = [
    {
        "title": "Основы Python",
        "description": "Изучение базовых концепций языка Python с нуля.",
        "category": "Программирование",
        "price": 4990,
        "published": True,
        "created_at": datetime(2023, 6, 10, 10, 0, 0),
        "teacher": {
            "name": "Иван Иванов",
            "email": "ivanov@example.com",
            "experience_years": 5
        },
        "lessons": [
            {"title": "Введение", "duration_min": 15, "video_url": "https://video.example.com/intro"},
            {"title": "Основы", "duration_min": 25, "video_url": "https://video.example.com/basics"}
        ],
        "students": [
            {"name": "Алексей Попов", "email": "alex@example.com", "progress": 60},
            {"name": "Мария Козлова", "email": "maria@example.com", "progress": 100}
        ]
    },
    {
        "title": "Web-разработка с HTML и CSS",
        "description": "Создание адаптивных сайтов с нуля.",
        "category": "Веб-дизайн",
        "price": 4500,
        "published": True,
        "created_at": datetime(2023, 6, 15, 11, 30, 0),
        "teacher": {
            "name": "Анна Смирнова",
            "email": "anna@example.com",
            "experience_years": 3
        },
        "lessons": [
            {"title": "HTML Основы", "duration_min": 20, "video_url": "https://video.example.com/html"},
            {"title": "CSS Основы", "duration_min": 30, "video_url": "https://video.example.com/css"}
        ],
        "students": [
            {"name": "Сергей Иванов", "email": "sergey@example.com", "progress": 40},
            {"name": "Ольга Петрова", "email": "olga@example.com", "progress": 90}
        ]
    }
]

courses.insert_many(courses_data)

print("\n1️⃣ Опубликованные курсы:")
for course in courses.find({"published": True}, {"title": 1, "_id": 0}):
    print("-", course["title"])

print("\n2️⃣ Курсы по программированию с ценой < 5000:")
for course in courses.find({"category": "Программирование", "price": {"$lt": 5000}}, {"title": 1, "price": 1, "_id": 0}):
    print(f"- {course['title']} ({course['price']}₸)")

print("\n3️⃣ Курсы, где есть студент с прогрессом < 50%:")
for course in courses.find({"students.progress": {"$lt": 50}}, {"title": 1, "_id": 0}):
    print("-", course["title"])

print("\n4️⃣ Преподаватели всех курсов:")
for teacher in courses.find({}, {"teacher.name": 1, "_id": 0}):
    print("-", teacher["teacher"]["name"])

client.close()
print("\n✅ Готово!")
