#!/usr/bin/env python

import wx
from ParametersPanel import ParametersPanel
from Polynomial import *




class ParametersFrame(wx.Frame):
  def __init__(self, parent, size = (300,300), pos = (0,0), data = None):
    wx.Frame.__init__(self, parent, -1, 'Parameters', size = size, pos = pos)
    panel = wx.Panel(self)
    self.createMenuBar()
    self.data = data
    self.parent = parent
    self.isFocused = True

    self.nb = wx.Notebook(panel, style=wx.NB_TOP)

    topZeroPanel = wx.Panel(self.nb)
    topPolePanel = wx.Panel(self.nb)

    self.zeroPanel = ParametersPanel(topZeroPanel, data = self.data)
    self.polePanel = ParametersPanel(topPolePanel, data = self.data)

    self.zeroSizer = wx.BoxSizer(wx.VERTICAL)
    self.poleSizer = wx.BoxSizer(wx.VERTICAL)

    self.zeroButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
    self.poleButtonSizer = wx.BoxSizer(wx.HORIZONTAL)

    

    self.addZeroButton = wx.Button(topZeroPanel, label = 'Add Zero')
    self.deleteZeroButton = wx.Button(topZeroPanel, label = 'Delete Zero')
    self.addPoleButton = wx.Button(topPolePanel, label = 'Add Pole')
    self.deletePoleButton = wx.Button(topPolePanel, label = 'Delete Pole')

    self.addZeroButton.Bind(wx.EVT_BUTTON, self.OnAddZeroButton)
    self.deleteZeroButton.Bind(wx.EVT_BUTTON, self.OnDeleteZeroButton)
    self.addPoleButton.Bind(wx.EVT_BUTTON, self.OnAddPoleButton)
    self.deletePoleButton.Bind(wx.EVT_BUTTON, self.OnDeletePoleButton)

    self.zeroComboBox = wx.ComboBox(topZeroPanel, name = 'Zeroes', choices = self.data.getZeroes())
    self.poleComboBox = wx.ComboBox(topPolePanel, name = 'Poles', choices = self.data.getPoles())


    self.zeroComboBox.Bind(wx.EVT_COMBOBOX, self.OnZeroComboBox)
    self.poleComboBox.Bind(wx.EVT_COMBOBOX, self.OnPoleComboBox)

    
    self.zeroButtonSizer.Add(self.addZeroButton, proportion = 1, flag = wx.EXPAND)
    self.zeroButtonSizer.Add(self.deleteZeroButton, proportion = 1, flag = wx.EXPAND)

    self.poleButtonSizer.Add(self.addPoleButton, proportion = 1, flag = wx.EXPAND)
    self.poleButtonSizer.Add(self.deletePoleButton, proportion = 1, flag = wx.EXPAND)    

    self.zeroSizer.Add(self.zeroComboBox, flag = wx.EXPAND)
    self.zeroSizer.Add(self.zeroButtonSizer, flag =wx.EXPAND)
    self.zeroSizer.Add(self.zeroPanel, flag =wx.EXPAND)

    self.poleSizer.Add(self.poleComboBox, flag = wx.EXPAND)
    self.poleSizer.Add(self.poleButtonSizer, flag =wx.EXPAND)
    self.poleSizer.Add(self.polePanel, flag =wx.EXPAND)


    topZeroPanel.SetSizer(self.zeroSizer)
    topZeroPanel.Fit()

    topPolePanel.SetSizer(self.poleSizer)
    topPolePanel.Fit()


    self.nb.AddPage(topZeroPanel, "Zeroes")
    self.nb.AddPage(topPolePanel, "Poles")

    self.nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChange)

    mainSizer = wx.BoxSizer(wx.VERTICAL)
    mainSizer.Add(self.nb, 1, wx.EXPAND)
    panel.SetSizer(mainSizer)
    panel.Fit()

    panel.Bind(wx.EVT_IDLE, self.OnIdle)
    panel.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
    panel.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

  def OnEnterWindow(self, event):
    self.isFocused = True
    print 'focus on'

  def OnLeaveWindow(self, event):
    self.isFocused = False
    print 'focus off'

  def OnIdle(self, event):
    if not self.isFocused:
      if self.nb.GetSelection() == 0 and self.data.getActiveMonomial() is not None:
        self.zeroPanel.updateCtrls()
        self.zeroPanel.updateSliders()
      elif self.nb.GetSelection() == 1 and self.data.getActiveMonomial() is not None:
        self.polePanel.updateCtrls()
        self.polePanel.updateSliders()
      event.Skip()

  def OnPageChange(self, event):
    if self.nb.GetSelection() == 0:
      print 'switch to page zero'
      
      print 'selected: ' + self.zeroComboBox.GetStringSelection()
      self.data.activate(self.data.getZeroByName(self.zeroComboBox.GetStringSelection()))
      print 'active name: ' + self.data.getActiveMonomial().getName()
    else:
      self.data.activate(self.data.getPoleByName(self.poleComboBox.GetStringSelection()))


  def OnZeroComboBox(self, event):
    print self.zeroComboBox.GetStringSelection()
    self.data.activate(self.data.getZeroByName(self.zeroComboBox.GetStringSelection()))
    self.zeroPanel.updateCtrls()
    self.zeroPanel.updateSliders()
    event.Skip()

  def OnPoleComboBox(self, event):
    self.data.activate(self.data.getPoleByName(self.poleComboBox.GetStringSelection()))
    self.polePanel.updateCtrls()
    self.polePanel.updateCtrls()
    event.Skip()

  def OnAddZeroButton(self, event):
    self.data.addZero(complex(0))
    #for z in self.data.getZeroes():
      #print z.getName() + 'x: ' + str(z.getReal()) + ' | y: ' + str(z.getImag())
    self.zeroComboBox.Append(self.data.getActiveMonomial().getName())
    self.zeroComboBox.Select(self.zeroComboBox.GetCount() - 1)
    self.zeroPanel.updateCtrls()
    self.zeroPanel.updateSliders()



  def OnDeleteZeroButton(self, event):
    self.zeroComboBox.Delete(self.zeroComboBox.FindString(self.data.getActiveMonomial().getName()))
    self.data.deleteActiveZero()
    self.zeroComboBox.Select(self.zeroComboBox.GetCount() - 1)
    self.data.activate(self.data.getZeroByName(self.zeroComboBox.GetSelection()))
    self.zeroPanel.updateCtrls()
    self.zeroPanel.updateSliders()


  def OnAddPoleButton(self, event):
    self.data.addPole(complex(0))
    self.poleComboBox.Append(self.data.getActiveMonomial().getName())
    self.poleComboBox.Select(self.poleComboBox.GetCount() - 1)
    self.polePanel.updateCtrls()
    self.polePanel.updateSliders()

  def OnDeletePoleButton(self, event):
    self.poleComboBox.Delete(self.poleComboBox.FindString(self.data.getActiveMonomial().getName()))
    self.data.deleteActivePole()
    self.poleComboBox.Select(self.poleComboBox.GetCount() - 1)
    self.data.activate(self.data.getPoleByName(self.poleComboBox.GetSelection()))
    self.polePanel.updateCtrls()
    self.polePanel.updateSliders()


  def menuData(self):
    return[('&File', (
      ('&New', 'New Filter File', self.OnNew),
      ('&Open', 'Open Filter File', self.OnOpen),
      ('&Save', 'Save Filter File', self.OnSave),
      ('','',''),
      ('E&xport', (
        ('&Jsfx', 'Export to JSFX plugin', self.OnExportJSFX, wx.ITEM_NORMAL),
        ('&Faust', 'Export to Faust code', self.OnExportFaust, wx.ITEM_NORMAL))),
      ('','',''),
      ('&Quit', 'Quit Program', self.OnQuit)))]

  def createMenuBar(self):
    menuBar = wx.MenuBar()
    for eachMenuData in self.menuData():
      menuLabel = eachMenuData[0]
      menuItems = eachMenuData[1]
      menuBar.Append(self.createMenu(menuItems), menuLabel)
      self.SetMenuBar(menuBar)

  def createMenu(self, menuData):
    menu = wx.Menu()
    for eachItem in menuData:
      if len(eachItem) == 2:
        label = eachItem[0]
        subMenu = self.createMenu(eachItem[1])
        menu.AppendMenu(wx.NewId(), label, subMenu)
      else:
        #print eachItem
        self.createMenuItem(menu, *eachItem)
    return menu

  def createMenuItem(self, menu, label, status, handler, kind = wx.ITEM_NORMAL):
    if not label:
      menu.AppendSeparator()
      return
    menuItem = menu.Append(-1, label, status, kind)
    self.Bind(wx.EVT_MENU, handler, menuItem)

  def OnNew(self):
    pass

  def OnOpen(self):
    pass

  def OnSave(self):
    pass


#used as test for polynomial generation for now

  #must find a way to convert ComplexPoints to Monomials before calling polynomial
  def OnExportJSFX(self, event):
    #z = Polynomial(self.data.zeroes)
    #p = Polynomial(self.data.poles)

    for z in self.data.getZeroes():
      print "data :" +  str(vars(z)) + 'data.getZeroes()'

    fract = dataToPolyFract(self.data)
    print fract

    """
    for e in fract.getNum().getMonomials():
      print str(vars(e)) + 'fract.getNum().getMonomials()' 
    for e in fract.getDen().getMonomials():
      print str(vars(e)) + 'fract.getDen().getMonomials()' 
    """


  def OnExportFaust(self):
    pass

  def OnQuit(self):
    pass



if __name__ == '__main__':
  app = wx.PySimpleApp()
  frame = ParametersFrame(None)
  frame.Show(True)
  app.MainLoop()