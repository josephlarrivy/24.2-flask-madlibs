from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)





@app.route('/')
def form():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/submitted')
def submitted():
    text = story.generate(request.args)
    return render_template('submitted.html', text=text)
























if __name__ == '__main__':
    app.run