import os

#prova
class DettagliFile(object):
    def __init__(self, path):
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.d_create = os.path.getctime(path)
        self.path = path

    def compare(self,other):
        if (self.name == other.name and self.size == other.size and self.d_create == other.d_create):
            return True 
        else:
            return False 

