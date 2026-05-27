from flask import Flask, request, render_template

from datetime import datetime

from database import (

    criar_tabelas,

    cadastrar_aluno,

    listar_alunos,

    buscar_aluno_por_matricula,

    verificar_ultimo_acesso,

    registrar_acesso,

    verificar_presenca_dia,

    registrar_presenca,

    gerar_relatorio_acessos,

    gerar_relatorio_presencas

)

app = Flask(__name__)

# =========================================
# CRIAR TABELAS
# =========================================

criar_tabelas()

# =========================================
# PÁGINA INICIAL
# =========================================

@app.route("/")
def inicio():

    return render_template("index.html")

# =========================================
# CADASTRAR ALUNO
# =========================================

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    mensagem = ""

    if request.method == "POST":

        nome = request.form.get("nome")

        idade = request.form.get("idade")

        turma = request.form.get("turma")

        matricula = request.form.get("matricula")

        cadastrar_aluno(
            nome,
            idade,
            turma,
            matricula
        )

        mensagem = "Aluno cadastrado com sucesso!"

    return render_template(
        "cadastro.html",
        mensagem=mensagem
    )

# =========================================
# LISTAR ALUNOS
# =========================================

@app.route("/alunos")
def alunos():

    lista_alunos = listar_alunos()

    return render_template(
        "alunos.html",
        alunos=lista_alunos
    )

# =========================================
# REGISTRAR ACESSO
# =========================================

@app.route("/acesso", methods=["GET", "POST"])
def acesso():

    mensagem = ""

    if request.method == "POST":

        matricula = request.form.get(
            "matricula"
        )

        aluno = buscar_aluno_por_matricula(
            matricula
        )

        if aluno:

            aluno_id = aluno[0]

            nome = aluno[1]

            horario = datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            data = datetime.now().strftime(
                "%d/%m/%Y"
            )

            # =================================
            # VERIFICAR ÚLTIMO ACESSO
            # =================================

            ultimo_acesso = verificar_ultimo_acesso(
                aluno_id
            )

            # =================================
            # DEFINIR ENTRADA OU SAÍDA
            # =================================

            if ultimo_acesso:

                ultimo_tipo = ultimo_acesso[0]

                if ultimo_tipo == "entrada":

                    tipo = "saida"

                else:

                    tipo = "entrada"

            else:

                tipo = "entrada"

            # =================================
            # REGISTRAR ACESSO
            # =================================

            registrar_acesso(
                aluno_id,
                tipo,
                horario
            )

            # =================================
            # REGISTRAR PRESENÇA
            # =================================

            presenca_hoje = verificar_presenca_dia(
                aluno_id,
                data
            )

            if not presenca_hoje and tipo == "entrada":

                registrar_presenca(
                    aluno_id,
                    data
                )

            mensagem = (
                f"{nome} registrou {tipo} às {horario}"
            )

        else:

            mensagem = "Aluno não encontrado"

    return render_template(
        "acesso.html",
        mensagem=mensagem
    )

# =========================================
# RELATÓRIO DE ACESSOS
# =========================================

@app.route("/relatorio-acessos")
def relatorio_acessos():

    relatorio = gerar_relatorio_acessos()

    return render_template(
        "relatorio_acessos.html",
        relatorio=relatorio
    )

# =========================================
# RELATÓRIO DE PRESENÇAS
# =========================================

@app.route("/relatorio-presencas")
def relatorio_presencas():

    relatorio = gerar_relatorio_presencas()

    return render_template(
        "relatorio_presencas.html",
        relatorio=relatorio
    )

# =========================================
# INICIAR SERVIDOR
# =========================================

app.run(debug=True)