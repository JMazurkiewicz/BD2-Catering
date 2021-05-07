import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title = "Catering")
        
        panel = wx.Panel(self)

        text = wx.StaticText(panel, label = 'Hello catering')
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        panel.SetSizer(sizer)

        self.make_menu_bar()

        
    def make_menu_bar(self):
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(help_menu, '&Help')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)


    def OnExit(self, event):
        self.Close(True)


    def OnAbout(self, event):
        wx.MessageBox('Robocza aplikacja', "BD2", wx.OK | wx.ICON_INFORMATION)
