import sys, os
import krypto
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
a= 0
class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Pilla algne tekstifail siia \n\n')
        
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }                  
        ''')   
class AppDemo(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setAcceptDrops(True)
        
        mainLayout = QVBoxLayout()
        self.setWindowTitle("Zeta") 
        self.setLayout(mainLayout)
        
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
 
        self.setLayout(mainLayout)
        
        
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasText:
            event.accept()
        else:
            event.ignore()
            
    def dragMoveEvent(self, event):
        if event.mimeData().hasText:
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        global a, key_path
        if a==0 and event.mimeData().hasText:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            event.accept()
            krypto.encrypt(file_path)
            a +=1
        elif a== 1 and event.mimeData().hasText:
            event.setDropAction(Qt.CopyAction)
            key_path = event.mimeData().urls()[0].toLocalFile()
            event.accept()
            a +=1
        elif a ==2 and event.mimeData().hasText:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            event.accept()
            krypto.decrypt(key_path, file_path)
            a +=1
        else:
            event.ignore()
    
        

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec_())