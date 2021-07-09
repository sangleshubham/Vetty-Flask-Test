from flask import Flask, request , render_template , Markup
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

base_path = "files/"

@app.errorhandler(HTTPException)
def method_not_allowed(e):
    return render_template("error.html", code= e.code , message =  e.description)

@app.route('/', methods=["GET"], defaults={'filename': "file1"})
@app.route('/<filename>', methods=["GET"])
def read_file(filename):
    argument = request.args
    files = {
        ("file1", "file1.txt"): base_path + "file1.txt",
        ("file2", "file2.txt"): base_path + "file2.txt",
        ("file3", "file3.txt"): base_path + "file3.txt",
        ("file4", "file4.txt"): base_path + "file4.txt",
        ("new", "new.txt"): base_path + "new.txt",
    }

    file = secure_filename(filename)
    error_mes = ""
    start = argument.get("start")
    end = argument.get("end")
    if  start != None and not start.isnumeric():
        return render_template("error.html", code= "400" , message =  "Bad Request! Start value must be number" )
    if  end != None and not end.isnumeric():
        return render_template("error.html", code= "400" , message =  "Bad Request! End value must be number" )
    finalfile = ""

    for f in files:
        if file in f:
            finalfile = files[f]

    textdata = []

    # Get encodning of text-file
    encod  = None
    try:
        f = open(finalfile , encoding="utf-8" )
        f.readlines()
        f.close()
        encod = "utf-8"
    except UnicodeDecodeError:
        try:
            f = open(finalfile , encoding="utf-16" )
            f.readlines()
            f.close()
            encod = "utf-16"
        except e:
            return render_template("error.html", code = 415 , message =  "Unsupported File Type! Try with text files" )


    with open(finalfile , encoding=encod ) as read_this_file:
        lines = read_this_file.readlines()
        start = int(start)  if start != None else 0
        end = int(end) if end != None else len(lines)
        data = lines[ abs(int(start)) : abs(int( end))]
        for tag in data:
            textdata.append( Markup(tag))
        return render_template("render.html", lines=textdata , file =  file )


if __name__ == "__main__":
    app.run()
