from flask import Flask, request, render_template, redirect
from stories import Story

app = Flask(__name__)
app.config['TESTING'] = True


if __name__ == '__main__':
    app.run




@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/form', methods=['POST'])
def show_form():
    num = request.form['story_number']
    return redirect('/form/num')


@app.route('/submitted')
def submitted():
    text = story.generate(request.args)
    return render_template('submitted.html', text=text)






















