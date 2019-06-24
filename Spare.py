import wx

#!/usr/bin/env python
"""Spare.py is a starting point for a wxPython program."""
import wx
class Frame(wx.Frame):
      pass
class App(wx.App):
   def OnInit(self):
     self.frame = Frame(None, title='Spare')
     self.frame.Show()
     self.SetTopWindow(self.frame)
     return True

app = App()
app.MainLoop()