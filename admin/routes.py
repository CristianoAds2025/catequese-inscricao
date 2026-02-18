from flask import Blueprint, render_template, session, redirect
from database.db import conectar_db
import pandas as pd
from flask import send_file
import io

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

@admin_bp.route('/exportar')
def exportar():
    conexao = conectar_db()
    df = pd.read_sql("SELECT * FROM inscricoes", conexao)

    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)

    return send_file(output,
                     download_name="inscricoes.xlsx",
                     as_attachment=True)
