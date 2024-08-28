from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='teste',
        password='teste!',
        database='portfolio'
    )
    return connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contatos (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        mensagem TEXT NOT NULL
                    )''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)", (nome, email, mensagem))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('contato') + '?success=1')

    return render_template('contato.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
