from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

# ==============================
# CONFIGURAÇÃO DO BANCO
# ==============================

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "catequese_db"),
    "port": int(os.getenv("DB_PORT", 3306))
}


def conectar_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        ssl_disabled=False
    )

# ==============================
# ROTA PRINCIPAL
# ==============================

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        nome = request.form.get('nome')
        data_nascimento = request.form.get('data_nascimento') or None
        idade = request.form.get('idade') or None
        idade = int(idade) if idade else None
        sexo = request.form.get('sexo')
        serie = request.form.get('serie')
        turma = request.form.get('turma')
        email = request.form.get('email')
        celular = request.form.get('celular')
        whatsapp = request.form.get('whatsapp')
        mae = request.form.get('mae')
        pai = request.form.get('pai')
        responsavel = request.form.get('responsavel')
        participa_paroquia = request.form.get('participa_paroquia')
        qual_paroquia = request.form.get('qual_paroquia')
        batizado = request.form.get('batizado')
        nome_responsavel_termo = request.form.get('nome_responsavel_termo')
        data_preenchimento = request.form.get('data_preenchimento') or None


        conexao = conectar_db()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO inscricoes (
            nome, data_nascimento, idade, sexo, serie, turma,
            email, celular, whatsapp, mae, pai, responsavel,
            participa_paroquia, qual_paroquia, batizado,
            nome_responsavel_termo, data_preenchimento
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome, data_nascimento, idade, sexo, serie, turma,
            email, celular, whatsapp, mae, pai, responsavel,
            participa_paroquia, qual_paroquia, batizado,
            nome_responsavel_termo, data_preenchimento
        )

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return "<h3>Inscrição salva com sucesso!</h3>"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)








