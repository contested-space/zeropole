import cmath
from ComplexPoint import ComplexPoint


class Data():
  def __init__(self, isRealFilter = True):
    self.poles = []
    self.zeroes = []
    self.isRealFilter = isRealFilter
    self.activeMonomial = None
    self.numForZero = 0
    self.numForPole = 0


  #very ugly way to find the conjugate
  def getActiveConjugate(self):
    pass

  def setActiveMonomial(self, complexpoint):
    if self.activeMonomial is not None:
      self.activeMonomial.setActive(False)
    self.activeMonomial = complexpoint
    complexpoint.setActive(True)

  def getActiveMonomial(self):
    return self.activeMonomial

  def getZeroByName(self, name):
    for i in range(len(self.zeroes) - 1):
      if self.zeroes[i].getName() == name:
        return self.zeroes[i]

  def getPoleByName(self, name):
    for i in range(len(self.poles) - 1):
      if self.poles[i].getName() == name:
        return self.poles[i]

  def isReal(self):
    return self.isRealFilter

  def getPoles(self):
    return self.poles

  def getZeroes(self):
    return self.zeroes

  def generateZeroName(self):
    n = 'z_' + str(self.numForZero)
    self.numForZero += 1
    return n

  def generatePoleName(self):
    n = 'p_' + str(self.numForPole)
    self.numForPole += 1
    return n


  def deleteActiveZero(self):

    for z in self.zeroes:
      if z == self.activeMonomial:
        if self.isRealFilter:
          self.zeroes.remove(z.getConjugate())

        self.zeroes.remove(z)
    self.ActiveMonomial = None

  def deleteActivePole(self):
    for p in self.poles:
      if p == self.activeMonomial:
        if self.isRealFilter:
          self.poles.remove(p.getConjugate())
        self.poles.remove(p)
    self.ActiveMonomial = None    


  def addPole(self, pole, name = None):
    newname = self.generatePoleName()
    newPole = ComplexPoint(pole, name = newname)
    self.activate(newPole)
    self.poles.append(newPole)
    if self.isRealFilter == True:
      conjugate = newPole.generateConjugate()
      self.poles.append(conjugate)


  def addZero(self, zero, name = None):
    newname = self.generateZeroName()
    newZero = ComplexPoint(zero, name = newname)
    self.activate(newZero)
    self.zeroes.append(newZero)
    if self.isRealFilter == True:
      conjugate = newZero.generateConjugate()
      self.zeroes.append(conjugate)

  def activate(self, monomial):
    if monomial is None:
      if self.activeMonomial is not None:
        self.activeMonomial.setActive(False)
        self.activeMonomial = monomial

    elif self.activeMonomial is not None:
      self.activeMonomial.setActive(False)
      self.activeMonomial = monomial
      self.activeMonomial.setActive(True)
    else:
      self.activeMonomial = monomial
      self.activeMonomial.setActive(True)



  def deletePole(self, complexpoint):
    for p in self.poles:
      if id(p) == id(complexpoint):
        self.poles.remove(p)

  def deleteZero(self, complexpoint):
    for p in self.zeroes:
      if id(p) == id(complexpoint):
        self.zeroes.remove(p)

