from flask import Flask
from flask import redirect
from config import Config
from auth.routes import auth_bp
from admin.routes import admin_bp

@app.route('/')
def home():
    return redirect('/login')

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run()









