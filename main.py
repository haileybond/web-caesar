from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = '''
<!DOCTYPE HTML>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px; sans-serif;
                border-radius: 10px;
            }}
            text-area {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method='post'>
            <label for="rotate">
            Rotate by:
            <input type="text" id="rotate" name="rot" value="0"/>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
'''

@app.route("/", methods=['post'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text'] 
    encrypted_text = rotate_string(text, rot)
    return form.format(encrypted_text)

@app.route("/")
def index():
    return form.format('')

app.run()