getRegistrationDetails = """SELECT r.id regid,g.id GuardianDetailsid,r.superid,COALESCE(fullname, firstname) AS name,r.gender,r.dob,r.AdmissionNo,g.fathername,g.mothername,g.Address,g.mobileno
FROM [Campus].[Registrations] r
INNER JOIN [Campus].[GuardianDetails] g ON g.regid = r.id
WHERE  g.mobileno = '{1}' and superid = {0}"""


createvisitorpickupqueries = """INSERT INTO Request.VisitsPickups (RegID, StartDateTime, EndDateTime, VisitorName, Reason, RequestType, Status,mobileNo,GuardianDetailsid)
VALUES ({0}, '{1}', '{2}', '{3}', '{4}', {5}, 1,'{6}',{7});"""

updatevisitorpickupqueries = """UPDATE Request.VisitsPickups SET RegID = {0} ,StartDateTime = '{1}', EndDateTime = '{2}',VisitorName = '{3}',Reason = '{4}',
    RequestType = {5}, Status = 1 ,mobileno = '{7}',GuardianDetailsid = {8}
WHERE RequestID = {6}; 
"""

deletevisitorpickupqueries = """UPDATE Request.VisitsPickups
SET isactive = 0, 
    UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE())
WHERE RequestID = {0}; 
"""

Getvisitorpickupqueries = """select v.RequestID,v.RegID,FORMAT(v.StartDateTime, 'yyyy-MM-dd HH:mm tt'),FORMAT(v.EndDateTime, 'yyyy-MM-dd HH:mm tt')
,v.VisitorName,v.Reason,v.RequestType,v.Status,
v.IsActive,v.mobileNo,v.GuardianDetailsid
,COALESCE(r.fullname, r.firstname) AS studentname from Request.VisitsPickups  V
inner join [Campus].[Registrations] r on r.id = v.RegID
where V.mobileno = '{0}' and V.isactive = 1 
order by id desc"""