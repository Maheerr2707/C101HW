import os
import dropbox

class TransferData:

   def upload_file(self,from_file,to_file):
      dbx = dropbox.Dropbox(self.accessToken)
      f = open(from_file,'rb')
      dbx.files_upload(f.read(),to_file)

   def upload_file(self,from_file,to_file):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(from_file,'rb')
        dbx.files_upload(f.read(),to_file)

def main():
    accessToken = "sl.AwsI0bHkoBscvFFZzgjLJUyTH1wAIDfqTbIh4NlzQPJ2NVTVgiykMYtdZhDNMdRoZOFg6RuhJ4YGc9h41kACzaIpgTAaXBFDLLiuYgVYWt7I2uOQmcxANN_Ycywyd2dwdrbA9_s"        
    transferData = TransferData(accessToken)
    fromFile = input("Enter the file you want to put in the Dropbox")
    toFile = input("Enter the file you want to save it in the Dropbox")
    transferData.upload_file(fromFile,toFile)
    print("file has been executed")


   for root, dirs, files in os.walk("D:\WHITEHAT JR\C-17", topdown=False):

   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))


main()