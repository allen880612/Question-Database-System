from PyQt5 import QtCore, QtWidgets
import copy

# checkbox, 所屬layout, 所屬layout的level, level(string list)
class CheckboxData(object):
	def __init__(self, checkbox, layout, layoutLevel, questionLevel):
		self.checkbox = checkbox
		self.layout = layout
		self.layoutLevel = layoutLevel
		self.questionLevel = questionLevel

# Question Level Tree
# (None -> 數學 & 國文etc, 數學 -> 應用題, XX題 etc)
class QLT(object):
	def __init__(self, cbView):
		self.fuck = ""
		self.comboboxView = cbView
		self.head_node = QLTNode(-1, "None", False, [])

	def CreateTree(self):
		noselect_list = self.comboboxView.GetDictValue("NOSELECT")
		head = self.head_node
		# 建第一層
		for nodename in noselect_list:
			head.AddNode(QLTNode(0, nodename, False, [nodename], True))

		depth = 0

		# 建之後的層
		for node in head.childList:
			qList = [node.name]
			self.AddNode(node, qList, depth)

	# 在node下 再加一個node, questionLsit, depth
	def AddNode(self, node, questionList, depth):
		cb_list = self.comboboxView.GetDictValue(self.GetQuestionLevelTupleKey(questionList))

		if cb_list == False:
			return

		for node_name in cb_list:
			temp_qList = copy.deepcopy(questionList) # 先把上一層的list temp起來
			temp_qList.append(node_name)
			new_node = QLTNode(depth + 1, node_name, False, temp_qList)
			node.AddNode(new_node)
			self.AddNode(new_node, temp_qList, depth + 1)

	def DFS(self):
		for node in self.head_node.childList:
			self.DFSRun(node)

	def DFSRun(self, node):
		print(node.questionLevel, node.depth)
		# print(node.questionLevel, str(node.depth))
		if len(node.childList) == 0:
			#print(node.questionLevel)
			return

		for nodes in node.childList:
			self.DFSRun(nodes)

	# 藉由Level 取得Node Return QLT Node
	def GetNodeByLevel(self, depth):
		return_QTL_node = []
		for node in self.head_node.childList:
			self.GetNodeByLevel_DFS(node, depth, return_QTL_node)
		return return_QTL_node
		
	# ↑DFS
	def GetNodeByLevel_DFS(self, node, search_depth, return_QTL_list):
		if node.depth == search_depth:
			return_QTL_list.append(node)
			return

		for child in node.childList:
			self.GetNodeByLevel_DFS(child, search_depth, return_QTL_list)
	
	# 用題目階層得到Node
	def GetNodeByQuestionLevel(self, questionLevel):
		return self.GetNodeByQuestionLevel_DFS(self.head_node, questionLevel)

	# ↑DFS
	def GetNodeByQuestionLevel_DFS(self, node, questionLevel):
		# 這一顆真的很棒，找到了
		if node.questionLevel == questionLevel:
			print("Find", node.questionLevel)
			return node

		# 確定name 有在題目階層內 > 不再就不搜尋這棵樹ㄌ (以及避開head)
		if (node.name in questionLevel) or node.depth == -1:
			for nodes in node.childList:
				get_node = self.GetNodeByQuestionLevel_DFS(nodes, questionLevel)
				if get_node:
					return get_node

	# 設置顆樹所有的節點的isShow & Check State
	def SetTreeCheckShow(self, node, isShow):
		node.isShow = isShow
		node.isCheck = isShow
		for child in node.childList:
			self.SetTreeCheckShow(child, isShow)

	# 取得 篩選comboboxView.GetDictValue 用的tuple key
	def GetQuestionLevelTupleKey(self, questionLevel):
		if len(questionLevel) == 1:
			return questionLevel[0]
		else:
			return tuple(questionLevel)

# Question Level Tree - Node
# (depth = 深度, name = 題目階層名, ischeck = 是否有被勾選, questionLevel = 題目階層 (含自己))
class QLTNode(object):
	def __init__(self, depth, name, ischeck, questionLevel, isShow=False):
		self.childList = []
		self.depth = depth
		self.name = name
		self.isCheck = ischeck
		self.questionLevel = questionLevel
		self.isShow = isShow

	def AddNode(self, node):
		self.childList.append(node)

