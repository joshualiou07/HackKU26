from flask import Flask, request, jsonify
from hwprioritizer import Prioritizer

app = Flask(__name__, static_folder='.')
prioritizer = Prioritizer()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/add', methods=['POST'])
def add_assignment():
    data = request.get_json()
    name = data.get('name')
    days = int(data.get('days'))
    difficulty = int(data.get('difficulty'))
    prioritizer.add(name, days, difficulty)
    prioritizer.sort()
    return jsonify({'status': 'success'})

@app.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = []
    for i, hw in enumerate(prioritizer.assignments):
        assignments.append({
            'index': i,
            'name': hw.name,
            'days': hw.due,
            'difficulty': hw.difficulty,
            'score': round(hw.score(), 3)
        })
    return jsonify(assignments)

@app.route('/remove/<int:index>', methods=['DELETE'])
def remove_assignment(index):
    if 0 <= index < len(prioritizer.assignments):
        prioritizer.remove(index)
        prioritizer.sort()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Invalid index'}), 400

if __name__ == '__main__':
    app.run(debug=True)