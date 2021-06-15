#!/usr/bin/env python
# @author Jakub Mazurkiewicz

from view import MainWindow
import os

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    
    window = MainWindow()
    window.mainloop()
    