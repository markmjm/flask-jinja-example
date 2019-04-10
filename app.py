from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    hasLowerCase = False
    hasUpperCase = False
    endsWithNumber = False
    username = request.args.get('username')
    if username is not None and len(str(username).strip()) > 0:
        lastletter = username[-1]
        for c in username:
            if c.islower():
                hasLowerCase = True
        for c in username:
            if c.isupper():
                hasUpperCase = True
        if lastletter.isdigit():
            endsWithNumber = True
    return render_template('report.html', hasLowerCase = hasLowerCase, hasUpperCase = hasUpperCase, endsWithNumber = endsWithNumber)

if __name__ == '__main__':
    app.run(debug=True)
