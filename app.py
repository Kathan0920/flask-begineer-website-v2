from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)

# This will return list of jobs data not in form of HTML but in form of json.
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  # data = request.args # request.args get the data from the url when the data is sent in the url without using post method.
  # token = request.POST[`"h-captcha-response"]
  # params = {
  #  "secret": "ES_d6e44e13476549f786ff01d4f38461f4",
  #  "response": token
  # }
  # json = http.POST("https://hcaptcha.com/siteverify", params)

  data = request.form   # request.form will get data from when it is sended using post method.
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', application=data, job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
