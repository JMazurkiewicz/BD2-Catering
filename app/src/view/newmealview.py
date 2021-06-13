#!/usr/bin/env python
# @author Damian Piotrowski

import tkinter as tk
from view.formview import FormView

class NewMealView(FormView):

    def __init__(self, parent):
        FormView.__init__(self, parent)

        self.add_entry('ingridient').set_description('Ingridient')

        self.entry_frame.grid(column=0, row=1, rowspan=2)