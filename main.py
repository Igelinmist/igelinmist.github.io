from fastapi import FastAPI
from chunks import Chunk
from pydantic import BaseModel
import utils

data_from_url= utils.load_document_text('https://docs.google.com/document/d/11MU3SnVbwL_rM-5fIC14Lc3XnbAV4rY1Zd_kpcMuH4Y')

markdown = utils.text_to_markdown(data_from_url)

# инициализация индексной базы
chunk = Chunk(path_to_base="Simble.txt")

# класс с типами данных параметров
class Item(BaseModel):
    text: str

# создаем объект приложения
app = FastAPI()

# функция обработки get запроса + декоратор
@app.get("/")
def read_root():
    return {"message": "answer"}

# функция обработки post запроса + декоратор
@app.post("/api/get_answer")
def get_answer(question: Item):
    answer = chunk.get_answer(query=question.text)
    return {"message": answer}

