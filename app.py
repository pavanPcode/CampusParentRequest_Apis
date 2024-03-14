from flask import Flask
from flask_cors import CORS
from Services import ParentsDetails,VisitsPickups


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Campus Parents Appointment'

#import
app.register_blueprint(ParentsDetails.parentsDetailsapp)
app.register_blueprint(VisitsPickups.VisitsPickupsapp)

if __name__ == '__main__':
    app.run()

