# INSTALACIÓN
conda create --prefix ./env python
conda activate 
pip install flask
pip install "psycopg[binary,pool]"

# Ejecución en modo desarrollo
conda activate ./env
flask --app app run
