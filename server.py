import translate
from flask import Flask, render_template, request

app = Flask("Translator")


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/frToEn")
def fr_to_en():
    return translate.french_to_english(request.args.get('textToTranslate'))


@app.route("/enToFr")
def en_to_fr():
    return translate.english_to_french(request.args.get('textToTranslate'))

    

if __name__=="__main__":
    app.run(debug=True, port=5001)
