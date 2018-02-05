from math import log
from random import sample
from numpy import genfromtxt
from random import randint
from copy import deepcopy
import sys

class Node:
	def __init__(self):
		self.children = {}

	def setLabel(self, label):
		self.label = label

	def setMostCommonValue(self, value):
		self.mostCommonValue = value

def readFromFile(filename):
	'''
		Reads data from a csv file
		filename : Path to file
		returns : an array of dictionary, each dictionary corresponds to a row
				in the csv file
	'''
	myData = genfromtxt(filename, delimiter=',', dtype = str)
	attributes = myData[0]
	data = []
	for row in myData[1:]:
		entry = {}
		i = 0
		for attr in attributes:
			entry[attr] = int(row[i])
			i += 1
		data.append(entry)
	return data

def splitByAttribute(examples, attribute):
	'''
		Splits a data set based on the value of an attribute
		Assumes the attribute is binary and takes values from {0, 1}
		examples : The data set
		attribute : based on the value of which the data set will be split
	'''
	split = {}
	split[0] = []
	split[1] = []
	for example in examples:
		split[example[attribute]].append(example)
	return split

def countByAttributesValue(examples, attribute):
	'''
		Returns the count of zeros and count of ones in column for the attribute
		in the data set
		examples : The data set
		attribute : The attribute whose zero and one count we need
		returns : [Number of zeroes, number of ones]
	'''
	split = [0, 0]
	for example in examples:
		split[example[attribute]] += 1
	return split

def getMostCommonValue(examples, attribute):
	'''
		Returns the value the attribute most often has in the data set
	'''
	t = 0
	split = countByAttributesValue(examples, attribute)
	if(split[0] > split[1]):
		return 0
	return 1

def entropy(examples, attribute):
	'''
		Computes the entropy of the data set on the attribute
	'''
	split = countByAttributesValue(examples, attribute)
	total = sum(split)
	ones  = split[1]
	zeros = split[0]
	entropyValue = 0
	if (ones > 0):
		entropyValue -= ((ones/total) * log(ones/total, 2))
	if (zeros > 0):
	 	entropyValue -= ((zeros/total) * log(zeros/total, 2))  

	return entropyValue

def varImpurity(examples, attribute):
	'''
		Computes the variance impurity of the data set on the attribute
	'''
	split = countByAttributesValue(examples, attribute)
	total = sum(split)
	if(total == 0):
		return 0
	ones  = split[1]
	zeros = split[0]
	return (ones / total) * (zeros / total)

def gainFromAttribute(examples, entropyTotal, attribute, targetAttribute, heuristic):
	'''
		Computes the information gain or variance impurity gain from the attribute given
		examples : data set
		entropyTotal : total entropy of the data set
		attribute : attribute whose information gain we need to find
		targetAttribute : the target attribute for the decision tree
		heuristic : "info" for information gain, any other value for variance impurity 
	'''
	split = splitByAttribute(examples, attribute)
	total = len(examples)
	ones = split[1]
	zeros = split[0]
	e1 = 0
	e2 = 0
	if (heuristic == "info"):
		e1 = ((len(ones) / total) * entropy(ones, targetAttribute))
		e2 = ((len(zeros) / total) * entropy(zeros, targetAttribute))
	else:
		e1 = ((len(ones) / total) * varImpurity(ones, targetAttribute))
		e2 = ((len(zeros) / total) * varImpurity(zeros, targetAttribute))		
	return entropyTotal - e1 - e2

def bestClassifier(examples, targetAttribute, attributes, heuristic):
	'''
		Returns the attribute that best classifies the examples based on the heuristic given
		examples : the data set
		targetAttribute : the target attribute for the decision tree
		attribute : the candidates from which we need to find the best one
		heuristic : info for Information Gain / any other value for variance impurity
	'''
	total = 0
	if (heuristic == "info"):
		total = entropy(examples, targetAttribute)
	else:
		total = varImpurity(examples, targetAttribute)
	maxGain = 0
	bestAtt = attributes[0]
	for a in attributes:
		gain = 0
		gain = gainFromAttribute(examples, total, a, targetAttribute, heuristic)
		if (gain > maxGain):
			maxGain = gain
			bestAtt = a
	return bestAtt

def ID3(examples, targetAttribute, attributes, heuristic = "info"):
	'''
		examples = Training Set
		targetAttribute = The attribute whose value is to be
							predicted
		attributes = List of other attributes that may be tested
					 by the learned decision tree
		Returns a decision tree that correctly classifies the given examples
	'''
	root = Node()
	if (all(example[targetAttribute] == 1 for example in examples)):
		root.setLabel(1)
		return root
	if (all(example[targetAttribute] == 0 for example in examples)):
		root.setLabel(0)
		return root
	if (len(attributes) == 0):
		root.setLabel(getMostCommonValue(examples, targetAttribute))
		return root

	a = bestClassifier(examples, targetAttribute, attributes, heuristic)
	mostCommonValue = getMostCommonValue(examples, targetAttribute)
	root.setLabel(a)
	root.setMostCommonValue(mostCommonValue)
	examplesSplit = splitByAttribute(examples, a)
	for vi in [0, 1]:
		if (len(examplesSplit[vi]) == 0):
			newNode = Node()
			newNode.setLabel(mostCommonValue)
			root.children[vi] = newNode
		else:
			newAttributeList = attributes[:]
			newAttributeList.remove(a)
			root.children[vi] = ID3(examplesSplit[vi], targetAttribute, newAttributeList, heuristic)
	return root

def getNonLeafNodes(curr):
	'''
		Get non leaf nodes of a decision tree
		curr : root of the decision tree
		returns the list of non leaf nodes of a decision tree
	'''
	q = [curr]
	nodeArray = []
	count = 0
	while(len(q) != 0):
		newQ = []
		while(len(q) != 0):
			node = q.pop()
			if (len(node.children) != 0):
				nodeArray.append(node)
				count += 1
			for c in node.children:
				newQ.append(node.children[c])
		q = newQ
	return nodeArray

def postPrune(root, l, k, validationSet, targetAttribute):
	'''
		Post prune the decision tree, based on the validation set
		l = The parameter L for post pruning as specified in the Algorithm 1
		k = The parameter K for post pruning as specified in the Algorithm 1
		validationSet = The validation set on which to perform the post pruning
		targetAttribute = The target attribute of the decision tree
	'''
	dBest = root
	bestAcc = computeAccuracy(root, validationSet, targetAttribute)
	for i in range(l):
		curr = deepcopy(root)
		m = randint(1, k)
		for j in range(m):
			nodes = getNonLeafNodes(curr)
			n = len(nodes)
			if (n <= 1):
				break
			p = randint(1, n)
			node = nodes[p - 1]
			node.label = node.mostCommonValue
			node.children = []
		acc = computeAccuracy(curr, validationSet, targetAttribute)
		if(acc > bestAcc):
			bestAcc = acc
			dBest = curr
	return dBest

def printTreeHelper(root, pad):
	'''
		The helper method for pringting the decision tree
	'''
	if(root.label == 0 or root.label == 1):
		print(str(root.label))
		return
	print("")
	print(pad + str(root.label) + " = 0 :", end = " ")
	printTreeHelper(root.children[0], pad + "| ")
	print(pad + str(root.label) + " = 1 :", end = " ")
	printTreeHelper(root.children[1], pad + "| ")

def printTree(root):
	'''
		Prints the decision tree given as argument
	'''
	printTreeHelper(root, "")

def predict(root, data):
	'''
		Computes the target attribute for the data given
	'''
	curr = root
	while (curr.label != 0 and curr.label != 1):
		curr = curr.children[data[curr.label]]
	return int(curr.label)


def computeAccuracy(root, testData, targetAttribute):
	'''
		Computes the accuracy of the decision tree
	'''
	correct = 0
	for row in testData:
		predition = predict(root, row)
		actual = row[targetAttribute]
		if (predition == actual):
			correct += 1
	return correct * 100 / len(testData)


L = int(sys.argv[1])
K = int(sys.argv[2])
trainingDataFile = sys.argv[3]
validationDataFile = sys.argv[4]
testDataFile = sys.argv[5]
toPrint = False
if(sys.argv[6] == "yes"):
	toPrint = True

traningData = readFromFile(trainingDataFile)
testData = readFromFile(testDataFile)
validationData = readFromFile(validationDataFile)
attributes = list(traningData[0].keys())
attributes.remove("Class")

print("Information Gain heuristic")
print("==========================")
root = ID3(traningData, "Class", attributes)
if(toPrint):
	print("The Decision Tree")
	printTree(root)

print("Accuracy on the training set = ", end = "")
print(computeAccuracy(root, traningData, "Class"))
print("Accuracy on the validation set = ", end = "")
print(computeAccuracy(root, validationData, "Class"))
print("Accuracy on the test set = ", end = "")
print(computeAccuracy(root, testData, "Class"))

postPruned = postPrune(root, L, K, validationData, "Class")
if(toPrint):
	print("The Decision Tree after post pruning")
	printTree(postPruned)

print("Accuracy on the training set after post pruning = ", end = "")
print(computeAccuracy(postPruned, traningData, "Class"))
print("Accuracy on the validation set set after post pruning = ", end = "")
print(computeAccuracy(postPruned, validationData, "Class"))
print("Accuracy on the test set after post pruning = ", end = "")
print(computeAccuracy(postPruned, testData, "Class"))
print("==========================")

print("Variance Impurity heuristic")
print("==========================")
root = ID3(traningData, "Class", attributes, "var")
if(toPrint):
	print("The Decision Tree")
	printTree(root)

print("Accuracy on the training set = ", end = "")
print(computeAccuracy(root, traningData, "Class"))
print("Accuracy on the validation set = ", end = "")
print(computeAccuracy(root, validationData, "Class"))
print("Accuracy on the test set = ", end = "")
print(computeAccuracy(root, testData, "Class"))

postPruned = postPrune(root, L, K, validationData, "Class")
if(toPrint):
	print("The Decision Tree after post pruning")
	printTree(postPruned)

print("Accuracy on the training set after post pruning = ", end = "")
print(computeAccuracy(postPruned, traningData, "Class"))
print("Accuracy on the validationDataFile set after post pruning = ", end = "")
print(computeAccuracy(postPruned, validationData, "Class"))
print("Accuracy on the test set after post pruning = ", end = "")
print(computeAccuracy(postPruned, testData, "Class"))
print("==========================")