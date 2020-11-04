from flask import Flask, render_template #追加

app = Flask(__name__, static_folder='frontend/build/static', template_folder='frontend/build')

@app.route('/')
def hello():
    return render_template('index.html')

## おまじない
if __name__ == "__main__":
    app.run()