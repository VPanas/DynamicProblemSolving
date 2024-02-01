from flask import Flask, abort, render_template
import os

app = Flask(__name__)

problems_data = [
    {
        'id': 1,
        'title': 'Problem 1',
        'description': 'Realizar un ciclo for bien fachero',
        'test_cases': [
            {'input': 'test_input_1', 'output': 'expected_output_1'},
            {'input': 'test_input_2', 'output': 'expected_output_2'},
        ]
    },
    {
        'id': 2,
        'title': 'Problem 2',
        'description': 'Realizar un while infinito',
        'test_cases': [
            {'input': 'test_input_1', 'output': 'expected_output_1'},
            {'input': 'test_input_2', 'output': 'expected_output_2'},
        ]
    },
]

@app.route('/')
def index():
    # get problems from the db
    return render_template('index.html')

@app.route('/problems')
def problems():
    # query from db all problems
    return render_template('problems/problems.html', problems = problems_data)

@app.route('/problem/<int:id>')
def problem(id):
    selected_problem = next((p for p in problems_data if p['id'] == id), None)

    if selected_problem:
        return render_template('problems/problem.html', problem=selected_problem)
    else:
        abort(404)

@app.route('/about')
def about():
    #about us info
    return render_template('info/about.html')

@app.route('/contact')
def contact():
    #form and diff links to contact
    return render_template('info/contact.html')

@app.route('/top')
def top():
    #best results
    return render_template('top/top.html')

@app.route('/profile/<id>')
def profile(id):
    #el perfil
    return render_template('profile/profile.html')

if __name__ == '__main__':
    app.run(debug=True)



    #command = ['manim', 'animation.py', 'CreateCircle', '-pql']
    #subprocess.run(command)
    #project_path = os.path.abspath(os.path.dirname(__file__))
    #video_path = os.path.join(project_path, 'media', 'videos', 'animation', '480p15', 'partial_movie_files', 'CreateCircle', 'video1.mp4')
    #, video_path=video_path