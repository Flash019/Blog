from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app= FastAPI() #instence ---> app


# path operation decorater @app.get('/blog') # get is a operation 
def index(limit=10,published: bool=True,sort: Optional[str] = None): # Path operation function 
    # only get 10 published blog
    
    if published:
        return {'data': f'{limit} published blog from the db '} #dictionary
    else: 
        return {'data':f'{limit} blog list'}
@app.get('/blog/unpublishedblog')

def unpublishedblog():
    return {'data':'A blog (a truncation of "weblog")[1] is an informational website consisting of discrete, often informal diary-style text entries also known as posts. Posts are typically displayed in reverse chronological order so that the most recent post appears first, at the top of the web page. In the 2000s, blogs were often the work of a single individual, occasionally of a small group, and often covered a single subject or topic. In the 2010s, multi-author blogs (MABs) emerged, featuring the writing of multiple authors and sometimes professionally edited. MABs from newspapers, other media outlets, universities, think tanks, advocacy groups, and similar institutions account for an increasing quantity of blog traffic. The rise of Twitter and other "microblogging" systems helps integrate MABs and single-author blogs into the news media. Blog can also be used as a verb, meaning to maintain or add content to a blog.'}

@app.get('/blog/{id}')
def show(id:int): 
    #fetch blog with id = id 
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    

    #fetch comments of blog with id = id 
    return {'data':{'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')

def create_blog(blog: Blog):
    
    return{'data':f"blog is created with {blog.title}"}




#if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1", port=9000)  # to run in local host 9000  ----> in bash -----> python main.py
