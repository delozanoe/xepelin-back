from fastapi import FastAPI
import http.client
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/send-email/')
def send_email(idOp, tasa, email):
    conn = http.client.HTTPSConnection("hooks.zapier.com")
    payload = json.dumps({
        "idOp": idOp,
        "tasa": tasa,
        "email": email
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/hooks/catch/6872019/oahrt5g/", payload, headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return {"menssage": data.decode("utf-8")}
