import arcpy
import pythonaddins

class Existing(object):
    """Implementation for pythonaddin_addin.existing (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class Future(object):
    """Implementation for pythonaddin_addin.future (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass