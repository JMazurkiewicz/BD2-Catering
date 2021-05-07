#!/usr/bin/env python
import view
import wx

if __name__ == '__main__':
    app = wx.App()
    frame = view.MainFrame()
    frame.Show()
    app.MainLoop()
