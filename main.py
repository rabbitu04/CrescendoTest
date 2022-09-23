from src import create_app

app = create_app()


@app.route('/hello-world', methods=['GET'])
def hello_word():
    return 'Hello'
