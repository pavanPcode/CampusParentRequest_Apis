from flask import Flask
from flask_cors import CORS
from Services import ParentsDetails,VisitsPickups,Announcements,ImgAdvertisement


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Campus Parents Appointment'


app.register_blueprint(ParentsDetails.parentsDetailsapp)
app.register_blueprint(VisitsPickups.VisitsPickupsapp)
app.register_blueprint(Announcements.Announcementsapp)
app.register_blueprint(ImgAdvertisement.ImgAdvertisementapp)

if __name__ == '__main__':
    app.run()


