from Gen_QR_build26102026 import GénérateurQR
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import QIcon
import os

class IU:
    def __init__(self, app):
        
        self.erreur = {"vide" : ["La case pour QR est vide","Il n'y a pas de nom, enregistré sous abréviation"], "long" : ["Le message est trop long (max 2930)","le nom est trop long (max 100)"], "inconnu" : ["Comment tu t'es débrouillié ?"]}
        self.message_derreur = QErrorMessage()
        
        self.Generateur = GénérateurQR("Transformer en QRcode")
        
        self.want_design = 0
        self.type_design = "light"
        
        self.designs = {"light" : ["""QWidget {
    background-color: #f4f6f9;
}

QLabel#phrase {
    background-color: transparent;
    color: #1e293b;
    font-weight: bold;
}

QLabel#URL {
    background-color: transparent;
    color: #2563eb;
}

QLineEdit {
    background-color: #ffffff;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 6px 12px;
}

QLineEdit:focus {
    border: 1.5px solid #2563eb;
}

QPlainTextEdit {
    background-color: #ffffff;
    color: #0f172a;
    border: 1px solid #cbd5e1;
    border-radius: 20px;
    padding: 20px;
}

QPlainTextEdit:focus {
    border: 1.5px solid #2563eb;
}

QPushButton {
    background-color: #2563eb;
    color: #ffffff;
    border-radius: 20px;
    padding: 10px 20px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1d4ed8;
}

QPushButton:pressed {
    background-color: #1e40af;
}""","""QWidget {
    background-color: #f8f5f2;
}

QLabel#phrase {
    background-color: transparent;
    color: #232323;
}

QLabel#URL {
    background-color: transparent;
    color: #b91c1c;
}

QLineEdit {
    background-color: #ffffff;
    color: #232323;
    border: 1px solid #e2dcd5;
    border-radius: 10px;
    padding: 6px 12px;
}

QLineEdit:focus {
    border: 1.5px solid #b91c1c;
}

QPlainTextEdit {
    background-color: #ffffff;
    color: #232323;
    border: 1px solid #e2dcd5;
    border-radius: 20px;
    padding: 20px;
}

QPlainTextEdit:focus {
    border: 1.5px solid #b91c1c;
}

QPushButton {
    background-color: #b91c1c;
    color: #ffffff;
    border-radius: 20px;
    padding: 10px 20px;
}

QPushButton:hover {
    background-color: #991b1b;
}

QPushButton:pressed {
    background-color: #7f1d1d;
}""","""QWidget {
    background-color: #f0fdf4;
}

QLabel#phrase {
    background-color: transparent;
    color: #14532d;
}

QLabel#URL {
    background-color: transparent;
    color: #059669;
}

QLineEdit {
    background-color: #ffffff;
    color: #064e3b;
    border: 1px solid #bbf7d0;
    border-radius: 10px;
    padding: 6px 12px;
}

QLineEdit:focus {
    border: 1.5px solid #10b981;
}

QPlainTextEdit {
    background-color: #ffffff;
    color: #064e3b;
    border: 1px solid #bbf7d0;
    border-radius: 20px;
    padding: 20px;
}

QPlainTextEdit:focus {
    border: 1.5px solid #10b981;
}

QPushButton {
    background-color: #059669;
    color: #ffffff;
    border-radius: 20px;
    padding: 10px 20px;
}

QPushButton:hover {
    background-color: #047857;
}

QPushButton:pressed {
    background-color: #065f46;
}""","""QWidget {
    background-color: #f8f7fc;
}

QLabel#phrase {
    background-color: transparent;
    color: #2e1065;
    font-weight: bold;
}

QLabel#URL {
    background-color: transparent;
    color: #7c3aed;
}

QLineEdit {
    background-color: #ffffff;
    color: #1e1b4b;
    border: 1px solid #ddd6fe;
    border-radius: 10px;
    padding: 6px 12px;
}

QLineEdit:focus {
    border: 1.5px solid #7c3aed;
}

QPlainTextEdit {
    background-color: #ffffff;
    color: #1e1b4b;
    border: 1px solid #ddd6fe;
    border-radius: 20px;
    padding: 20px;
}

QPlainTextEdit:focus {
    border: 1.5px solid #7c3aed;
}

QPushButton {
    background-color: #7c3aed;
    color: #ffffff;
    border-radius: 20px;
    padding: 10px 20px;
}

QPushButton:hover {
    background-color: #6d28d9;
}

QPushButton:pressed {
    background-color: #5b21b6;
}"""], "dark" : ["""
                        QLabel#phrase {
                            background-color : gray;
                            color : black
                        }
                        QLabel#URL {
                            background-color : gray;
                            color : white
                        }
                        QWidget {
                            background-color : gray
                        }
                        QLineEdit {
                            background-color : white;
                            color : black;
                            border-radius : 10px;
                            padding : 5px 10px;
                        }
                        QPlainTextEdit {
                            background-color : white;
                            color : black;
                            border-radius : 20px;
                            padding : 20px 20px
                        }
                        QPushButton {
                            background-color : darkred;
                            color : white;
                            border-radius : 20px;
                        }
                        """,
                """QLabel#phrase {
                            background-color : #0f172a;
                            color : #f8fafc
                        }
                        QLabel#URL {
                            background-color : #0f172a;
                            color : #38bdf8
                        }
                        QWidget {
                            background-color : #0f172a
                        }
                        QLineEdit {
                            background-color : #1e293b;
                            color : #f8fafc;
                            border-radius : 10px;
                            padding : 5px 10px;
                        }
                        QPlainTextEdit {
                            background-color : #1e293b;
                            color : #f8fafc;
                            border-radius : 20px;
                            padding : 20px 20px
                        }
                        QPushButton {
                            background-color : #0284c7;
                            color : #ffffff;
                            border-radius : 20px;
                        }""",
                """QLabel#phrase {
                            background-color : #18181b;
                            color : #fafafa
                        }
                        QLabel#URL {
                            background-color : #18181b;
                            color : #f87171
                        }
                        QWidget {
                            background-color : #18181b
                        }
                        QLineEdit {
                            background-color : #27272a;
                            color : #fafafa;
                            border-radius : 10px;
                            padding : 5px 10px;
                        }
                        QPlainTextEdit {
                            background-color : #27272a;
                            color : #fafafa;
                            border-radius : 20px;
                            padding : 20px 20px
                        }
                        QPushButton {
                            background-color : #991b1b;
                            color : #ffffff;
                            border-radius : 20px;
                        }""",
                    """QLabel#phrase {
                            background-color : #0b1912;
                            color : #ecfdf5
                        }
                        QLabel#URL {
                            background-color : #0b1912;
                            color : #34d399
                        }
                        QWidget {
                            background-color : #0b1912
                        }
                        QLineEdit {
                            background-color : #132a1e;
                            color : #ecfdf5;
                            border-radius : 10px;
                            padding : 5px 10px;
                        }
                        QPlainTextEdit {
                            background-color : #132a1e;
                            color : #ecfdf5;
                            border-radius : 20px;
                            padding : 20px 20px
                        }
                        QPushButton {
                            background-color : #059669;
                            color : #ffffff;
                            border-radius : 20px;
                        }""",
                """QLabel#phrase {
                            background-color : #130c22;
                            color : #f5f3ff
                        }
                        QLabel#URL {
                            background-color : #130c22;
                            color : #c084fc
                        }
                        QWidget {
                            background-color : #130c22
                        }
                        QLineEdit {
                            background-color : #22163b;
                            color : #f5f3ff;
                            border-radius : 10px;
                            padding : 5px 10px;
                        }
                        QPlainTextEdit {
                            background-color : #22163b;
                            color : #f5f3ff;
                            border-radius : 20px;
                            padding : 20px 20px
                        }
                        QPushButton {
                            background-color : #7e22ce;
                            color : #ffffff;
                            border-radius : 20px;
                        }"""]}
        
        self.app = app
        
        try:
            self.app.setStyleSheet(self.designs[self.type_design][self.want_design])
        except Exception as y:
            print(y)
            return y 
        
        self.window = QWidget()
        self.window.setFixedSize(1100,1000)
        self.window.setWindowTitle("QoR Code")
        
        self.layout = QFormLayout()
        
        try:
            self.logo=os.path.join(os.path.dirname(__file__),"logo.ico")
            self.window.setWindowIcon(QIcon(self.logo))
        except Exception as t:
            return t
        
        self.premier_texte = QLabel("Entre ton truc pour le QR", alignment = Qt.AlignCenter)
        self.premier_texte.setObjectName("phrase")
        
        self.plain = QPlainTextEdit()
        self.plain.setPlaceholderText("Entre ton truc à transformer")
        
        self.pour_nom = QLineEdit()
        self.pour_nom.setPlaceholderText("Entre le nom du QR")
        self.pour_nom.setFixedSize(1050,50)
        
        self.url = QLabel('<a href="https://github.com/LOCKXIOR/QR-code-generator/tree/main">Vérifier les mises à jour</a>', alignment = Qt.AlignCenter)
        self.url.setOpenExternalLinks(True)
        self.url.setObjectName("URL")
        
        self.chemin = QLabel("Prêt.")
        self.chemin.setObjectName("chemin")
        
        self.bouton = QPushButton("Transformer")
        self.bouton.setFixedSize(1050,50)
        self.bouton.clicked.connect(self.transformer)
        
        self.bouton_de_design = QPushButton("Changer de design")
        
        self.bouton_de_design.clicked.connect(self.changer_design)
        
        self.layout.addRow(self.premier_texte)
        self.layout.addRow(self.url, self.bouton_de_design)
        self.layout.addRow(self.pour_nom)
        self.layout.addRow(self.plain)
        self.layout.addRow(self.chemin)
        self.layout.addRow(self.bouton)
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
                self.chemin.setText(f"Créé dans : {os.getcwd()}")
                
            else:
                self.Generateur.transforme(truc)
                self.Generateur.enregistre(nom)
                self.chemin.setText(f"Créé dans : {os.getcwd()}")
            
        elif not self.requis(truc, nom)[0]:
            
            self._erreurs(("long",0))
            
        elif not self.requis(truc, nom)[1]:
            
            self._erreurs(("long",1))
            
        else: 
            self._erreurs(("inconnu",0))
            
    def _erreurs(self, type_erreur):
        self.message_derreur.showMessage(f"Erreur : {self.erreur[type_erreur[0]][type_erreur[1]]}")

    def requis(self,a,b):
        return (len(a) <= 2930, len(b) <= 100)
    
    def changer_design(self):
        if self.type_design == "light":
            try:
                self.want_design += 1
                self.app.setStyleSheet(self.designs[self.type_design][self.want_design])
                
            except IndexError:
                self.want_design = 0
                self.type_design = "dark"
                self.app.setStyleSheet(self.designs[self.type_design][self.want_design])
        
        else: 
            
            try:
                self.want_design += 1
                self.app.setStyleSheet(self.designs[self.type_design][self.want_design])
                
            except IndexError:
                self.want_design = 0
                self.type_design = "light"
                self.app.setStyleSheet(self.designs[self.type_design][self.want_design])
          
        
if __name__ == "__main__":
    Appli = QApplication([])
    
    
    lor = IU(Appli)
    lor.launch()