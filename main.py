from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Harry Potter", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 1},
    {"title": "Little", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 2},
    {"title": "Saga", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 3},
    {"title": "Attack", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 4}
]
@app.get("/api/{title}")
async def search(title: str):
    for book in BOOKS:
        if book.get("title") == title:
            print(book)
            return book
    else:
        return "Not found"