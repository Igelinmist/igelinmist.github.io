from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# count = 0
# аннотации типов
# класс с типами данных параметров
class Item(BaseModel):
    name: str
    description: str
    price: float

class Expression(BaseModel):
    a: float
    b: float
    operation: str

# создаем объект приложения
app = FastAPI()

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:5000/
@app.get("/")
def root():
    # count += 1
    return {"message": "Hello FastAPI"}

# функция, которая обрабатывает запрос по пути "/about"
@app.get("/about")
def about():
    return {"message": "Страница с описанием проекта"}

# функция-обработчик с параметрами пути
@app.get("/users/{id}")
def users(id):
    return {"user_id": id}

# функция-обработчик post запроса с параметрами
@app.post("/users")
def get_model(item:Item):
    return {"user_name": item.name, "description": item.description, "price": item.price}


@app.post("/calculate")
def get_model(item:Expression):
    description = f"{item.a} {item.operation} {item.b}"
    match item.operation:
        case "+":
            return {"description": description, "result": item.a + item.b}
        case "-":
            return {"description": description, "result": item.a - item.b}
        case "*":
            return {"description": description, "result": item.a * item.b}
        case "/":
            if item.b == 0.:
                return {"description": description, "result": "error: division by zero"}
            else:
                return {"description": description, "result": item.a / item.b}
        case _:
            return {"description": description, "result": "error: unknown operation"}

@app.get("/my_page", response_class=HTMLResponse)
def read_file():
    with open("my_page.html", 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content