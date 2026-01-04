from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Job
from scraper import scrape_jobs

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

@app.route("/")
def home():
    return "<h2>Welcome to the Job Scraper Portal 🚀</h2><p>Visit <a href='/jobs'>/jobs</a> to view listings.</p>"

@app.route("/jobs")
def jobs():
    jobs = Job.query.all()
    return render_template("jobs.html", jobs=jobs)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # scrape jobs only if DB is empty
        if Job.query.count() == 0:
            scrape_jobs()
    app.run(debug=True)
