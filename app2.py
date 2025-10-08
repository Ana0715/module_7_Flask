from flask import Flask

app = Flask(__name__)

# 1

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an informational page.'


# 2

@app.route('/calc/<a>/<b>')
def calc(a, b):
    try:
        a = int(a)
        b = int(b)
        return f'The sum of {a} and {b} is {a + b}'
    except ValueError:
        return 'Ошибка: введите целые числа', 400


# 3

@app.route('/reverse/<some_text>')
def reverse(some_text):
    if not some_text:
        return 'Ошибка: Неверно введено значение!', 400
    return f'{some_text}: {some_text[::-1]}'


# 4

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


if __name__ == '__main__':
    app.run(debug=True)





# Добавьте обработку ошибок для неправильных данных (например, /calc/a/b).
# Для маршрута /reverse/ добавьте проверку, чтобы текст содержал хотя бы один символ.
# Для маршрута /user// добавьте валидацию возраста (например, не допускайте возраст меньше 0).