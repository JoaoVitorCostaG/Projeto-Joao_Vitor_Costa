class ClasseA:
  a1 = ''
  a2 = ''
  
  def __init__ (self, a1p, a2p):
    self.a1 = int (a1p)
    self.a2 = float (a2p)
   
  def setA1(self, valor):
    self.a1 = int(valor)
  
  def getA1(self):
    return self.a1
    
  def setA2(self, valor):
    self.a2 = int(valor)
  
  def getA2(self):
    return self.a2
  
  def MA1(self):
    print("Você está no método MA1")
    
  def MA2(self):
    print("Você está no método MA2")

  def MA3(self):
    print("Alteração a classe A partir do clone")
