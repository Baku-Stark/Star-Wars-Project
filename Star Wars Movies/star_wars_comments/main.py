import os
from db.database import *

try:
    import uvicorn
    from fastapi import FastAPI, status
    from fastapi.middleware.cors import CORSMiddleware
    from pydantic import BaseModel



except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')

finally:
    os.system('cls')
    app = FastAPI()

    class Item(BaseModel):
        username: str
        comment: str
        stars_rating: int

    origins = [
        "http://localhost:8080",
        "http://localhost:8080/api/comment",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", status_code=status.HTTP_200_OK)
    async def root():
        """
            Ler e receber o banco de dados e inserir na API.

            ...

            RETURN
            ----------
            message : (str)
            data : (json)
        """

        return {
            "message": "Hello World",
            "body": read_comment()
        }

    @app.post('/api/comment', status_code=status.HTTP_201_CREATED)
    async def create_comment(item: Item):
        """
            Criar um novo comentário.

            ...

            RETURN
            ----------
            message : (str)
            data : (json)
        """

        return {"RESPONSE": "201 - CREATED", "NEW_ITEM": item}

    if __name__ == '__main__':
        uvicorn.run("main:app", host='127.0.0.1', reload=True)