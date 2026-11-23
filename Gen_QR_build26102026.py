import qrcode

class GénérateurQR :
    def __init__(self, _nom = "GénérateurQR"):
        
        self._nom = _nom
        self.type_image_connu = ["jpeg", "png", "jpg"]
        self.fait = False
    
    def nom(self):
        return self._nom
    
    def ajouter_type_image(self, élément_type):
        try :
            if élément_type.lower().replace(" ","") not in self.type_image_connu:
                self.type_image_connu.append(élément_type.lower().replace(" ",""))
            else :
                return "Déjà présent"
        except Exception as at_e:
            return at_e
    
    def transforme(self, truc):
        self.qr = qrcode.make(truc)
        self.fait = True
        return self.qr
    
    def enregistre(self, nom, type_image = "png"):
        if self.fait == True:
            try :
                im = type_image.lower().replace(" ","")
                if im in self.type_image_connu :
                    image = self.qr.get_image()
                    if im in ["jpg","jpeg"]:
                        
                        image = image.convert("RGB")
                    image.save(f"{nom}.{im}")
                    return "Done"
                else:
                    return "Impossible"
            except Exception as en_e:
                return en_e
        else :
            return "Aucun Qr à enregistrer"
