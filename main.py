from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Harry Potter", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 1},
    {"title": "Little", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 2},
    {"title": "Saga", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 3},
    {"title": "Attack", "desc": "smth", "Author": "J.K.Rolling", "price": 150, "id": 4}
]
@app.get("/api/{title}") #Эта секция для получения данных
async def search(title: str):
    for book in BOOKS:
        if book.get("title") == title: # Находим книгу по названию
            return book
    else: # Else вне for из-за своего первого срабатывания, если она будет в нем то программа не сработает
        return "Not found"

@app.delete("/api/{book_name}")
async def delete(book_name: str):# Функция удаления данных
    for book in BOOKS:
        if book.get("title") == book_name:
            a = BOOKS.index(book)
            BOOKS.pop(a)
            return "Successfully deleted."
    else:
        return "Book was not found."
@app.put("/api/{book_name}/{change_to_}/{item_to_change}")
async def change(book_name: str, change_to_: str, item_to_change: str): # Фунция для изменения данных
    for book in BOOKS:
        if book.get("title") == book_name:
            a = book.keys()
            if item_to_change in a:
                book.update({change_to_: item_to_change})
                return "All successfull."
            else:
                return "Parameter to change don't exist."
    else:
        return "Book not found."
@app.post("/api/{title}/{desc}/{Author}/{price}/{id}")
async def new_book(title: str,desc: str, Author: str,price: int,id: int):
    if title != None and desc != None and Author != None and price != None and id != None:
        BOOKS.append({"title": title, "desc": desc, "Author" : Author, "price": price, "id": id})
        return "New book aded successfully."
    else:
        return "Enter the all info in proper format."
