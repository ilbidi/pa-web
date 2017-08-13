# views
from pa_web import app

# Index
@app.route('/')
@app.route('/index')
def index():
    return 'Hi'
