from Gen_QR_build26102026 import GénérateurQR
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import QIcon
import os
import json

class IU:
    def __init__(self, app):
        
        self.erreur = {"vide" : ["La case pour QR est vide","Il n'y a pas de nom, enregistré sous abréviation"], "long" : ["Le message est trop long (max 2930)","le nom est trop long (max 100)"], "inconnu" : ["Comment tu t'es débrouillié ?"]}
        self.message_derreur = QErrorMessage()
        
        self.Generateur = GénérateurQR("Transformer en QRcode")
        
        self.want_design = None
        self.type_design = "light"
        
        
        self.designs = {}
        self._ensemble = {}
        
        self.app = app
        self.charger() 
        
        self.window = QWidget()
        self.window.setFixedSize(1100,1000)
        self.window.setWindowTitle("QoR Code")
        
        self.layout = QFormLayout()
        
        try:
            self.logo=os.path.join(os.path.dirname(__file__),"logo-removebg-preview.ico")
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
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])
                
            except KeyError:
                self.want_design = 0
                self.type_design = "dark"
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])

            except IndexError:
                self.want_design = 0
                self.type_design = "dark"
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])
                        
        else: 
            
            try:
                self.want_design += 1
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])
                
            except KeyError:
                self.want_design = 0
                self.type_design = "light"
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])
                
            except IndexError:
                self.want_design = 0
                self.type_design = "light"
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])

        try :
            self.sauvegarde()
        except Exception as ale:
            print(ale)
        
    def sauvegarde(self):
        try:
            self._ensemble["endroit"] = self.want_design
            kk = json.dumps(self._ensemble)
            with open("design.json", "w", encoding="utf-8") as f:
                json.dump(kk, f, indent=2, ensure_ascii=True)
                
        except Exception as ee:
            print(ee)   
        
    def charger(self):
        try:
            with open("design.json", "r", encoding="utf-8") as ff:
                tempo = json.load(ff)
                tempo1 = json.loads(tempo)
                
            self._ensemble = tempo1

            
            try:
                self.want_design = int(self._ensemble["endroit"])
                self.app.setStyleSheet(self._ensemble["desinal"][self.type_design][self.want_design])
            except Exception as y:
                print(y)
                return y 
            
        except Exception as el:
            print(el)
        
                
if __name__ == "__main__":
    Appli = QApplication([])
    
    
    lor = IU(Appli)
    lor.launch()