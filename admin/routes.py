from flask import Blueprint, render_template, session, redirect
from database.db import conectar_db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def painel():
    if 'usuario' not in session:
        return redirect('/login')

    conexao = conectar_db()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inscricoes ORDER BY id DESC")
    dados = cursor.fetchall()

    return render_template('admin.html', dados=dados)

