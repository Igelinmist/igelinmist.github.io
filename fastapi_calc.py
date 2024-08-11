from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class Operands(BaseModel):
    a: float
    b: float

class Expression(BaseModel):
    a: float
    b: float
    operation: str

app = FastAPI()

@app.post("/calc_sum")
def get_model(item:Operands):
    return {"operation": f"{item.a} + {item.b}", "result": item.a + item.b}

@app.post("/calc_minus")
def get_model(item:Operands):
    return {"operation": f"{item.a} - {item.b}", "result": item.a - item.b}

@app.post("/calc_mult")
def get_model(item:Operands):
    return {"operation": f"{item.a} * {item.b}", "result": item.a * item.b}

@app.post("/calc_div")
def get_model(item:Operands):
    if item.b == 0.:
        return {"operation": f"{item.a} / {item.b}", "result": "error: division by zero"}
    return {"operation": f"{item.a} / {item.b}", "result": item.a / item.b}

@app.post("/calculate")
def get_model(item:Expression):
    operation = f"{item.a} {item.operation} {item.b}"
    match item.operation:
        case "+":
            return {"operation": operation, "result": item.a + item.b}
        case "-":
            return {"operation": operation, "result": item.a - item.b}
        case "*":
            return {"operation": operation, "result": item.a * item.b}
        case "/":
            if item.b == 0.:
                return {"operation": operation, "result": "error: division by zero"}
            else:
                return {"operation": operation, "result": item.a / item.b}
        case _:
            return {"operation": operation, "result": "error: unknown operation"}
