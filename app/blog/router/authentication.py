from fastapi import APIRouter ,Depends ,HTTPException , status
from sqlalchemy.orm import Session 
from blog import schemas, database, models, token
from fastapi.security import OAuth2PasswordRequestForm

from blog.hashing import Hash
router =APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user =db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Invaild Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Incorrect Password")
    
    #generate a JWT token and return
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    
    return user

