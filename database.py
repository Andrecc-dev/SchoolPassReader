import sqlite3

# =========================================
# CONEXÃO
# =========================================

def conectar_banco():

    return sqlite3.connect("escola.db")

# =========================================
# CRIAR TABELAS
# =========================================

def criar_tabelas():

    conexao = conectar_banco()

    cursor = conexao.cursor()

    # =====================================
    # TABELA ALUNOS
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nome TEXT NOT NULL,

        idade INTEGER NOT NULL,

        turma TEXT NOT NULL,

        matricula TEXT UNIQUE NOT NULL

    )
    """)

    # =====================================
    # TABELA ACESSOS
    # ENTRADA / SAÍDA
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS acessos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        aluno_id INTEGER NOT NULL,

        tipo TEXT NOT NULL,

        horario TEXT NOT NULL,

        FOREIGN KEY(aluno_id)
        REFERENCES alunos(id)

    )
    """)

    # =====================================
    # TABELA PRESENÇAS
    # CHAMADA ESCOLAR
    # =====================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS presencas (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        aluno_id INTEGER NOT NULL,

        data TEXT NOT NULL,

        presente INTEGER NOT NULL,

        FOREIGN KEY(aluno_id)
        REFERENCES alunos(id)

    )
    """)

    conexao.commit()

    conexao.close()

# =========================================
# CADASTRAR ALUNO
# =========================================

def cadastrar_aluno(
    nome,
    idade,
    turma,
    matricula
):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    try:

        cursor.execute("""
        INSERT INTO alunos (

            nome,
            idade,
            turma,
            matricula

        )

        VALUES (?, ?, ?, ?)
        """, (

            nome,
            idade,
            turma,
            matricula

        ))

        conexao.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conexao.close()

# =========================================
# LISTAR ALUNOS
# =========================================

def listar_alunos(busca=None):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    # =====================================
    # SE TIVER PESQUISA
    # =====================================

    if busca:

        cursor.execute("""

        SELECT

            id,

            nome,

            idade,

            turma,

            matricula

        FROM alunos

        WHERE nome LIKE ?
        OR matricula LIKE ?
        OR turma LIKE ?

        """, (

            f"%{busca}%",

            f"%{busca}%",

            f"%{busca}%"

        ))

    # =====================================
    # SEM PESQUISA
    # =====================================

    else:

        cursor.execute("""

        SELECT

            id,

            nome,

            idade,

            turma,

            matricula

        FROM alunos

        """)

    alunos = cursor.fetchall()

    conexao.close()

    return alunos

# =========================================
# BUSCAR ALUNO POR MATRÍCULA
# =========================================

def buscar_aluno_por_matricula(
    matricula
):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT

        id,
        nome

    FROM alunos

    WHERE matricula = ?
    """, (matricula,))

    aluno = cursor.fetchone()

    conexao.close()

    return aluno

# =========================================
# BUSCAR ALUNO POR NOME
# =========================================

def buscar_aluno_por_nome(nome):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT

        id,
        nome

    FROM alunos

    WHERE nome = ?
    """, (nome,))

    aluno = cursor.fetchone()

    conexao.close()

    return aluno

# =========================================
# VERIFICAR ÚLTIMO ACESSO
# =========================================

def verificar_ultimo_acesso(
    aluno_id
):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT tipo

    FROM acessos

    WHERE aluno_id = ?

    ORDER BY id DESC

    LIMIT 1
    """, (aluno_id,))

    ultimo = cursor.fetchone()

    conexao.close()

    return ultimo

# =========================================
# REGISTRAR ACESSO
# =========================================

def registrar_acesso(
    aluno_id,
    tipo,
    horario
):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO acessos (

        aluno_id,
        tipo,
        horario

    )

    VALUES (?, ?, ?)
    """, (
        aluno_id,
        tipo,
        horario
    ))

    conexao.commit()

    conexao.close()

# =========================================
# VERIFICAR PRESENÇA DO DIA
# =========================================

def verificar_presenca_dia(
    aluno_id,
    data
):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *

    FROM presencas

    WHERE aluno_id = ?
    AND data = ?
    """, (
        aluno_id,
        data
    ))

    presenca = cursor.fetchone()

    conexao.close()

    return presenca

# =========================================
# REGISTRAR PRESENÇA
# =========================================

def registrar_presenca(
    aluno_id,
    data
):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO presencas (

        aluno_id,
        data,
        presente

    )

    VALUES (?, ?, ?)
    """, (
        aluno_id,
        data,
        1
    ))

    conexao.commit()

    conexao.close()

# =========================================
# RELATÓRIO DE ACESSOS
# =========================================

def gerar_relatorio_acessos(busca=None):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    # =====================================
    # COM PESQUISA
    # =====================================

    if busca:

        cursor.execute("""

        SELECT

            alunos.nome,

            alunos.turma,

            alunos.matricula,

            acessos.tipo,

            acessos.horario

        FROM acessos

        JOIN alunos

        ON alunos.id = acessos.aluno_id

        WHERE alunos.nome LIKE ?
        OR alunos.matricula LIKE ?
        OR alunos.turma LIKE ?
        OR acessos.tipo LIKE ?

        ORDER BY acessos.horario DESC

        """, (

            f"%{busca}%",

            f"%{busca}%",

            f"%{busca}%",

            f"%{busca}%"

        ))

    # =====================================
    # SEM PESQUISA
    # =====================================

    else:

        cursor.execute("""

        SELECT

            alunos.nome,

            alunos.turma,

            alunos.matricula,

            acessos.tipo,

            acessos.horario

        FROM acessos

        JOIN alunos

        ON alunos.id = acessos.aluno_id

        ORDER BY acessos.horario DESC

        """)

    relatorio = cursor.fetchall()

    conexao.close()

    return relatorio

# =========================================
# RELATÓRIO DE PRESENÇAS
# =========================================

def gerar_relatorio_presencas(busca=None):

    conexao = conectar_banco()

    cursor = conexao.cursor()

    # =====================================
    # COM PESQUISA
    # =====================================

    if busca:

        cursor.execute("""

        SELECT

            alunos.nome,

            alunos.turma,

            alunos.matricula,

            presencas.data,

            presencas.presente

        FROM presencas

        JOIN alunos

        ON alunos.id = presencas.aluno_id

        WHERE alunos.nome LIKE ?
        OR alunos.matricula LIKE ?
        OR alunos.turma LIKE ?

        ORDER BY presencas.data DESC

        """, (

            f"%{busca}%",

            f"%{busca}%",

            f"%{busca}%"

        ))

    # =====================================
    # SEM PESQUISA
    # =====================================

    else:

        cursor.execute("""

        SELECT

            alunos.nome,

            alunos.turma,

            alunos.matricula,

            presencas.data,

            presencas.presente

        FROM presencas

        JOIN alunos

        ON alunos.id = presencas.aluno_id

        ORDER BY presencas.data DESC

        """)

    relatorio = cursor.fetchall()

    conexao.close()

    return relatorio