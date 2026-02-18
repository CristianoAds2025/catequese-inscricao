from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        nome = request.form.get('nome')
        email = request.form.get('email')

        documentos = request.files.get('documentos')
        foto = request.files.get('foto')

        if documentos:
            documentos.save(os.path.join(app.config['UPLOAD_FOLDER'], documentos.filename))

        if foto:
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto.filename))

        print(f"Nova inscrição recebida: {nome} - {email}")

        return "<h3>Inscrição enviada com sucesso!</h3>"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
