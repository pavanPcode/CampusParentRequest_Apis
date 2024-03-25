from ftplib import FTP


def upload_image_ftp(server, username, password, image_path, remote_path):
    try:
        # Connect to the FTP server
        ftp = FTP(server)
        ftp.login(username, password)

        # Open the image file
        with open(image_path, 'rb') as file:
            # Change to the remote directory (if it exists)
            ftp.cwd(remote_path)

            # Upload the image file
            ftp.storbinary('STOR ' + image_path.split('/')[-1], file)

        # Close the FTP connection
        ftp.quit()
        print("Upload successful.")
    except Exception as e:
        print("Error:", e)


# Example usage
server = '50.63.8.82'
username = 'novusadmin'
password = 'zq4z906$X'
image_path = 'table.txt'
remote_path = '/Advertisement_Images'

upload_image_ftp(server, username, password, image_path, remote_path)

