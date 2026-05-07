# Import
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')

        return render_template(
            'index.html',
            button_python=button_python,
            button_discord=button_discord,
            button_html=button_html,
            button_db=button_db
        )

    return render_template('index.html')


@app.route('/egitim')
def egitim():
    return render_template('egitim.html')

@app.route('/dogum')
def dogum():
    return render_template('dogum.html')

@app.route('/eserler')
def eserler():
    return render_template('eserler.html')

@app.route('/siyasi')
def siyasi():
    return render_template('siyasi.html')

@app.route('/fiziksel')
def fiziksel():
    return render_template('fiziksel.html')

@app.route('/ogretmenlik')
def ogretmenlik():
    return render_template('ogretmenlik.html')

@app.route('/anasayfa')
def anasayfa():
    return render_template('index.html')

@app.route('/kaynakca')
def kaynakca():
    return render_template('kaynakca.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)