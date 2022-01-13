from flask import Flask,render_template,request

app=Flask(__name__,template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pass/',methods=['POST'])
def handler_pass_endpoint():
    if request.method == 'POST':
        id=request.form["Enter ID"]
        name=request.form["Enter your name "]
    return render_template('pass.html')

@app.errorhandler(404)
def invalid_route(e):
    return render_template('404.html')

