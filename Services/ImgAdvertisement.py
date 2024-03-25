from flask import Blueprint,request,jsonify,send_from_directory,send_file
from DAL import dbImgAdvertisement
from ftplib import FTP
import tempfile
import os
import io

ImgAdvertisementapp = Blueprint('ImgAdvertisementapp',__name__,url_prefix='/ImgAdvertisement')


@ImgAdvertisementapp.route('/GetimagesAdvPaths')
def GetimagesAdvPaths():
    superid = request.args.get('superid')
    result = dbImgAdvertisement.dbGetimagesAdvPaths(superid)
    return jsonify(result)

@ImgAdvertisementapp.route('/createimagesAdv',methods = ['POST'])
def createimagesAdv():
    data = request.form
    accepted_extensions = ['jpg', 'png', 'jpeg']

    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    file_extension = file.filename.rsplit('.', 1)[-1].lower()
    if file_extension not in accepted_extensions:
        return jsonify({'message': "Error: Invalid file extension. Only jpg, png, and jpeg are allowed."})

    result = dbImgAdvertisement.dbcreateimagesAdv(data, file)

    return jsonify(result)

@ImgAdvertisementapp.route('/deleteimagesAdvPaths',methods = ['POST'])
def deleteimagesAdvPaths():
    data = request.json
    result = dbImgAdvertisement.dbdeleteimagesAdvPaths(data)
    return jsonify(result)


@ImgAdvertisementapp.route('/images/<path:filename>')
def send_image(filename):
    try:
        # FTP credentials
        server = '50.63.8.82'
        username = 'novusadmin'
        password = 'zq4z906$X'
        remote_path = '/Advertisement_Images'
        with FTP(server) as ftp:
            ftp.login(username, password)
            ftp.cwd(remote_path)

            # Create an in-memory buffer
            file_buffer = io.BytesIO()

            # Retrieve the file from the FTP server and write it to the buffer
            ftp.retrbinary('RETR ' + filename, file_buffer.write)

            # Set the buffer's position to the beginning
            file_buffer.seek(0)

            # Return the file directly from the buffer
            return send_file(file_buffer, mimetype='image/jpeg')  # Adjust mimetype as needed
    except Exception as e:
        return f'An error occurred: {str(e)}'



#
#
# @ImgAdvertisementapp.route('/delete-image/<path:filename>', methods=['DELETE'])
# def delete_image(filename):
#     server = 'ftp.example.com'
#     username = 'your_username'
#     password = 'your_password'
#
#     ftp_handler = FTPImageHandler(server, username, password)
#
#     remote_path = '/remote/directory/' + filename
#     ftp_handler.delete_image(remote_path)
#     ftp_handler.disconnect()
#     return jsonify({'message': 'File deleted successfully'})
#
#
# @ImgAdvertisementapp.route('/get-image', methods=['GET'])
# def get_image():
#     server = '50.63.8.82'
#     username = 'novusadmin'
#     password = 'zq4z906$X'
#     filename = 'table.txt'
#
#     ftp_handler = FTPImageHandler(server, username, password)
#
#     local_path = filename.split('/')[-1]
#     remote_path = '/Advertisement_Images/'
#
#     remote_path = remote_path + filename
#     ftp_handler.get_image(remote_path, local_path)
#     ftp_handler.disconnect()
#     return jsonify({'message': 'File retrieved successfully'})
