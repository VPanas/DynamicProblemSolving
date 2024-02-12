from flask import Flask, abort, render_template
import os
from datetime import date


app = Flask(__name__, static_folder='static')

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

users = [
    {
        'id':1001,
        'username':'jorge24',
        'register_date':date(2002, 12, 31),
        'photo_url':'https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&fl=progressive&q=70&fm=jpg',
        'problems_history':[
            {
                'problem_id':100,
                'date_solved':date(2024, 2, 9),
                'score':90
            },
            {
                'problem_id':101,
                'date_solved':date(2024, 2, 10),
                'score':60
            },
            {
                'problem_id':102,
                'date_solved':date(2024, 2, 11),
                'score':20
            }
        ],

    }
]

@app.route('/')
def index():
    # get problems from the db
    return render_template('index.html', user=users[0])

@app.route('/problems')
def problems():
    # query from db all problems
    return render_template('problems/problems.html', problems = problems_data, user=users[0])

@app.route('/problem/<int:id>')
def problem(id):
    selected_problem = next((p for p in problems_data if p['id'] == id), None)

    if selected_problem:
        return render_template('problems/problem.html', problem=selected_problem, user=users[0])
    else:
        abort(404)

@app.route('/about')
def about():
    #about us info
    return render_template('info/about.html', user=users[0])

@app.route('/contact')
def contact():
    #form and diff links to contact
    return render_template('info/contact.html', user=users[0])

@app.route('/top')
def top():
    #best results
    return render_template('top/top.html', user=users[0])

@app.route('/profile/<username>')
def profile(username):
    #el perfil
    return render_template('profile/profile.html', user=users[0])

if __name__ == '__main__':
    app.run(debug=True)



    #command = ['manim', 'animation.py', 'CreateCircle', '-pql']
    #subprocess.run(command)
    #project_path = os.path.abspath(os.path.dirname(__file__))
    #video_path = os.path.join(project_path, 'media', 'videos', 'animation', '480p15', 'partial_movie_files', 'CreateCircle', 'video1.mp4')
    #, video_path=video_path