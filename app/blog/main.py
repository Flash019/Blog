from fastapi import FastAPI 
from blog import models
from blog.database import engine 
from blog.router import blog
from blog.router import user
from blog.router import authentication
app = FastAPI(
)

# This line will create all tables defined in models
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)





