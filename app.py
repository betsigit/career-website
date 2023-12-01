from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'python developer',
    'location': 'Ethiopia',
    'salary' :'10,000ETB'
  
  },
  {
    'id':2,
    'title':'flask developer',
    'location': 'Ethiopia',
    'salary' :'15,000ETB'

  },
  {
    'id':3,
    'title':'MERN stack developer',
    'location': 'Ethiopia',
    'salary' :'30,000ETB'

  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS,company_name ='impex')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug =True)



