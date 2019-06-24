import wx  #sample of move event

class Sample(wx.App):
    def OnInit(self):
        frame=wx.Frame(None,title="Sample",size=(400,400))
        frame.Show(False)  # Make the frame invisible.
        frame.Hide()  # Equivalent to frame.Show(False).
        frame.Show(True)  # True is the default parameter value.
        return True

app = Sample()
app.MainLoop()