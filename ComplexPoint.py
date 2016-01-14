import math
import cmath

class ComplexPoint():

  def __init__(self, pos = complex(0,0), SR = 48000, name = ""):
    self.pos = pos
    self.SR = SR #sample rate
    self.centerFrequency = self.SR/math.pi * self.getPhase()
    self.name = name
    self.active = False
    self.conjugate = None
    #self.crumb = True #used to stop recursion on operations that affect both a monomial and it's conjugate

  def isActive(self):
    return self.active

  def setActive(self, isactive):
    self.active = isactive


  def getName(self):
    return self.name

  def getComplexValue(self):
    return self.pos

  def getReal(self):
    return self.pos.real

  def getImag(self):
    return self.pos.imag

  def getModulus(self):
    return cmath.polar(self.pos)[0]

  def getPhase(self):
    return cmath.polar(self.pos)[1]

  def getCenterFrequency(self):
    return self.centerFrequency

  def setConjugate(self, complexpoint):
    self.conjugate = complexpoint

  def generateConjugate(self):
    self.conjugate = ComplexPoint(complex(self.pos.real, -self.pos.imag), SR = self.SR, name = self.name + '*')
    return self.conjugate

  def getConjugate(self):
    return self.conjugate

  def setName(self, name):
    self.name = name


  def setComplexValue(self, newValue):
    self.pos = newValue
    self.centerFrequency = (self.SR/2)/math.pi * self.getPhase()
    if self.conjugate is not None:
      self.conjugate.setComplexValue(newValue)
      self.conjugate.setImag(-self.pos.imag)

  def setReal(self, newReal):
    self.pos = complex(newReal, self.pos.imag)
    self.centerFrequency = (self.SR/2)/math.pi * self.getPhase()
    if self.conjugate is not None:
      self.conjugate.setReal(newReal)

  def setImag(self, newImag):
    self.pos = complex(self.pos.real, newImag)
    self.centerFrequency = (self.SR/2)/math.pi * self.getPhase()
    if self.conjugate is not None:
      self.conjugate.setImag(-newImag)

  def setModulus(self, newModulus):
    self.pos = cmath.rect(newModulus, self.getPhase())
    if self.conjugate is not None:
      self.conjugate.setModulus(newModulus)

  def setPhase(self, newPhase):
    self.pos = cmath.rect(self.getModulus(), newPhase)
    self.centerFrequency = (self.SR/2)/math.pi * self.getPhase()
    if self.conjugate is not None:
      self.conjugate.setPhase(-newPhase)

  def setCenterFrequency(self, newFreq):
    self.setComplexValue(cmath.rect(self.getModulus(), newFreq * math.pi /(self.SR/2)))
    if self.conjugate is not None:
      self.conjugate.setCenterFrequency(-newFreq)

  def __str__(self):
    return self.name + " " + str(self.pos)



if __name__ == '__main__':
  z = ComplexPoint(complex(0.5, 0.5))
  print z
  print z.getReal()
  print z.getImag()
  print z.getPhase()
  print z.getModulus()
  print z.getCenterFrequency()



  z.setPhase(0)
  print z
  print z.getReal()
  print z.getImag()
  print z.getPhase()
  print z.getModulus()
  print z.getCenterFrequency() 