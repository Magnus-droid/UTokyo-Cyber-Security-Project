from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
file_path = '/UTokyo-Cyber-Security-Project/Packet_Cap/main.py'

file1 = drive.CreateFile()
file1.SetContentFile(file_path)
file1.Upload()
