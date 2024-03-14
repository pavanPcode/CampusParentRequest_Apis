from HelperClass import sqlhelper,sqlqueries

def dbGetParentDetails(superid,mobile):
    quary = sqlqueries.getRegistrationDetails.format(superid,mobile)
    runquary = sqlhelper.sqlserverhelper()
    rows = runquary.queryall(quary)
    return rows