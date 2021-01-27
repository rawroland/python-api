from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    greeting: str


@app.get('/', response_model=Message)
async def root(name: str):
    """Root path as an example for fastapi which greets people by their name.

    Pydantic is used to define the response model and uvicorn is used as a simple server.

    Args:
        name: Name

    Returns:
        An object with the property greeting.
    """
    return {
        "greeting": f'Hello {name}!'
    }


uvicorn.run(app, host="127.0.0.1", port=5000)
