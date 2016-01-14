import wx
from ParametersFrame import ParametersFrame
from GraphFrame import *
from ZeroPoleFrame import ZeroPoleFrame
from ComplexPoint import ComplexPoint
from Data import Data

class ZeroPoleApp(wx.PySimpleApp):
  def __init__(self):
    wx.PySimpleApp.__init__(self)
    self.data = Data()
    self.parametersFrame = ParametersFrame(None, size = (wx.DisplaySize()[0]/5, wx.DisplaySize()[1]), pos = (0,0), data = self.data)
    self.magnitudeGraphFrame = GraphMagnitude(None, size = (wx.DisplaySize()[0]/4, wx.DisplaySize()[1]*2/5),pos = (wx.DisplaySize()[0]*3/4, 0), data = self.data)
    self.phaseGraphFrame = GraphPhase(None,size = (wx.DisplaySize()[0]/4, wx.DisplaySize()[1]*2/5), pos = (wx.DisplaySize()[0]*3/4, wx.DisplaySize()[1]/2), data = self.data)
    self.zeroPoleFrame = ZeroPoleFrame(None, size = (wx.DisplaySize()[0]/2, wx.DisplaySize()[1]), pos = (wx.DisplaySize()[0]/5, 0), data = self.data)




    self.parametersFrame.Show()
    self.magnitudeGraphFrame.Show()
    self.phaseGraphFrame.Show()
    self.zeroPoleFrame.Show()

  def getData(self):
    return self.data

if __name__ == '__main__':
  app = ZeroPoleApp()
  app.MainLoop()
