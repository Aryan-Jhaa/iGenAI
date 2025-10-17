#HTTP
from fastapi import FastAPI

#1 Lets make a fastAPI app

app = FastAPI(title="Calculator API")

@app.post("/multiply")

def multiply(a: float, b: float)-> float:
    """
    args: a(float): the first number
          b(float): the second number
    
    returns float

    """
    return a*b
