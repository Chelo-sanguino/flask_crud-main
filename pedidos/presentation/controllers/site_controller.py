from flask import render_template
from pedidos import app

@app.route('/')
def site_index():
    return render_template('site/index.html', title='Almacén')