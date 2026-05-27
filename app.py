from flask import Flask, request
import sqlite3

app = Flask(__name__)

def conectar_banco():
    return sqlite3.connect("escola.db")

conexao = conectar_banco()

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    turma TEXT
)
""")

conexao.commit()

conexao.close()

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        nome = request.form.get("nome")
        idade = request.form.get("idade")
        turma = request.form.get("turma")

        conexao = conectar_banco()

        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO alunos (nome, idade, turma)
        VALUES (?, ?, ?)
        """, (nome, idade, turma))

        conexao.commit()

        conexao.close()

        return f"{nome} cadastrado com sucesso!"

    return """
    <h1>Sistema SmartPresence</h1>

    <form method="POST">

        <input type="text" name="nome" placeholder="Digite seu nome">

        <input type="number" name="idade" placeholder="Digite sua idade">

        <input type="text" name="turma" placeholder="Digite sua turma">

        <button type="submit">
            Cadastrar
        </button>

    </form>
    """

@app.route("/alunos")
def listar_alunos():
    conexao = conectar_banco()
    
    cursor = conexao.cursor()
    
    cursor.execute("select*from alunos")
    
    alunos = cursor.fetchall()
    
    conexao.close()
    
    return str(alunos)
app.run(debug=True)