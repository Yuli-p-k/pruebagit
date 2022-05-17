print("Subiendo a github")

class Cuenta: 
  def __init__(self, titular, cantidad=0): 
    self.titular = titular 
    self.cantidad = cantidad
  def mostrar(self):
    print ("El titular ", self.titular, " tiene el saldo de: ", self.cantidad,)
    
  def ingresar(self,dinero=0):
    self.dinero=dinero
    if dinero >= 0:
      self.cantidad += self.dinero
      print("Usted ingreso", self.dinero, "y el saldo es:", self.cantidad)
      
  def retirar(self,resta=0):
    self.resta=resta
    self.cantidad -= self.resta
    print("Usted retiro", self.resta, "y el saldo es:", self.cantidad)

    
      
Pers1 = Cuenta("Yuliana Parmucci", 2110)
Pers1.mostrar()
Pers1.ingresar(1505)
Pers1.retirar(120)
