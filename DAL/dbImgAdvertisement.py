from HelperClass import sqlhelper,sqlqueries,ftphelper
import os


def dbGetimagesAdvPaths(superid):
    quary = sqlqueries.GetimagesAdvPathsQuary.format(superid)
    runquary = sqlhelper.sqlserverhelper()
    rows = runquary.queryall(quary)
    return rows



def dbcreateimagesAdv(data,file):
    try:
        ftpresult = ftphelper.upload(file)
        print(ftpresult)
        print(data['isexpire'],type(data['isexpire']))

        if data['isexpire'] == '1':
            quary =sqlqueries.createimagesAdvPathsExpireQuary.format(data['superid'],file.filename,data['startdatetime'],
                                                           data['enddatetime'],1)
        else:
            quary = sqlqueries.createimagesAdvPathsQuary.format(data['superid'], file.filename, 0)
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}

def dbdeleteimagesAdvPaths(data):
    try:
        quary =sqlqueries.deleteimagesAdvPathsQuary.format(data['id'])
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}