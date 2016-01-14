from Data import Data
import cmath

class Monomial():
  def __init__(self, coeff = 0, exponent = 1):
    self.coeff = coeff
    self.exponent = exponent

  def getCoeff(self):
    return self.coeff

  def getExponent(self):
    return self.exponent

  def add(self, newCoeff):
    self.coeff += newCoeff

  def sub(self, newCoeff):
    self.coeff -= newCoeff

  def mulC(self, constant):
    self.coeff *= constant

  def mulM(self, monomial):
    self.coeff *= monomial.getCoeff()
    self.exponent += monomial.getExponent()

  def differentiate(self, nbDiff = 1):
    for i in range(nbDiff):
      self.coeff *= self.exponent
      self.exponent -= 1

  def __str__(self):
    return str(self.coeff) + 'x^' + str(self.exponent)

class Polynomial():
  def __init__(self, listOfMonomials = []):
    #replace by for loop with addM for each monomial
    self.monomials = []
    for m in listOfMonomials:
      self.addM(m)
    self.sort()

  def addM(self, monomial):
    for m in self.getMonomials():
      if m.getExponent() == monomial.getExponent():
        m.add(monomial.getCoeff())
        #self.sort()
        return
    self.monomials.append(monomial)
    #self.sort()

  def addMReturn(self, monomial):
    p = Polynomial(self.monomials)
    p.addM(monomial)
    return p


    

  def getMonomials(self):
    return self.monomials

  def addP(self, polynomial):
    for m in polynomial.getMonomials():
      self.addM(m)
      #self.sort()

  def addPReturn(self, polynomial):
    p = Polynomial(self.monomials)
    p.addP(polynomial)
    return p

  #multiply polynomial by a constant
  def mulC(self, constant):
    for m in self.monomials:
      m.mulC(constant)

  def mulCReturn(self, constant):
    p = Polynomial(self.monomials)
    p.mulC(constant)
    return p


  def mulM(self, monomial):
    for m in self.monomials:
      m.mulM(monomial)
    #self.sort()

  def mulMReturn(self, monomial):
    p = Polynomial(self.monomials)
    p.mulM(monomial)
    return p

  #multiply polynomial by a factor of the form (1-bx^n)
  def mulF(self, monomial):
    p = Polynomial(self.monomials)
    p.mulM(monomial)
    print str(vars(p)) + 'mulF'
    p.mulC(-1)
    self.addP(p)
    #self.sort()

  def mulFReturn(self, monomial):
    p = Polynomial(self.monomials)
    p.mulF(monomial)
    return p

  def mulP(self, polynomial):
    #p0 = Polynomial(self.getMonomials())
    p1 = Polynomial()
    for m in polynomial.getMonomials():
      p1.addP(self.mulMReturn(m))
    self.monomials = p1.getMonomials()

  def mulPReturn(self, polynomial):
    p = Polynomial(self.monomials)
    p.mulP(polynomial)
    return p


  def sort(self):
    self.monomials = sorted(self.monomials, key = lambda x: x.getExponent())
    """
    for i in range(len(self.monomials) - 2):polynomial multiplication algorithm
      if self.monomials[i+1].getExponent() == self.monomials[i].getExponent():
        self.monomials[i].add(self.monomials[i].getCoeff())
        self.monomials.pop(i+1)
        self.sort()
    """
    


  def differentiate(self):
    for m in self.monomials:
      if m.getExponent == 0:
        self.monomials.remove(m)
      else:
        m.differentiate()

  def __str__(self):
    s = ""
    for m in self.monomials:
      s+= str(m) + '+'

    return s[:-1]



class PolynomialFraction():
  def __init__(self, num = Polynomial([Monomial(0, 1)]), den = Polynomial([Monomial(0, 1)])):
    self.num = num
    self.den = den

  def getNum(self):
    return self.num

  def getDen(self):
    return self.den

  def __str__(self):
    return '(' + str(self.num) + ')/(' + str(self.den) + ')'





def dataToPolyFract(data):
  B = Polynomial([Monomial(1, 0)])
  A = Polynomial([Monomial(1, 0)])
  #print B.getMonomials()
  for z in data.getZeroes():
    #print str(vars(z)) + 'data.getZeroes()'
    B.mulF(Monomial(z.getComplexValue()))
    #print str(vars(B)) + 'vars(B)'

  for p in data.getPoles():
    A.mulF(Monomial(p.getComplexValue()))

  return PolynomialFraction(B, A)


if __name__ == '__main__':

  """
  mon1 = Monomial(coeff = 2, exponent = 2)
  mon2 = Monomial(coeff = 3, exponent = 1)
  mon3 = Monomial(coeff = 4, exponent = 0)
  mon4 = Monomial(coeff = 2, exponent = 2)
  
  listOfMon = [mon1, mon2, mon3, mon4]
  poly = Polynomial(listOfMon)
  print "original polynomial"
  print poly
  mon5 = Monomial(coeff = 2, exponent = 2)
  poly2 = poly.mulPReturn(poly)
  print "polynomial squared"
  print poly2
  """

  mono1 = Monomial(coeff = 1, exponent = 1)
  mono2 = Monomial(coeff = 1, exponent = 0)
  mono3 = Monomial(coeff = 1, exponent = 2)
  mono4 = Monomial(coeff = 1, exponent = 0)

  pol1 = Polynomial([mono1, mono2, mono3])
  pol2 = Polynomial([mono3])
  print pol1
  print pol2


 


  #pol1.addP(pol2)
  pol1.mulM(mono3)
  #pol1.mulP(pol2)
  print pol1




  
    


