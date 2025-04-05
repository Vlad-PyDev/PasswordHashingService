from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher = Fernet(key)
passwords = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/passwords', methods=['GET', 'POST'])
def store_password():
    encrypted_password = None
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        encrypted = cipher.encrypt(password.encode()).decode()
        passwords.append({'login': login, 'encrypted': encrypted})
        encrypted_password = encrypted
    return render_template('main.html', encrypted=encrypted_password, passwords=passwords)


if __name__ == '__main__':
    app.run(debug=True)