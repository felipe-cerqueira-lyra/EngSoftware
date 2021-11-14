from website import create_app

app = create_app()


@app.route('/')
def home():
    return 'Home Page'


if __name__ == '__main__':
    app.run(debug=True)
