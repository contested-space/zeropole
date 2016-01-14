from Data import Data
from ComplexPoint import ComplexPoint

class Monomial():
  def __init__(self, coeff, exponent):
    self.coeff = coeff
    self.exponent = exponent

  def getCoeff(self):
    return self.coeff

  def getExponent(self):
    return self.exponent

  def addToCoeff(self, otherCoeff):
    self.coeff += otherCoeff

class Polynomial():
  def __init__(self, listOfMonomials):
    self.monomials = listOfMonomials

  def addMonomial(monomial):
    for m in self.monomials:
      if m.
