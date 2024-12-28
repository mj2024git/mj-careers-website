from flask import Flask, jsonify, render_template

app = Flask(__name__)
JOBS=[
{
    'id':1,
    'salary':'$1,000.00',
    'title':'Data Analyst',
    'location':'Cranborne, Harare',
},
    {
        'id':2,
        'salary':'$1,500.00',
        'title':'Data Scientist',
        'location':'Msasa Park, Harare',
    },
    {
        'id':3,
        'salary':'$2,000.00',
        'title':'Software Engineer',
        'location':'Balgravia, Harare',
    },
    {
        'id':4,
        'salary':'$2,500.00',
        'title':'Database Administrator',
        'location':'Malborough, Harare',
    }
]
@app.route("/")
def hello():
    return render_template('home.html', 
                            jobs=JOBS,
                            company_name='Mj')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)