from fastapi import FastAPI,Depends, status, Response
from . import schemas, models
from .models import User
from .schemas import UserCreate
from .database import engine, SessionLocal 
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db: Session= Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200)
def show(id,response: Response,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"blog com esse id {id} não existe" }
    return blog

@app.post('/users/')
def create_user(user: UserCreate, db: Session= Depends(get_db)):
    db_user = User(username=user.username,
                name= user.name,
                email=user.email)
    db_user.set_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get('/users/')
def get_users(db: Session= Depends(get_db)):
    users = db.query(models.User).all()
    return users