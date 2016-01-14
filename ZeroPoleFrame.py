import wx
import cmath
from ComplexPoint import ComplexPoint

class ZeroPoleFrame(wx.Frame):
  def __init__(self, parent, title = "", size = (800,600), pos = (0,0), isReal = True, data = None):
    wx.Frame.__init__(self, parent, -1, title = title, size=size, pos=pos)
    panel = wx.Panel(self)
    panel.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Bind(wx.EVT_SIZE, self.OnSize)
    self.size = size
    self.data = data
    self.isReal = isReal
    if data is None:
      self.zeroes = []
      self.poles = []
    else:
      self.zeroes = data.getZeroes()
      self.poles = data.getPoles()
    self.circleSize = min([self.size[0], self.size[1]])/3

    panel.Bind(wx.EVT_LEFT_UP, self.OnClick)

    panel.Bind(wx.EVT_IDLE, self.OnIdle)

  def OnIdle(self, event):
    self.Refresh()
    event.Skip()



  def setZeroes(self, zeroes):
    self.zeroes = setZeroes
    self.Refresh()

  def setPoles(self, poles):
    self.poles = poles
    self.Refresh()

  def drawGraph(self, event = None):
    dc = wx.PaintDC(event.GetEventObject())
    dc.Clear()
    dc.SetPen(wx.Pen("black", 2))

      #dc.DrawLine(i, self.size[1] - graphList[i]*self.size[1]/10,i + 1,   self.size[1] - graphList[i+1]*self.size[1]/10)
      #dc.DrawPoint(i, self.size[1] - graphList[i]*self.size[1]/10)

    self.circleSize = min([self.size[0], self.size[1]])/3

    dc.DrawCircle(self.Size[0]/2, self.Size[1]/2, self.circleSize)
    dc.SetPen(wx.Pen("blue", 1))
    dc.DrawLine(self.Size[0]/2, 0, self.Size[0]/2, self.Size[1])
    dc.DrawLine(0, self.Size[1]/2, self.Size[0], self.Size[1]/2)
    self.drawMonomials(dc, event)
    event.Skip()

  def OnClick(self, event):
    if self.data.getActiveMonomial() is not None:
      self.data.getActiveMonomial().setReal(float(event.GetX() - self.size[0]/2)/self.circleSize)
      self.data.getActiveMonomial().setImag(-float(event.GetY() - self.size[1]/2)/self.circleSize)
    self.Refresh()
    event.Skip()

  def OnSize(self, event):
    self.size = event.GetSize()
    self.drawGraph(event)
    self.Refresh()
    event.Skip()

  def drawPole(self, x, y, dc, event):
    monomialSize = self.circleSize/30
    dc.DrawLine(self.size[0]/2 + x * self.circleSize - monomialSize, self.size[1]/2 - y * self.circleSize + monomialSize,
      self.size[0]/2 + x * self.circleSize + monomialSize, self.size[1]/2 - y * self.circleSize - monomialSize)
    dc.DrawLine(self.size[0]/2 + x * self.circleSize + monomialSize, self.size[1]/2 - y * self.circleSize + monomialSize,
      self.size[0]/2 + x * self.circleSize - monomialSize, self.size[1]/2 - y * self.circleSize - monomialSize)
    event.Skip()

  def drawZero(self, x, y, dc, event):
    monomialSize = self.circleSize/30
    dc.DrawCircle(self.size[0]/2 + x * self.circleSize, self.size[1]/2 - y * self.circleSize, monomialSize)
    event.Skip()


  def drawPoles(self, dc, event):
    for p in self.poles:
      if p.isActive():
        dc.SetPen(wx.Pen("red", 3))
      else:
        dc.SetPen(wx.Pen("black", 2))
      self.drawPole(p.getReal(), p.getImag(), dc, event)

  def drawZeroes(self, dc, event):
    #print self.zeroes
    for z in self.zeroes:
      if z.isActive():
        dc.SetPen(wx.Pen("red", 3))
      else:
        dc.SetPen(wx.Pen("black", 2))
      self.drawZero(z.getReal(), z.getImag(), dc, event)
      #print 'loop:drawZeroes()'
    #print 'drawZeroes end'

  def drawMonomials(self, dc, event):
    self.drawPoles(dc, event)
    self.drawZeroes(dc, event)
    #print 'drawMonomials()'

  def OnPaint(self, event = None):
    self.drawGraph(event)

if __name__ == '__main__':
  #print 'absolute start'
  app = wx.PySimpleApp()
  #print 'start'
  frame = ZeroPoleFrame(None)
  #print 'end ZeroFrame Construction'
  zer = [ComplexPoint(complex(0, 0)), ComplexPoint(complex(1.0/2, 1.0/2))]
  pol = [ComplexPoint(complex(-1.0/2, -1.0/2))]
  frame.setZeroes(zer)
  frame.setPoles(pol)
  #print 'executed'
  frame.Show()
  app.MainLoop()