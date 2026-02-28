from flask import Flask, jsonify, request
import represitory

#creer l'application
app = Flask(__name__)

#Definir les routes
@app.route('/')
def home ():
    return "c'est cool REST !"

@app.route('/students', methods=['GET'])
def get_students():
    students = represitory.get_all_students()
    return jsonify(students), 200

#lancer le serveur
#Force Flosk à écouter sur toutes les interfaces (IPV4 + IPV6):
if __name__ == ' __main__':
    app.run(host="0.0.0.0", port=5001, debug =True)