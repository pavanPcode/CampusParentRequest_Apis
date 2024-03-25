
from ftplib import FTP


# FTP credentials
server = '50.63.8.82'
username = 'novusadmin'
password = 'zq4z906$X'
remote_path = '/Advertisement_Images'



def upload(file):
    try:
        ftp = FTP(server)
        ftp.login(username, password)
        ftp.cwd(remote_path)

        # Upload the file without saving it locally
        ftp.storbinary(f'STOR {file.filename}', file)

        ftp.quit()
        return 'File uploaded successfully'
    except Exception as e:
        return f'An error occurred: {str(e)}'