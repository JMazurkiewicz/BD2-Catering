#!/usr/bin/env python
# @author Damian Piotrowski

from model.addextracostsmodel import ExtraCostsModel
import tkinter as tk
from model.newproductmodel import NewProductModel
from view.formview import FormView

class ExtraCostsView(FormView):

    def __init__(self, parent, controller):
        FormView.__init__(self, parent, controller)

        self.add_entry('cost').set_description('Cost')
        self.add_entry('cause').set_description('Cause')

        self.save_button = tk.Button(self, text='Save')
        self.save_button.configure(command=self.on_save_click)
        self.go_back_button = tk.Button(self, text='Main menu')
        self.go_back_button.configure(command=self.controller.display_control_panel)

        self.__build_grid()

        self.set_model(ExtraCostsModel())

    def __build_grid(self):
        self.entry_frame.grid(column=0, row=0)
        self.save_button.grid(column=1, row=1)
        self.go_back_button.grid(column=0, row=1)

    def on_save_click(self):
        cost = self.get_input('cost')
        cause = self.get_input('cause')
        self.get_model().add_extra_cost(cost, cause)

