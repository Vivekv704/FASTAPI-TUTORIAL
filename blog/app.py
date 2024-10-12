from fastapi import FastAPI
from . import schemas

vibes = FastAPI()



@vibes.post('/blog')
def create_blog(blog: schemas.Blog):
   return blog

@vibes.get('/')
def get_blog():
    return {'data': 'blogs'}