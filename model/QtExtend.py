from PyQt5 import QtCore, QtWidgets

# checkbox, 所屬layout, 所屬layout的level, level(string list)
class CheckboxData(object):
	def __init__(self, checkbox, layout, layoutLevel, questionLevel):
		self.checkbox = checkbox
		self.layout = layout
		self.layoutLevel = layoutLevel
		self.questionLevel = questionLevel

