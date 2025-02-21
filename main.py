from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    roots = None
    error = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            if a <= 0:
                error = "Коэффициент 'a' не может быть меньше или равен нулю"
            else:
                discriminant = b ** 2 - 4 * a * c
                if discriminant > 0:
                    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                    roots = (root1, root2)
                elif discriminant == 0:
                    root = -b / (2 * a)
                    roots = (root,)
                else:
                    error = "Уравнение не имеет действительных корней"
        except ValueError:
            error = "Введите числовые значения для a, b, c"
        except ZeroDivisionError:
            error = "Коэффициент 'a' не может быть равен нулю"

    return render_template('main.html', roots=roots, error=error)


if __name__ == '__main__':
    app.run(debug=True)
