from HelperClass import sqlhelper,sqlqueries

def dbgetvisitorpickup(mobileno):
    try:
        quary =sqlqueries.Getvisitorpickupqueries.format(mobileno)
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.queryall(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}


def dbCreateVisitorPickups(data):
    try:
        for regid in data['regid']:
            quary =sqlqueries.createvisitorpickupqueries.format(regid, data['startdatetime'], data['enddatetime'], data['visitorname'],
                           data['reason'], data['requesttype'],data['mobileno'],data['guardiandetailsid'])
            runquary = sqlhelper.sqlserverhelper()
            rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}

def dbupdatevisitorpickup(data):
    try:
        for regid in data['regid']:
            quary =sqlqueries.updatevisitorpickupqueries.format(regid, data['startdatetime'], data['enddatetime'], data['visitorname'],
                           data['reason'], data['requesttype'],data['requestid'],data['mobileno'],data['guardiandetailsid'])
            runquary = sqlhelper.sqlserverhelper()
            rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}

def dbdeletevisitorpickup(data):
    try:
        quary =sqlqueries.deletevisitorpickupqueries.format(data['requestid'])
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}