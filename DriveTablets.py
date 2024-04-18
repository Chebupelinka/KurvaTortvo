from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#from Parser import Parser


class Start:

    auth = GoogleAuth()
    auth.LocalWebserverAuth()
    drive = GoogleDrive(auth)
    all_folders = {}

    root = '00000000000000000'

    def create_and_upload_file(self, file_name='test.txt', parent_folder=root):

        try:
            my_file = self.drive.CreateFile({'title': f'{file_name}'})
            my_file['parents'][0]['id'] = parent_folder
            my_file.SetContentString("Text")
            my_file.Upload()
            return f"File {file_name} was uploaded!"

        except Exception as _ex:
            return "Error!"

    def get_root_folder_id(self):
        root_folder = self.drive.ListFile({'q': "trashed=false"}).GetList()
        for fold in root_folder:
            if str(fold['parents'][0]['isRoot']) == 'True':
                return fold['parents'][0]['id']
        # 1Fe9DzGJ30AFR93hk9kQrPl7Qql5RAQ9Q
        # Print the folder names and IDs

    def get_list_of_all_folders(self):
        root_folder = self.drive.ListFile({'q': "trashed=false"}).GetList()
        for fold in root_folder:
            if self.all_folders.get(fold['parents'][0]['id'], 0) == 0:
                self.all_folders[str(fold['parents'][0]['id'])] = []
            d = {str(fold['id']): str(fold['title'])}
            self.all_folders[str(fold['parents'][0]['id'])].append(d)
        # 1Fe9DzGJ30AFR93hk9kQrPl7Qql5RAQ9Q
        # Print the folder names and IDs

    def __init__(self):

        self.root = self.get_root_folder_id()
        self.get_list_of_all_folders()
        #print(self.create_and_upload_file())

    if __name__ == '__main__':
        print("Success!")


p = Start()
print(p.all_folders)
