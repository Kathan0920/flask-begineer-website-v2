from sqlalchemy import create_engine, text
from decouple import config

db_connection_url = config('DATABASE_CONNECTION_URL_STRING')
engine = create_engine(db_connection_url)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs
