import cpf
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Funcionario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, cadastre-se'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/funcionarios')
@login_required
def funcionarios():
    funcionarios_sql = select(Funcionario)
    funcionarios_resultado = db_session.execute(funcionarios_sql).scalars().all()

    return render_template("funcionarios.html", lista_funcionarios=funcionarios_resultado)


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        # passo 1
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            flash("Subtração realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            flash("Multiplicação realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            flash("Divisão realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("operacoes.html")

@app.route('/triangulo_perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro = n1 + n1 + n1
            flash("Perímetro realizado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro=perimetro)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")

@app.route('/triangulo_area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area = (n1 * n1) / 2
            flash("Área realizada", "alert-success")
            return render_template("geometria.html", n1=n1, area=area)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")


@app.route('/circulo_perimetro', methods=['GET', 'POST'])
def circulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro2 = 2 * 3,14 * n1
            flash("Perímetro realizado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro2=perimetro2)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")

@app.route('/circulo_area', methods=['GET', 'POST'])
def circulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area2 = 3,14 * n1 ** 2
            flash("Área realizada", "alert-success")
            return render_template("geometria.html", n1=n1, area2=area2)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")

@app.route('/quadrado_perimetro', methods=['GET', 'POST'])
def quadrado_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro3 = n1 + n1 + n1 + n1
            flash("Perímetro realizado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro3=perimetro3)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")

@app.route('/quadrado_area', methods=['GET', 'POST'])
def quadrado_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area3 = n1 * n1
            flash("Área realizada", "alert-success")
            return render_template("geometria.html", n1=n1, area3=area3)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")

@app.route('/hexagono_perimetro', methods=['GET', 'POST'])
def hexagono_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro4 = n1 + n1 + n1 + n1 + n1 + n1
            flash("Perímetro realizado", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro4=perimetro4)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")

@app.route('/hexagono_area', methods=['GET', 'POST'])
def hexagono_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area4 = ((n1 * n1) / 2) * 6
            flash("Área realizada", "alert-success")
            return render_template("geometria.html", n1=n1, area4=area4)
        else:
            flash("Preencha todos os campos.", "alert-danger")

    return render_template("geometria.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form.get('form-cpf')
        senha = request.form.get('form-senha')

        if cpf and senha:
            verificar_cpf = select(Funcionario).where(Funcionario.cpf == cpf)
            resultado_cpf = db_session.execute(verificar_cpf).scalar_one_or_none()
            if resultado_cpf:
                # se encontrado na base de dados
                if resultado_cpf.check_password(senha):
                    # login correto
                    login_user(resultado_cpf)
                    flash(f'Logado com sucesso!', 'success')
                    return redirect(url_for('home'))
                else:
                    # login incorreto
                    flash('Senha incorreta!', 'alert-danger')
                    return render_template('login.html')
            else:
                # se nao encontrado na base de dados
                flash(f'CPF não encontrado!', 'alert-danger')
                return render_template('login.html')
    print(f'funcionario:{current_user}')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('home'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        nascimento = request.form.get('form-nascimento')
        cpf = request.form.get('form-cpf')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = request.form.get('form-salario')

        if not nome or not nascimento or not cpf or not email or not senha or not cargo or not salario:
            flash('Preencher todos os campos!', 'alert-danger')
            return render_template('login.html')

        verificar_cpf = select(Funcionario).where(Funcionario.cpf == cpf)
        existe_cpf = db_session.execute(verificar_cpf).scalar_one_or_none()

        if existe_cpf:
            flash(f'CPF {cpf} já está cadastrado!', 'alert-danger')
            return render_template('login.html')
        try:
            novo_funcionario = Funcionario(nome=nome, data_nascimento=nascimento, cpf=cpf, email=email, senha=senha,
                                           cargo=cargo, salario=float(salario))
            novo_funcionario.set_password(senha)
            db_session.add(novo_funcionario)
            db_session.commit()
            flash(f'Funcionário {nome} cadastrado com sucesso!', 'success')
            return redirect(url_for('funcionarios'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar funcionário', 'alert-danger')
            print(f'Erro na base de dados {e}')
            return redirect(url_for('funcionarios'))
        except Exception as e:
            flash(f'Erro ao cadastrar usuário', 'alert-danger')
            print(f'Erro ao cadastrar {e}')
            return redirect(url_for('funcionarios'))
    return render_template('funcionarios.html')

@app.route('/animais')
def animais():
    return render_template('animais.html')

if __name__ == '__main__':
    app.run(debug=True)
