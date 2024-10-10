# Interpreter pour gérer API et le "random mode"

from flask import Flask, jsonify
import random

app = Flask(__name__)

# Phrases de test
citations = [
    "On dit que le rire est le meilleur des remèdes… Ton visage doit être en train de guérir le monde !",
    "Le premier homme qui est mort a dû être drôlement surpris",
    "Entre le sarcasme et l’ironie il y a la même distance qu’entre un rot et un soupir.",
    "J’ai passé une merveilleuse soirée, mais ce n’était pas ça.",
    "Une citation ironique qui peut ennuyer quiconque se fait dire. L’ironie devant le bellicisme politique dominant.",
    "Je te dirais bien d’aller en enfer, mais je travaille là-bas et je ne veux pas voir ta sale tronche tous les jours."
]

@app.route('/generate-text', methods=['GET'])
def generate_text():
    random_text = random.choice(citations)
    return jsonify({"generated_text": random_text})

if __name__ == '__main__':
    app.run(debug=True)

#Après execution Ouvrir Postman ou Navigateur et se rendre sur http://127.0.0.1:5000/generate-text