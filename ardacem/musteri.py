from app import app

from app.models import Customer,CustomerRecords

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'Customer':Customer,'Records':CustomerRecords}