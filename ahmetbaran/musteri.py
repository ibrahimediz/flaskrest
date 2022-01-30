from app import app, db
# app klasor icindeki init ile birlikte configlere erisebilmeyi saglar

from app.models import Customer, CustomerRecords

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Customer': Customer, 'Records': CustomerRecords}