python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página con Flask</title>
</head>
<body>
    <h1>¡Hola, mundo!</h1>
    <p>Bienvenido a mi primera página web usando Flask.</p>
</body>
</html>

