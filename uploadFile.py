import os
import dropbox
from pkg_resources import to_filename

class TransferData:

   def __init__(self,access_token):
       self.accessToken = access_token

   def upload_file(self,from_file,to_file):
      dbx = dropbox.Dropbox(self.accessToken)
      
      for root, dirs, files in os.walk(from_file, topdown=False):

         for to_filename in files:
            local_path = os.path.join(root,to_filename)
            relativePath = os.path.relpath(local_path,from_file)
            dropboxPath = os.path.join(to_file,relativePath)

            f = open(local_path,'rb')
            dbx.files_upload(f.read(),dropboxPath)

def main():
    accessToken = "sl.Aw5rcT93kIwxq8fjmcjpUB2NBTcBkHXV-5p_sR2fxewTb_tDbTkavfDJibqzxykOBDeDCQLo05zokWp3_g4YR5cmDtaThjGMPs69Kr1dUUugr2HTj060WwcXxnmzMB2CupnnzAI"        
    transferData = TransferData(accessToken)
    file_from = input("Enter the file you want to put in the Dropbox")
    toFile = input("Enter the file you want to save it in the Dropbox")
    transferData.upload_file(file_from,toFile)
    print("file has been executed")


main()