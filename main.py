from flask import Flask
from idom import component,html
from idom.backend.flask import configure

@component
def Hellotest():
    return html.h1(
        "test tes"
    )
app=Flask(__name__)
configure(app,Hellotest)