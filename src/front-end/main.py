from flask import Flask, abort, render_template
import os
from user.streak.getDates import getWeeks
from user.user import getUser
from problems.getProblems import getProblems


app = Flask(__name__, static_folder='static')

username = "jorge24"

@app.route('/')
def index():
    # get problems from the db
    user = getUser(username="jorge24")
    return render_template('index.html', user=user)

@app.route('/problems')
def problems():
    problems = getProblems()
    user = getUser(username="jorge24")
    return render_template('problems/problems.html', problems = problems, user=user)

@app.route('/problem/<int:id>')
def problem(id):
    selected_problem = next((p for p in getProblems() if p['id'] == id), None)
    user = getUser(username="jorge24")
    if selected_problem:
        return render_template('problems/problem.html', problem=selected_problem, user=user)
    else:
        abort(404)

@app.route('/about')
def about():
    #about us info
    user = getUser(username="jorge24")
    return render_template('info/about.html', user=user)

@app.route('/contact')
def contact():
    #form and diff links to contact
    user = getUser(username=username)
    return render_template('info/contact.html', user=user)

@app.route('/ranking')
def top():
    user = getUser(username="jorge24")
    return render_template('ranking/ranking.html', user=user)

@app.route('/profile/<username>')
def profile(username):
    weeks = getWeeks()
    user = getUser(username=username)
    return render_template('profile/profile.html', user=user, weeks=weeks)

if __name__ == '__main__':
    app.run(debug=True)



    #command = ['manim', 'animation.py', 'CreateCircle', '-pql']
    #subprocess.run(command)
    #project_path = os.path.abspath(os.path.dirname(__file__))
    #video_path = os.path.join(project_path, 'media', 'videos', 'animation', '480p15', 'partial_movie_files', 'CreateCircle', 'video1.mp4')
    #, video_path=video_path