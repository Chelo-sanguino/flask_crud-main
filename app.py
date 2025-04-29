from flask import Flask
from pedidos import app as pedidos_app

app = pedidos_app

if __name__ == "__main__":
    app.run()

