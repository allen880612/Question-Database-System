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
	def __init__(self, QDSLevel):
		self.QDSLevel = QDSLevel
		self.node_count = 0
		self.head_node = QLTNode(-1, "None", False, [], weight=self.node_count)

	def CreateTree(self):
		# 重建樹
		self.DeleteTree()
		self.head_node = QLTNode(-1, "None", False, [], weight=self.node_count)

		noselect_list = self.QDSLevel.get("NOSELECT", False)
		head = self.head_node
		depth = 0

		# 建第一層
		for nodename in noselect_list:
			qList = [nodename]
			self.node_count += 1
			new_node = QLTNode(0, nodename, False, [nodename], weight=self.node_count, isShow=True)
			head.AddNode(new_node)
			self.AddNode(new_node, qList, depth)

	# 從指定科目下建造樹
	def CreateTreeBySubject(self, subject):
		# 重建樹
		self.DeleteTree()
		noselect_list = self.QDSLevel.get("NOSELECT", False)

		if (noselect_list == False):
			self.CreateTree()
			return

		if (subject in noselect_list):
			print("???")
			self.head_node = QLTNode(-1, subject, False, [subject], weight=self.node_count)
			head = self.head_node
			subject_list = self.QDSLevel.get(subject, False)
			depth = 0
			# 建第一層
			for nodename in subject_list:
				qList = [subject, nodename]
				self.node_count += 1
				new_node = QLTNode(0, nodename, False, [subject, nodename], weight=self.node_count, isShow=True)
				head.AddNode(new_node)
				self.AddNode(new_node, qList, depth)
		else:
			self.CreateTree()

	# 在node下 再加一個node, questionLsit, depth
	def AddNode(self, node, questionList, depth):
		cb_list = self.QDSLevel.get(self.GetQuestionLevelTupleKey(questionList), False)

		if cb_list == False:
			return

		for node_name in cb_list:
			temp_qList = copy.deepcopy(questionList) # 先把上一層的list temp起來
			temp_qList.append(node_name)
			self.node_count += 1
			new_node = QLTNode(depth + 1, node_name, False, temp_qList, weight=self.node_count, isShow=False)
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
	
	# 刪除此樹
	def DeleteTree(self):
		if self.head_node is None:
			del self.head_node # 直接刪除首節點，我不知道這樣垃圾回收會不會做事
		#self.DeleteTree_DFS(self.head_node)

	# ↑ DFS
	def DeleteTree_DFS(self, node):
		if len(node.childList) == 0:
			return

		for nodes in node:
			DeleteTree_DFS(nodes)
			del nodes
		node.childList.clear()

	# 設置顆樹所有的節點的isShow & Check State
	def SetTreeCheckShow(self, node, isShow):
		node.isShow = isShow
		node.isCheck = isShow
		for child in node.childList:
			self.SetTreeCheckShow(child, isShow)

	# 得到所有葉節點
	def GetAllCheckedLeafNode(self):
		node_list = []
		self.GetAllCheckedLeafNode_DFS(self.head_node, node_list)
		return node_list

	# DFS↑
	def GetAllCheckedLeafNode_DFS(self, node, node_list):
		# 為葉節點
		if len(node.childList) == 0 and node.isCheck == True:
			node_list.append(node)
			return

		for nodes in node.childList:
			self.GetAllCheckedLeafNode_DFS(nodes, node_list)

	# 取得 篩選comboboxView.GetDictValue 用的tuple key
	def GetQuestionLevelTupleKey(self, questionLevel):
		if len(questionLevel) == 1:
			return questionLevel[0]
		else:
			return tuple(questionLevel)

# Question Level Tree - Node
# (depth = 深度, name = 題目階層名, ischeck = 是否有被勾選, questionLevel = 題目階層 (含自己))
class QLTNode(object):
	def __init__(self, depth, name, ischeck, questionLevel, weight=0, isShow=False):
		self.childList = []
		self.depth = depth
		self.name = name
		self.isCheck = ischeck
		self.questionLevel = questionLevel
		self.isShow = isShow
		self.weight = weight

	def AddNode(self, node):
		self.childList.append(node)

	def GetQuestionLevelExcludeSelf(self):
		returner = copy.deepcopy(self.questionLevel)
		returner.pop()
		return returner