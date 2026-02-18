from flask import Blueprint, render_template, request, redirect, session
from database.db import conectar_db
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        usuario = request.form['usuario']
        senha_digitada = request.form['senha'].encode()

        conexao = conectar_db()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s", (usuario,))
        user = cursor.fetchone()

        cursor.close()
        conexao.close()

        if user and bcrypt.checkpw(senha_digitada, user['senha'].encode()):
            session['usuario'] = user['usuario']
            return redirect('/admin')
        else:
            return "Usuário ou senha inválidos"

    return render_template('login.html')


