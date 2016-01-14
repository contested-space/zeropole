import wx
from ComplexPoint import ComplexPoint
import Functions
import cmath



class GraphMagnitude(wx.Frame):
  def __init__(self, parent, title = "Magnitude Response", size = (800,600), pos = (0,0), isReal = True, data = None):
    wx.Frame.__init__(self, parent, -1, title = title, size=size, pos=pos)
    panel = wx.Panel(self)
    panel.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Bind(wx.EVT_SIZE, self.OnSize)
    self.data = data
    if self.data is not None:
      self.zeroes = self.data.getZeroes()
      self.poles = self.data.getPoles()
    else:
      self.zeroes = []
      self.poles = []
    self.size = size
    self.isReal = True
    self.Bind(wx.EVT_IDLE, self.OnIdle)

  def OnIdle(self, event):
    self.Refresh()
    event.Skip()

  def updatePoleZeroLists(self):
    self.setZeroes(self.data.getZeroes())
    self.setPoles (self.data.getPoles())

  def setReal(self, isreal = True):
    self.isReal = isreal

  def setComplex(self, isreal = False):
    self.isReal = isreal

  def setZeroes(self, zeroes):
    self.zeroes = zeroes

  def setPoles(self, poles):
    self.poles = poles

  def drawGraph(self, event = None):
    self.updatePoleZeroLists()
    graphList = Functions.graphMagnitude(self.zeroes, self.poles, self.size[0], self.isReal)
    dc = wx.PaintDC(event.GetEventObject())
    dc.Clear()
    dc.SetPen(wx.Pen("BLACK", 2))
    for i in range(len(graphList)-1):
      dc.DrawLine(i, self.size[1] - graphList[i]*self.size[1]/10,i + 1,   self.size[1] - graphList[i+1]*self.size[1]/10)
      #dc.DrawPoint(i, self.size[1] - graphList[i]*self.size[1]/10)
    if not self.isReal:
      dc.SetPen(wx.Pen('Black', 1))
      dc.DrawLine(self.size[0]/2, 0, self.size[0]/2, self.size[1])

    #test for freq marker
    dc.SetPen(wx.Pen('blue', 1))
    freq = 440
    dc.DrawLine(int(float(self.size[0])/24000 * freq), 0, int(float(self.size[0])/24000 * freq),  self.size[1])
    #print int(float(self.size[0])/24000 * freq * self.size[0])
    #print self.size[0]

  def OnSize(self, event):
    self.size = event.GetSize()
    self.drawGraph(event)
    self.Refresh()
    event.Skip()


  def OnPaint(self, event = None):
    self.drawGraph(event)
  
class GraphPhase(wx.Frame):
  def __init__(self, parent, title = "Phase Response", size = (800,600), pos = (0,0), isReal = True, data = None):
    wx.Frame.__init__(self, parent, -1, title = title, size=size, pos=pos)
    panel = wx.Panel(self)
    panel.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Bind(wx.EVT_SIZE, self.OnSize)
    self.data = data

    if self.data is not None:
      self.zeroes = self.data.getZeroes()
      self.poles = self.data.getPoles()
    else:
      self.zeroes = []
      self.poles = []
    self.size = size
    self.isReal = True

    self.Bind(wx.EVT_IDLE, self.OnIdle)

  def OnIdle(self, event):
    self.Refresh()
    event.Skip()

  def updatePoleZeroLists(self):
    self.setZeroes(self.data.getZeroes())
    self.setPoles (self.data.getPoles())

  def setReal(self, isreal = True):
    self.isReal = isreal

  def setZeroes(self, zeroes):
    self.zeroes = zeroes

  def setPoles(self, poles):
    self.poles = poles

  def drawGraph(self, event = None):
    self.updatePoleZeroLists()
    graphList = Functions.graphPhase(self.zeroes, self.poles, self.size[0], self.isReal)
    dc = wx.PaintDC(event.GetEventObject())
    dc.Clear()
    dc.SetPen(wx.Pen("BLACK", 2))
    for i in range(len(graphList)-1):
      dc.DrawLine(i, self.size[1]/2 - graphList[i]*self.size[1]/40    ,i + 1,   self.size[1]/2 - graphList[i+1]*self.size[1]/40     )
      #print graphList[i]
      #dc.DrawPoint(i, self.size[1] - graphList[i]*self.size[1]/10)
    dc.SetPen(wx.Pen('Black', 1))
    dc.DrawLine(0, self.size[1]/2, self.size[0], self.size[1]/2)
    if not self.isReal:
      dc.DrawLine(self.size[0]/2, 0, self.size[0]/2, self.size[1])

  def OnSize(self, event):
    self.size = event.GetSize()
    self.drawGraph(event)
    self.Refresh()
    event.Skip()


  def OnPaint(self, event = None):
    self.drawGraph(event)  


if __name__ == '__main__':

  zer = []
  pol = []
  point = ComplexPoint(complex(1/2.0, 1.0/2))
  point2 = ComplexPoint(complex(1.0/3, -1.0/2))

  pol.append(point)
  pol.append(point.getConjugate())
  zer.append(point2)
  zer.append(point2.getConjugate())

  """
  for i in range(2):
    b = ComplexPoint(complex(1.0/(i+1), 0))
    #a = ComplexPoint(complex(0.1, 0.1/(pow(i + 1, 2))))
    zer.append(b)
    pol.append(a)
 """
  app = wx.PySimpleApp()

  frameM = GraphMagnitude(None, size = (400, 400))
  frameM.setReal(False)
  frameM.Show()
  frameM.setZeroes(zer)
  frameM.setPoles(pol)

  frameP = GraphPhase(None, size = (400, 400), pos = (450, 0))
  frameP.setReal(False)
  frameP.Show()
  frameP.setZeroes(zer)
  frameP.setPoles(pol)
  app.MainLoop()

