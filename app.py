from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 100,000'
    },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 150,000'
    },
    {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    },
    {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$ 150,000'
    }
]

@app.route("/")
def index():
    return render_template("index.html", jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)