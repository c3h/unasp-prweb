from flask import Flask, render_template
from app-back import carregar_acessos

app = Flask(__name__)

a, p, m = carregar_acessos()

@app.route('/')
def home():
  return render_template('home.html', anos=a, max=m, despesa_pessoa=p)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)