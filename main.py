from caesar import rotate_string
from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True


formOne= """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
     
        <form action = "/" name= "form" method = "POST">
            <label for = "rot"> 
            Rotate By 
                <input type = "text"  name = "rot" value = 0>
            </label>
                <textarea name= "text"></textarea>
            <button type = "submit" form = "form" value = "Submit"> Submit </button>

        </form>
    </body>
</html>


"""


@app.route('/')
def index():
    content = formOne
    return content

@app.route('/', methods=["POST"])
def encrypt():
    rotation = request.form(['rot'])
    text= request.form(['text'])
    encryption =rotate_string(text, rotation)
    return encryption


app.run()
