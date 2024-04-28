from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from Ui_main import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


class Start(QMainWindow, Ui_MainWindow):

    auth = GoogleAuth()
    auth.LocalWebserverAuth()
    drive = GoogleDrive(auth)
    all_folders = {}
    folder_buttons = []
    selfParent = '00000000000000000'

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
            print(fold['id'], fold['title'])
            if self.all_folders.get(fold['parents'][0]['id'], 0) == 0:
                self.all_folders[str(fold['parents'][0]['id'])] = []
            d = [str(fold['id']), str(fold['title'])]
            self.all_folders[str(fold['parents'][0]['id'])].append(d)
        # 1Fe9DzGJ30AFR93hk9kQrPl7Qql5RAQ9Q
        # Print the folder names and IDs

    def draw_folder_buttons(self, parent):
        next = self.all_folders[parent]

        for i in range(len(next)):
            self.ui.button = QPushButton(self)
            self.ui.button.setText(self.all_folders[parent][1])

    def __init__(self):
        super(Start, self).__init__()
        self.root = self.get_root_folder_id()
        self.selfParent = self.root
        self.get_list_of_all_folders()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print(self.all_folders)
        self.draw_folder_buttons(self.root)
        #print(self.create_and_upload_file())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Start()
    window.show()

    sys.exit(app.exec())
