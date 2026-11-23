from Gen_QR_build26102026 import GénérateurQR
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import QIcon
import os

class IU:
    def __init__(self, app):
        
        self.erreur = {"vide" : ["La case pour QR est vide","Il n'y a pas de nom"], "long" : ["Le message est trop long","le nom est trop long"], "inconnu" : ["Comment tu t'es débrouillié ?"]}
        self.message_derreur = QErrorMessage()
        
        self.Generateur = GénérateurQR("Transformer en QRcode")
        
        self.app = app
        
        self.window = QWidget()
        self.window.resize(1000,1000)
        self.layout = QFormLayout()
        
        try:
            self.logo=os.path.join(os.path.dirname(__file__),"logo.ico")
            self.window.setWindowIcon(QIcon(self.logo))
        except Exception as t:
            return t
        
        self.premier_texte = QLabel("Entre ton truc pour le QR", alignment = Qt.AlignCenter)
        
        self.plain = QPlainTextEdit()
        self.plain.setPlaceholderText("Entre ton truc à transformer")
        
        self.pour_nom = QLineEdit()
        self.pour_nom.setPlaceholderText("Entre le nom du QR")
        
        self.url = QLabel('<a href="https://github.com/LOCKXIOR/QR-code-generator/tree/main">Vérifier les mises à jour</a>', alignment = Qt.AlignCenter)
        self.url.setOpenExternalLinks(True)
        self.url.setObjectName("URL")
        
        self.chemin = QLabel("Prêt.")
        self.chemin.setObjectName("chemin")
        
        self.bouton = QPushButton("Transformer")
        self.bouton.clicked.connect(self.transformer)
        
        
        self.layout.addWidget(self.premier_texte)
        self.layout.addWidget(self.url)
        self.layout.addWidget(self.pour_nom)
        self.layout.addWidget(self.plain)
        self.layout.addWidget(self.chemin)
        self.layout.addWidget(self.bouton)
        self.window.setLayout(self.layout)
        
        
    def launch(self):
        self.window.show()
        self.app.exec_()
    
    def transformer(self):
        nom = self.pour_nom.text()
        self.pour_nom.setText("")
        truc = self.plain.toPlainText()
        self.plain.setPlainText("")
        
        if self.requis(truc, nom)[0] and self.requis(truc, nom)[1]:
        
            if not truc:
                self._erreurs(("vide",0))
                
            elif not nom:
                self._erreurs(("vide",1))
                self.Generateur.transforme(truc)
                self.Generateur.enregistre(f"QR_{truc[0:5:1].replace(" ","")}")
                self.chemin.setText(f"Chemin : {os.getcwd()}")
                
            else:
                self.Generateur.transforme(truc)
                self.Generateur.enregistre(nom)
                self.chemin.setText(f"Chemin : {os.getcwd()}")
            
        elif not self.requis(truc, nom)[0]:
            
            self._erreurs(("long",0))
            
        elif not self.requis(truc, nom)[1]:
            
            self._erreurs(("long",1))
            
        else: 
            self._erreurs(("inconnu",0))
            
    def _erreurs(self, type_erreur):
        self.message_derreur.showMessage(self.erreur[type_erreur[0]][type_erreur[1]])

    def requis(self,a,b):
        return (len(a) <= 2930, len(b) <= 100)
        
        
if __name__ == "__main__":
    Appli = QApplication([])
    Appli.setStyleSheet("""
                    QLineEdit {
                        border-radius : 10px;
                        padding : 5px 10px
                    }
                    """)
    
    
    lor = IU(Appli)
    lor.launch()