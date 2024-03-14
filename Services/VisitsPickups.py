from flask import Blueprint,request,jsonify
from DAL import dbVisitsPickups

VisitsPickupsapp = Blueprint('VisitsPickupsapp',__name__,url_prefix='/VisitsPickups')

@VisitsPickupsapp.route('/CreateVisitorPickups',methods = ['POST'])
def CreateVisitorPickups():
    data = request.json
    result = dbVisitsPickups.dbCreateVisitorPickups(data)
    return jsonify(result)

@VisitsPickupsapp.route('/updatevisitorpickup',methods = ['POST'])
def updatevisitorpickup():
    data = request.json
    result = dbVisitsPickups.dbupdatevisitorpickup(data)
    return jsonify(result)

@VisitsPickupsapp.route('/getvisitorpickup')
def getvisitorpickup():
    mobileno = request.args.get('mobileno')
    result = dbVisitsPickups.dbgetvisitorpickup(mobileno)
    return jsonify(result)

@VisitsPickupsapp.route('/deletevisitorpickup',methods = ['POST'])
def deletevisitorpickup():
    data = request.json
    result = dbVisitsPickups.dbdeletevisitorpickup(data)
    return jsonify(result)