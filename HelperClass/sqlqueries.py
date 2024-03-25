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

Getvisitorpickupqueries = """select v.RequestID,v.RegID,FORMAT(v.StartDateTime, 'dd-MM-yyyy HH:mm tt') StartDateTime,FORMAT(v.EndDateTime, 'dd-MM-yyyy` HH:mm tt') EndDateTime
,v.VisitorName,v.Reason,v.RequestType,v.Status,FORMAT(v.createdon, 'dd-MM-yyyy HH:mm tt')  CreatedOn,
v.IsActive,v.mobileNo,v.GuardianDetailsid
,COALESCE(r.fullname, r.firstname) AS studentname from Request.VisitsPickups  V
inner join [Campus].[Registrations] r on r.id = v.RegID
where V.mobileno = '{0}' and V.isactive = 1 
order by id desc"""


CreateAnnouncementsquerie = """ INSERT INTO [Request].Announcements (Name, Description, StartDateTime, EndDateTime,Superid)
VALUES ('{0}', '{1}', '{2}', '{3}',{4});"""

UpdateAnnouncementsquerie = """UPDATE [Request].Announcements
SET Name = '{0}', Description = '{1}',
StartDateTime = '{2}',EndDateTime = '{3}' ,Superid = {4},UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE())
WHERE ID = {5}; -- Assuming you want to update the announcement with ID = {5} """

DeleteAnnouncementsquerie = """UPDATE [Request].Announcements SET IsActive = 0,UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE()) WHERE ID = {0};  """

GetAnnouncementsquerie = """SELECT id,superid,name,description,startdatetime,enddatetime,isactive,createdon,updatedon
 FROM [Request].Announcements 
WHERE IsActive = 1 
AND Superid = {0} 
AND (StartDateTime between DATEADD(DAY, -7, GETDATE()) and GETDATE() OR 
EndDateTime between   GETDATE() and DATEADD(DAY, 7, GETDATE())); """

GetimagesAdvPathsQuary = """select id,imagename from [Request].imagesAdvPaths  
                            where isactive = 1  and isexpire = 0 and superid = {0}
                                    union all
                            select id,imagename from [Request].imagesAdvPaths  
                            where isactive = 1  and isexpire = 1 and superid = {0}  
                            AND (startdatetime between DATEADD(DAY, -7, GETDATE()) and GETDATE() OR 
                            enddatetime between   GETDATE() and DATEADD(DAY, 7, GETDATE()));"""

deleteimagesAdvPathsQuary = """UPDATE [Request].imagesAdvPaths  SET isactive = 0,
    UpdatedOn = DATEADD(MINUTE, 330, GETUTCDATE()) WHERE id = {0};"""

createimagesAdvPathsExpireQuary = """INSERT INTO [Request].imagesAdvPaths (superid,imageName, StartDateTime, EndDateTime,isExpire)
VALUES ({0},'{1}', '{2}', '{3}',{4});"""

createimagesAdvPathsQuary = """INSERT INTO [Request].imagesAdvPaths (superid,imageName,isExpire)
VALUES ({0},'{1}',{2});"""