from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a model for the input
class Operation(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
def calculate(operation: Operation):
    if operation.operation == "add":
        result = operation.num1 + operation.num2
    elif operation.operation == "subtract":
        result = operation.num1 - operation.num2
    elif operation.operation == "multiply":
        result = operation.num1 * operation.num2
    elif operation.operation == "divide":
        if operation.num2 != 0:
            result = operation.num1 / operation.num2
        else:
            return {"error": "Division by zero"}
    else:
        return {"error": "Invalid operation"}
    
    return {"result": result}
