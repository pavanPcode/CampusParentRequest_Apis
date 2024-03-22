from flask import Blueprint,request,jsonify
from DAL import dbAnnouncements

Announcementsapp = Blueprint('Announcementsapp',__name__,url_prefix='/Announcements')

@Announcementsapp.route('/CreateAnnouncements',methods = ['POST'])
def CreateAnnouncements():
    data = request.json
    result = dbAnnouncements.dbCreateAnnouncements(data)
    return jsonify(result)

@Announcementsapp.route('/updateAnnouncements',methods = ['POST'])
def updatevisitorpickup():
    data = request.json
    result = dbAnnouncements.dbupdateAnnouncements(data)
    return jsonify(result)

@Announcementsapp.route('/getAnnouncements')
def getvisitorpickup():
    superid = request.args.get('superid')
    result = dbAnnouncements.dbGetAnnouncements(superid)
    return jsonify(result)

@Announcementsapp.route('/deleteAnnouncements',methods = ['POST'])
def deletevisitorpickup():
    data = request.json
    result = dbAnnouncements.dbdeleteAnnouncements(data)
    return jsonify(result)