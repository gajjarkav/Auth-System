from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import crud, schemas, models
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from ratelimitor import rate_limiter

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= 'authentication system',
    description= 'a basic authentication system using fastapi',
    version='1.0.0'
)

# Jinja2 templates setup/connection
templates = Jinja2Templates(directory="app/templates")

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get('/register', response_class=HTMLResponse)
def register_get(request:Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post('/register', response_model=schemas.UserRead, response_class=HTMLResponse)
@rate_limiter(max_requests=5, period=60)  # Limit to 5 requests per minute
def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email):
        return templates.TemplateResponse("register.html", {"request": request, "error": "Email already exists"})
    if crud.get_user_by_username(db, username):
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username already exists"})
    
    crud.create_user(db, schemas.UserCreate(username=username, email=email, password=password))
    return RedirectResponse(url="/login", status_code=303)



@app.get('/login', response_class=HTMLResponse)
def login(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post('/login', response_class=HTMLResponse)
@rate_limiter(max_requests=5, period=60)
def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(db, email)
    if not db_user or not crud.verify_password(password, db_user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})
    
    return templates.TemplateResponse("base.html", {"request": request, "message": f"Welcome {db_user.username}!"})
