from flask import Blueprint, render_template, request, redirect, session, url_for
from database.db import conectar_db
from database import get_connection
import bcrypt

auth_bp = Blueprint('auth', __name__)

from flask import render_template, session, redirect, url_for
from database import get_connection

@auth.route('/admin')
def admin():
    if 'usuario' not in session:
        return redirect(url_for('auth.login'))

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, usuario FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('admin.html', usuarios=usuarios)


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


