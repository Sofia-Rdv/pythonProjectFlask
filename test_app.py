from flask import Flask


# Создаем объект приложения Flask
app = Flask(__name__)


# --- Задание 1. Простые маршруты ---
@app.route('/hello')
def hello():
    return "Hello, world!"


@app.route('/info')
def info():
    return "This is an informational page."


# --- Задание 2: Динамические маршруты ---
@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    try:
        # Пробуем преобразовать входные данные в числа(float для универсальности)
        n1 = float(num1)
        n2 = float(num2)
        result = n1 + n2
        # Убираем 0, если число целое, для красоты вывода
        if result.is_integer():
            result = int(result)
        return f"The sum of {num1} and {num2} is {result}."
    except ValueError:
        # Если ввели не числа
        return "Ошибка: Для расчета суммы /calc/ должны быть переданы числа (например, /calc/3/5/).", 400


# --- Задание 3. Создайте маршрут /reverse/, который переворачивает текст. ---
@app.route('/reverse/<text>')
def reverse(text):
    # Валидация: проверяем, что текст не пустой и не состоит только из пробелов
    if not text.strip():
        return "Ошибка: Тест для переворота не должен быть пустым.", 400

    reverse_text = text[::-1]
    return reverse_text


# --- Задание 4. Реализуйте маршрут /user//. Приветствие с именем и возрастом. ---
@app.route('/user/<name>/<age>')
def user_profile(name, age):
    try:
        age_int = int(age)

        # Валидация возраста
        if age_int < 0:
            return "Ошибка: Возраст не может быть отрицательным числом.", 400
        if age_int > 120:
            return "Ошибка: Указан слишком большой возраст.", 400

        return f"Hello, {name}. You are {age_int} years old."

    except ValueError:
        return "Ошибка: Возраст должен быть целым числом", 400


# Запуск приложения
# if __name__ == "__main__":
#     app.run(debug=True)