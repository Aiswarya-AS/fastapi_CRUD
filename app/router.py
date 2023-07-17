from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import BookSchema, RequestBook, Response
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response[str](status="ok", code="200", message="Book created successfully", result=None).dict(
        exclude_none=True
    )


@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _book = crud.get_book_by_id(db, id)
    return Response(
        status="ok", code="200", message="Success get data", result=_book
    ).dict(exclude_none=True)


@router.get("/")
async def get_books(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(
        status="ok", code="200", message="Sucessfully fetched data", result=_books
    )


@router.patch("/{id}")
async def update_book(id: int, request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(
        db,
        book_id=request.parameter.id,  # type: ignore
        title=request.parameter.title,  # type: ignore
        description=request.parameter.description,  # type: ignore
    )
    return Response(
        status="Ok", code="200", message="Success update data", result=_book
    )


@router.delete("/{id}")
async def delete_book(id: int, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=id)
    return Response[str](status="Ok", code="200", message="Success delete data").dict(
        exclude_none=None
    )
