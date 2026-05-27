from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# =========================================
# CONEXÃO COM BANCO
# =========================================

def conectar_banco():
    return sqlite3.connect("escola.db")

# =========================================
# CRIAR TABELAS
# =========================================

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

cursor.execute("""
CREATE TABLE IF NOT EXISTS presencas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER,
    horario TEXT
)
""")

conexao.commit()

conexao.close()

# =========================================
# PÁGINA INICIAL
# =========================================

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

    return render_template("index.html")

# =========================================
# LISTAR ALUNOS
# =========================================

@app.route("/alunos")
def listar_alunos():

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    conexao.close()

    return render_template(
        "alunos.html",
        alunos=alunos
    )

# =========================================
# REGISTRAR PRESENÇA
# =========================================

@app.route("/presenca", methods=["GET", "POST"])
def registrar_presenca():

    mensagem = ""

    if request.method == "POST":

        nome = request.form.get("nome")

        conexao = conectar_banco()

        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM alunos WHERE nome = ?",
            (nome,)
        )

        aluno = cursor.fetchone()

        if aluno:

            horario = datetime.now().strftime("%H:%M:%S")

            cursor.execute("""
            INSERT INTO presencas (aluno_id, horario)
            VALUES (?, ?)
            """, (aluno[0], horario))

            conexao.commit()

            mensagem = f"Presença registrada às {horario}"

        else:

            mensagem = "Aluno não encontrado"

        conexao.close()

    return render_template(
        "presenca.html",
        mensagem=mensagem
    )

# =========================================
# RELATÓRIO
# =========================================

@app.route("/relatorio")
def relatorio():

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT alunos.nome, presencas.horario
    FROM presencas
    JOIN alunos
    ON alunos.id = presencas.aluno_id
    """)

    relatorio = cursor.fetchall()

    conexao.close()

    return render_template(
        "relatorio.html",
        relatorio=relatorio
    )

# =========================================
# INICIAR SERVIDOR
# =========================================

app.run(debug=True)