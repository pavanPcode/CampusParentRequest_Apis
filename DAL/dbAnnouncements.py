from HelperClass import sqlhelper,sqlqueries

def dbGetAnnouncements(superid):
    quary = sqlqueries.GetAnnouncementsquerie.format(superid)
    runquary = sqlhelper.sqlserverhelper()
    rows = runquary.queryall(quary)
    return rows



def dbCreateAnnouncements(data):
    try:
        quary =sqlqueries.CreateAnnouncementsquerie.format(data['Name'], data['Description'], data['StartDateTime'],
                           data['EndDateTime'], data['Superid'])
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}

def dbupdateAnnouncements(data):
    try:
        quary =sqlqueries.UpdateAnnouncementsquerie.format(data['Name'], data['Description'], data['StartDateTime'],
                           data['EndDateTime'], data['Superid'],data['id'])
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}

def dbdeleteAnnouncements(data):
    try:
        quary =sqlqueries.DeleteAnnouncementsquerie.format(data['id'])
        runquary = sqlhelper.sqlserverhelper()
        rows = runquary.update(quary)
        return rows
    except Exception as e:
        return {'Status': False, 'ResultData': [], 'Message': str(e)}