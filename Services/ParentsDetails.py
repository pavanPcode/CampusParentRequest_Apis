from flask import Blueprint,request,jsonify
from DAL import dbParentsDetails

parentsDetailsapp = Blueprint('parentsDetailsapp',__name__)

@parentsDetailsapp.route('/GetParentDetails')
def GetParentDetails():
    superid = request.args.get('superid')
    mobile = request.args.get('mobile')
    result = dbParentsDetails.dbGetParentDetails(superid,mobile)
    return jsonify(result)