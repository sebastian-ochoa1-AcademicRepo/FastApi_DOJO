from fastapi import APIRouter, status, Response
from models.book_entity import BookEntity, BookEntityUpdate
from repository import book_repository

route = APIRouter(prefix='/book', tags=['books'])

@route.get('', status_code=200)
def get_books(response: Response):

    books = book_repository.get_all_books()

    response.status_code = status.HTTP_200_OK
    return {"message":"Obtenido con exito", "status_code":200, "body": books}


@route.get('/{isbn}', status_code=200)
def get_book_by_isbn(isbn: str, response: Response):

    book = book_repository.get_book_by_isbn(isbn)

    if not book:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":"No encontrado", "status_code":404}
    return {"message":"Libro obtenido con exito", "status_code":200, "body": book}

@route.post('', status_code=200)
def create_book(book: BookEntity, response: Response):
    isbn: str = book.isbn
    book_db = book_repository.get_book_by_isbn(isbn)
    if not book_db:
        book_db = book_repository.create_book(book)
        response.status_code = status.HTTP_201_CREATED
        return {"message": "Libro creado con exito", "status_code": 201, "body": book_db}
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"message": "El libro ya existe, no se ejcutará ninguna acción", "status_code": 400}


@route.put('/{isbn}', status_code=200)
def update_book(isbn: str ,book: BookEntityUpdate, response: Response):
    book_db = book_repository.get_book_by_isbn(isbn)
    if not book_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "El elemento no existe", "status_code": 404}
    book_db = book_repository.update_book(isbn,book)
    return {"message": "Libro actualizado con exito", "status_code": 200, "body": book_db}

@route.delete('/{isbn}', status_code=200)
def delete_book_by_isbn(isbn: str, response: Response):
    book_db = book_repository.delete_book(isbn)
    if not book_db:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "El elemento no existe", "status_code": 404}
    return {"message": "Libro eliminado correctamente", "status_code": 200, "body": book_db}