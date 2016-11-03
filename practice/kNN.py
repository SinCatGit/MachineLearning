# -*- coding: utf-8 -*-
__author__ = 'sincat'

from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # print diffMat
    sqDiffMat = diffMat**2
    # print 'sqDiffMat', sqDiffMat
    sqDistance = sqDiffMat.sum(axis=1)
    # print 'sqDistance', sqDistance
    distances = sqDistance**0.5
    # print 'distances', distances

    sortedDistIndicies = distances.argsort()
    # print 'sortedDistIndicies', sortedDistIndicies
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    print "arrayOLines", arrayOLines
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    print "returnMat", returnMat
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector
