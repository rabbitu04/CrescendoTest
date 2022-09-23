import os

from src import create_app

app = create_app()


@app.route('/hello-world', methods=['GET'])
def hello_word():
    return 'Hello'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT'))
    )
