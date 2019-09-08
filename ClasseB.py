class ClasseB:
  b1 = ''
  b2 = ''
  
  def __init__ (self, b1p, b2p):
    self.b1 = int (b1p)
    self.b2 = float (b2p)
   
  def setB1(self, valor):
    self.b1 = int(valor)
  
  def getB1(self):
    return self.b1
    
  def setB2(self, valor):
    self.b2 = int(valor)
  
  def getB2(self):
    return self.b2
  
  def MB1(self):
    print("Você está no método MB1")
    
  def MB2(self):
    print("Você está no método MB2")

  
