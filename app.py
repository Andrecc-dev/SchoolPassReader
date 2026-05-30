from flask import Flask, request, render_template
from datetime import datetime
import os  # Adicionado para ler a porta do servidor em nuvem

from database import (
    criar_tabelas,
    cadastrar_aluno,
    listar_alunos,
    buscar_aluno_por_matricula,
    buscar_aluno_por_nome,
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
# CADASTRO DE ALUNOS
# =========================================
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    mensagem = ""

    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        turma = request.form.get("turma")
        matricula = request.form.get("matricula")

        # =====================================
        # VALIDAR MATRÍCULA
        # =====================================
        if not matricula.isdigit():
            mensagem = "A matrícula deve conter apenas números!"
            return render_template("cadastro.html", mensagem=mensagem)

        # =====================================
        # VALIDAR IDADE
        # =====================================
        if not idade.isdigit():
            mensagem = "A idade deve conter apenas números!"
            return render_template("cadastro.html", mensagem=mensagem)

        # =====================================
        # CADASTRAR ALUNO
        # =====================================
        resultado = cadastrar_aluno(nome, idade, turma, matricula)

        # =====================================
        # VERIFICAR RESULTADO
        # =====================================
        if resultado:
            mensagem = "Aluno cadastrado com sucesso!"
        else:
            mensagem = "Matrícula já cadastrada!"

    return render_template("cadastro.html", mensagem=mensagem)

# =========================================
# LISTAR ALUNOS
# =========================================
@app.route("/alunos")
def alunos():
    busca = request.args.get("busca")
    lista_alunos = listar_alunos(busca)
    return render_template("alunos.html", alunos=lista_alunos)

# =========================================
# REGISTRAR ACESSO
# =========================================
@app.route("/acesso", methods=["GET", "POST"])
def acesso():
    mensagem = ""

    if request.method == "POST":
        tipo_busca = request.form.get("tipo_busca")
        valor = request.form.get("valor")

        # =================================
        # BUSCAR POR MATRÍCULA
        # =================================
        if tipo_busca == "matricula":
            aluno = buscar_aluno_por_matricula(valor)
        # =================================
        # BUSCAR POR NOME
        # =================================
        else:
            aluno = buscar_aluno_por_nome(valor)

        # =================================
        # VERIFICAR ALUNO
        # =================================
        if aluno:
            aluno_id = aluno[0]
            nome = aluno[1]
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            data = datetime.now().strftime("%d/%m/%Y")

            # =================================
            # VERIFICAR ÚLTIMO ACESSO
            # =================================
            ultimo_acesso = verificar_ultimo_acesso(aluno_id)

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
            registrar_acesso(aluno_id, tipo, horario)

            # =================================
            # REGISTRAR PRESENÇA
            # =================================
            presenca_hoje = verificar_presenca_dia(aluno_id, data)

            if not presenca_hoje and tipo == "entrada":
                registrar_presenca(aluno_id, data)

            mensagem = f"{nome} registrou {tipo} às {horario}"
        else:
            mensagem = "Aluno não encontrado!"

    return render_template("acesso.html", mensagem=mensagem)

# =========================================
# RELATÓRIO DE ACESSOS
# =========================================
@app.route("/relatorio-acessos")
def relatorio_acessos():
    busca = request.args.get("busca")
    relatorio = gerar_relatorio_acessos(busca)
    return render_template("relatorio_acessos.html", relatorio=relatorio)

# =========================================
# RELATÓRIO DE PRESENÇAS
# =========================================
@app.route("/relatorio-presencas")
def relatorio_presencas():
    busca = request.args.get("busca")
    relatorio = gerar_relatorio_presencas(busca)
    return render_template("relatorio_presencas.html", relatorio=relatorio)

# =========================================
# INICIAR SERVIDOR (CONFIGURADO PARA DEPLOY)
# =========================================
if __name__ == '__main__':
    # Captura a porta do ambiente web, caso contrário usa a 5000 localmente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)