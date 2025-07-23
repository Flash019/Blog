from fastapi import FastAPI ,Depends, status, Response , HTTPException,APIRouter
from blog import schemas,  database, models ,oaut2
from typing import List
from sqlalchemy.orm import Session
get_db=database.get_db
from blog.repository import blog

router =APIRouter(
    prefix="/blog",
    tags=['Blog']
)

@router.get('/',response_model=List[schemas.ShowBlog] )

def all(db : Session =Depends(database.get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db : Session =Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.create(db, request)



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Blog, db:Session =Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id:int, db:Session =Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.show(id,)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blog'])
def destroy(id:int, db:Session=Depends(get_db),current_user:schemas.User = Depends(oaut2.get_current_user)):
    return blog.destroy(id,db)