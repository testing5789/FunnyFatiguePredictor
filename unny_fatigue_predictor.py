from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Witzige Antworten
responses = [
    "Heute bist du ein Superschläfer mit Turbo-Fatigue – ruh dich aus oder riskiere ein Nickerchen auf der Tastatur!",
    "Du bist ein Energiewunder – nur 12 Stunden Schlaf nötig, um die Welt zu erobern!",
    "Achtung, Fatigue-Alarm! Heute ist Nickerchen-Oberliga – bleib liegen und lache!",
    "Mit deinem Schlaf bist du bereit, die Mathematik der Müdigkeit zu meistern – oder einfach zu dösen."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        hours = float(request.form['hours'])
        tiredness = int(request.form['tiredness'])
        if hours > 12 and tiredness > 5:
            prediction = random.choice(responses)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
