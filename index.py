from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def start(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    img_name = url_for("static", filename="img/sci.png")
    if "инженер" in prof or "строитель" in prof:
        img_name = url_for("static", filename="img/ing.png")

    return render_template("training.html", prof=prof.lower(), img=img_name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
