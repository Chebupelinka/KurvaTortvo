from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#from Parser import Parser


class Start:

    auth = GoogleAuth()
    auth.LocalWebserverAuth()
    drive = GoogleDrive(auth)

    def create_and_upload_file(self, file_name='test.txt'):

        try:
            my_file = self.drive.CreateFile({"title": f'{file_name}'})
            my_file.SetContentString("Text")
            my_file.Upload()
            return f"File {file_name} was uploaded!"

        except Exception as _ex:
            return "Error!"

    def get_folder_id(self):
        root_folder = self.drive.ListFile({'q': "trashed=false"}).GetList()
        for fold in root_folder:
            print(fold)
        # 1Fe9DzGJ30AFR93hk9kQrPl7Qql5RAQ9Q
        # Print the folder names and IDs

    def __init__(self):
        print()
        #print(self.create_and_upload_file())

    if __name__ == '__main__':
        print("Success!")


p = Start()
p.get_folder_id()
