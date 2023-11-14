from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_connection_url = os.environ.get('DATABASE_CONNECTION_URL_STRING')
engine = create_engine(db_connection_url) 

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:

    result = conn.execute(text("select * from jobs where id = {}".format(id)))

    rows = result.all()
    print(rows)
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()