

import math
import cmath
from ComplexPoint import ComplexPoint

def graphMagnitude(zeroes = [], poles = [], size = 100, isReal = True):
  graphList = []
  for i in range(size):
    if isReal:
      p = cmath.exp(cmath.pi * complex(0, 1) * i/size)
    else:
      p = cmath.exp(cmath.pi * complex(0, 1) * (i - size/2)/size)

    B = 1
    A = 1

    for j in zeroes:
      B *= math.sqrt(pow(p.real - j.getReal(), 2) + pow(p.imag - j.getImag(), 2))

    for k in poles:
      A *= math.sqrt(pow(p.real - k.getReal(), 2) + pow(p.imag - k.getImag(), 2))

    graphList.append(B/A)
  return graphList

def graphPhase(zeroes = [], poles = [], size = 100, isReal = True):
  graphList = []
  for i in range(size):
    if isReal:
      p = cmath.exp(cmath.pi * complex(0, 1) * i/size)
    else:
      p = cmath.exp(cmath.pi * complex(0, 1) * (i - size/2)/size)

    B = 0
    A = 0
    for j in zeroes:
      B += cmath.polar(p - j.getComplexValue())[1]
      #print i
      #print j.getComplexValue()

    for k in poles:
      A += cmath.polar(p - k.getComplexValue())[1]

    phase = B-A

    """
    while phase < -math.pi:
      phase += math.pi

    while phase > math.pi:
      phase -= math.pi
    """


    graphList.append(phase)
  return graphList



if __name__ == '__main__':
  testZeroes = []
  testPoles = []
  for i in range(1):
    b = ComplexPoint(complex(1.0, 0)) 
    testZeroes.append(b)
    #a = ComplexPoint(complex(1.0/(2*i+1),1.0/(2*i+1) ))
    #testPoles.append(a)


  mylist = graphPhase(zeroes = testZeroes, poles = testPoles)
  for num in mylist:
    print num
