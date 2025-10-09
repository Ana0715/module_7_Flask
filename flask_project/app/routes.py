from app import app

@app.route('/')
def start_page():
    return 'This is the start page.'

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is informational page.'

@app.route('/calc/<a>/<b>')
def calc(a, b):
    try:
        a = int(a)
        b = int(b)
        return f'The sum of {a} and {b} is {a + b}.'
    except ValueError:
        return 'Ошибка: введите целые числа', 400
    
@app.route('/reverse/<some_text>')
def reverse(some_text):
    if not some_text:
        return 'Ошибка: Неверно введено значение!', 400
    return f'{some_text}: {some_text[::-1]}'

@app.route('/user/<name>/<int:age>')
def user_info(name, age):
    if not name:
        return 'Ошибка: Имя не может быть пустым', 400
    if age <= 0:
        return 'Ошибка: Возраст должен быть положительным числом', 400
    return f'Hello, {name}. You are {age} years old.'

@app.errorhandler(400)
def bad_request(error):
    return error, 400

@app.errorhandler(404)
def not_found(error):
    return 'Ошибка: Маршрут не найден', 404

