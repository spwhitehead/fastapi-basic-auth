from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login") # '/login' can be anything, so long as it matches the tokenUrl in the OAuth2PasswordBearer
async def get_token(request_form: OAuth2PasswordRequestForm = Depends()): # Dependency injection
    print(request_form)
    allowed_users = ["ryan", "chris", "bob"]
    if request_form.username not in allowed_users:
        return {"error": "User not found"}
    print(request_form.username)
    print(request_form.password)
    return{"access_token": "token123", "token_type": "bearer"}


@app.get("/test")
async def get_something(token: str = Depends(oauth_scheme)):
    return {"message": "It's..... ALIVE!!!!!!", "token": token}
