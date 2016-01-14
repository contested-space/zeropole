import wx
import math
import sys
from ComplexPoint import ComplexPoint

class ParametersPanel(wx.Panel):
  def __init__(self, parent, title = "", data = None, SR = 48000):
    wx.Panel.__init__(self, parent, id = -1, name =title)

    self.x = 0
    self.y = 0
    self.norm = 0;
    self.angle = 0
    self.frequency = 0
    self.data = data
    self.SR = SR

    self.stable = True

    self.sliderMaxValue = int(pow(2, sys.getsizeof(int())))
    print sys.getsizeof(int())
    print self.sliderMaxValue

    self.xySlidersMin = -self.sliderMaxValue/2
    self.xySlidersMax = self.sliderMaxValue/2
    self.normSliderMin = 0
    self.normSliderMax = self.sliderMaxValue
    self.angleSliderMin = 0
    self.angleSliderMax = self.sliderMaxValue
    self.frequencySliderMin = 0
    self.frequencySliderMax = self.SR/2



    self.mainBox = wx.BoxSizer(wx.VERTICAL)
    #self.comboBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
    self.xyBox = wx.BoxSizer(wx.VERTICAL)
    self.normAngleBox = wx.BoxSizer(wx.VERTICAL)
    self.frequencyBox = wx.BoxSizer(wx.VERTICAL)

    #self.comboBox = wx.ComboBox(self, name = '')

    self.xText = wx.StaticText(self, label= "x:")
    self.yText = wx.StaticText(self, label= "y:")
    self.xCtrl = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
    self.yCtrl = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
    self.xSlider = wx.Slider(self, minValue = self.xySlidersMin, maxValue = self.xySlidersMax)
    self.ySlider = wx.Slider(self, minValue = self.xySlidersMin, maxValue = self.xySlidersMax)

    self.normText = wx.StaticText(self, label = 'Norm:')
    self.angleText = wx.StaticText(self, label = 'Angle')
    self.normCtrl = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
    self.angleCtrl = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)

    self.normSlider = wx.Slider(self, minValue = self.normSliderMin, maxValue = self.normSliderMax)
    self.angleSlider = wx.Slider(self, minValue = self.angleSliderMin, maxValue = self.angleSliderMax)

    self.frequencyText = wx.StaticText(self, label='Center Frequency')
    self.frequencyCtrl = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER)
    self.frequencySlider = wx.Slider(self, minValue = self.frequencySliderMin, maxValue = self.frequencySliderMax)


    self.xCtrl.SetValue('0')
    self.yCtrl.SetValue('0')
    self.normCtrl.SetValue('0')
    self.angleCtrl.SetValue('0')
    self.frequencyCtrl.SetValue('0')

    self.xCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnXEnter)
    self.yCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnYEnter)
    self.normCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnNormEnter)
    self.angleCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnAngleEnter)
    self.frequencyCtrl.Bind(wx.EVT_TEXT_ENTER, self.OnFrequencyEnter)

    self.xSlider.Bind(wx.EVT_SCROLL, self.OnXScroll)
    self.ySlider.Bind(wx.EVT_SCROLL, self.OnYScroll)
    self.normSlider.Bind(wx.EVT_SCROLL, self.OnNormScroll)
    self.angleSlider.Bind(wx.EVT_SCROLL, self.OnAngleScroll)
    self.frequencySlider.Bind(wx.EVT_SCROLL, self.OnFrequencyScroll)

    #self.comboBoxSizer.Add(self.comboBox)

    self.xyBox.Add(self.xText, flag = wx.EXPAND)
    self.xyBox.Add(self.xSlider, flag = wx.EXPAND)
    self.xyBox.Add(self.xCtrl, flag = wx.EXPAND)
    self.xyBox.Add(self.yText, flag = wx.EXPAND)
    self.xyBox.Add(self.ySlider, flag = wx.EXPAND)
    self.xyBox.Add(self.yCtrl, flag = wx.EXPAND)

    self.normAngleBox.Add(self.normText, flag = wx.EXPAND)
    self.normAngleBox.Add(self.normSlider, flag = wx.EXPAND)

    self.normAngleBox.Add(self.normCtrl, flag = wx.EXPAND)
    self.normAngleBox.Add(self.angleText, flag = wx.EXPAND)
    self.normAngleBox.Add(self.angleSlider, flag = wx.EXPAND)
    self.normAngleBox.Add(self.angleCtrl, flag = wx.EXPAND)

    self.frequencyBox.Add(self.frequencyText, flag = wx.EXPAND)
    self.frequencyBox.Add(self.frequencySlider, flag = wx.EXPAND)
    self.frequencyBox.Add(self.frequencyCtrl, flag = wx.EXPAND)

    #self.mainBox.Add(self.comboBoxSizer)
    self.mainBox.Add(self.xyBox, flag = wx.EXPAND)
    self.mainBox.Add(self.normAngleBox, flag = wx.EXPAND)
    self.mainBox.Add(self.frequencyBox, flag = wx.EXPAND)

    self.SetSizer(self.mainBox)
    self.Fit()

  def OnXScroll(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      value = float(event.GetPosition())/self.xySlidersMax
      self.data.activeMonomial.setReal(value)
      self.updateCtrls()
      #print self.xCtrl.GetValue()
      #self.xCtrl.SetValue(str(value))
    event.Skip()

  def OnYScroll(self, event):    
    if self.data.activeMonomial is None:
      pass
    else:
      value = float(event.GetPosition())/self.xySlidersMax
      self.data.activeMonomial.setImag(value)
      self.updateCtrls()
      self.updateSliders()
      #self.yCtrl.SetValue(str(value))
    event.Skip()

  def OnNormScroll(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setModulus(float(event.GetPosition())/self.sliderMaxValue)
      self.updateCtrls()
      self.updateSliders()
    event.Skip()
  def OnAngleScroll(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setPhase(float(event.GetPosition())/self.angleSliderMax * 2 *math.pi )
      self.updateCtrls()
      self.updateSliders()
    event.Skip()
  def OnFrequencyScroll(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setCenterFrequency(event.GetPosition())
      self.updateCtrls()
      self.updateSliders()
    event.Skip()
  
  def updateSliders(self):
    if self.data.activeMonomial is not None:
      self.xSlider.SetValue(self.data.activeMonomial.getReal() * self.xySlidersMax)
      self.ySlider.SetValue(self.data.activeMonomial.getImag() * self.xySlidersMax)
      self.normSlider.SetValue(self.data.activeMonomial.getModulus() * self.normSliderMax)
      self.angleSlider.SetValue(int(self.data.activeMonomial.getPhase() * self.angleSliderMax/(2 * math.pi)))
      self.frequencySlider.SetValue(self.data.activeMonomial.getCenterFrequency())

  def updateCtrls(self):
    if self.data.activeMonomial is not None:
      self.xCtrl.SetValue(str(self.data.activeMonomial.getReal()))
      self.yCtrl.SetValue(str(self.data.activeMonomial.getImag()))
      self.normCtrl.SetValue(str(self.data.activeMonomial.getModulus()))
      self.angleCtrl.SetValue(str(self.data.activeMonomial.getPhase()))
      self.frequencyCtrl.SetValue(str(self.data.activeMonomial.getCenterFrequency()))

  #use : SetSelection(-1,-1)
  #to highlight the selection. maybe map shift+clickBox to automatically highlight ?
  #might have to deal with focus stuff

  def OnXEnter(self, event):
    #self.normCtrl.SetValue(str(math.sqrt(pow(int(self.xCtrl.GetValue()), 2) + pow(int(self.yCtrl.GetValue()), 2))))
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setReal(float(self.xCtrl.GetValue()))
      #self.updateCtrls()
      self.updateSliders()
      print self.xCtrl.GetValue()
    event.Skip()

  def OnYEnter(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setImag(float(self.yCtrl.GetValue()))
      #self.updateCtrls()
    event.Skip()

  def OnNormEnter(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setModulus(float(self.normCtrl.GetValue()))
      #self.updateCtrls()
    event.Skip()

  def OnAngleEnter(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setPhase(float(self.angleCtrl.GetValue()))
      #self.updateCtrls()
    event.Skip()

  def OnFrequencyEnter(self, event):
    if self.data.activeMonomial is None:
      pass
    else:
      self.data.activeMonomial.setCenterFrequency(float(self.frequencyCtrl.GetValue()))
      #self.updateCtrls()
    event.Skip()


    
