from flask import Flask, url_for

app = Flask(__name__)


# @app.route('/')
# def start():
#     return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return """<p>Человечество вырастает из детства.</p>
    <p>Человечеству мала одна планета.</p>
    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p>И начнем с Марса!</p>
    <p>Присоединяйся!</p>"""



@app.route('/')
def image_mars():
    return f"""<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <title>Жди нас, Марс!</title>
                       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                       <link rel="stylesheet" href="{url_for("static", filename="css/styles.css")}">
                     </head>
                     <body>
                        <div class="container">
                            <h3>Вот, она какая, красная планета.</h1>
                            <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть картинка, но не нашлась">
                            <div class="row">
                                <div class="col-12 gray">
                                    <p>Человечество вырастает из детсва</p>
                                </div>
                                
                                <div class="col-12 green">
                                    <p>Человечеству мала одна из планет</p>
                                </div>
                                
                                <div class="col-12 gray">
                                    <p>Мы сделаем обидаемым безжизненные пока планеты.</p>
                                </div>
                                
                                <div class="col-12 yellow">
                                    <p>И начнём с марса!</p>
                                </div>
                                
                                <div class="col-12 red">
                                    <p>Присоединяся!</p>
                                </div>
                            </div>
                        </div>
                     </body>
                   </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

