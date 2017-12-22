from caesar import rotate_string
from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True



form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label>
                Rotate By
                <input type="text" name="rot" value= "0"/>     
            </label>

            <textarea name="text" >{0}</textarea>

            <input type="submit" value="Encrypt It"/>
         </form>

    </body>
</html>

"""


@app.route('/')
def index():
    return form.format("")

@app.route('/', methods=["POST"])
def encrypt():
    rotation_element = int(request.form['rot'])
    text_element= request.form['text']
    result = rotate_string(text_element, rotation_element)
    return form.format(result)


app.run()
