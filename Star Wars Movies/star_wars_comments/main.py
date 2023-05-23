import os
from database import *

try:
    import uvicorn
    from fastapi import FastAPI, status
    from pydantic import BaseModel
    from fastapi.encoders import jsonable_encoder
    from fastapi.middleware.cors import CORSMiddleware

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')

finally:
    os.system('cls')
    app = FastAPI()

    class Item(BaseModel):
        username: str
        comment: str
        stars_rating: int

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/read/{id_movie}", status_code=status.HTTP_200_OK)
    async def root(id_movie: int):
        """
            Ler e receber o banco de dados e inserir na API.

            ...

            ARGs
            ----------
            id_movie : int

            RETURN
            ----------
            body : (tuple)
        """

        create_db(id_movie)

        id_movie_rec = id_movie

        return {
            "body": read_comment(id_movie_rec)
        }

    @app.post('/api/comment/{id_movie}', status_code=status.HTTP_201_CREATED)
    async def api_create_comment(item: Item, id_movie: int):
        """
            Criar um novo comentário.

            ...
            
            ARGs
            ----------
            item : JSON - stringify
                    `-> Documento stringify(comment)

            id_movie: int

            RETURN
            ----------
            RESPONSE : (str)
            NEW_COMMENT : (json)
        """

        json_item = jsonable_encoder(item)

        create_comment(json_item, id_movie)

        return {
            "RESPONSE": movie_id_convert(id_movie),
            "NEW_COMMENT": item
        }

    if __name__ == '__main__':
        uvicorn.run("main:app", host='127.0.0.1', reload=True)