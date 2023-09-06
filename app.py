from flask import Flask, render_template, jsonify

app = Flask(__name__)

BOSSES = [
    {
        'id': 1,
        'Title': 'Owl',
        'Location': 'Hirata',
        'Difficulty': 'Hard'
    },
    {
        'id': 2,
        'Title': 'Geni',
        'Location': 'Ashina Castle',
        'Difficulty': 'Mid'
    },
    {
        'id': 3,
        'Title': 'Ishhin',
        'Location': 'Haunted Place',
        'Difficulty': 'Very Hard'
    },
    {
        'id': 4,
        'Title': 'Monk',
        'Location': 'Deep Ashina',
        'Difficulty': 'Low-Mid'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', bosses=BOSSES)

@app.route("/api/bosses")
def list_bosses():
    return jsonify(BOSSES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

