from flask import Flask, request

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def homepage():
    return app.send_static_file('homepage.html')

@app.route('/profilepage')
def profilepage():
    return app.send_static_file('profilepage.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)