# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:27:11 2015

@author: roca
"""
import re

class PrintrawPfileHdrReader():
    def __init__(self,printrawPfileHdr_fname):
        self.printrawPfileHdr_fname = printrawPfileHdr_fname
        file = open(printrawPfileHdr_fname, 'r')
        self.printrawPfileHdr = file.read()
        file.close()
        self.ExamHdrDict = None
        
    def setDictFromExamHeader(self):
        paragraph_list = re.split(r'\n{2,}', self.printrawPfileHdr)
        # paragraph_list format: 
        # 7 elements
        # paragraph_list[0] : version and encoding parameters
        # paragraph_list[3] : Prescan header
        # paragraph_list[4] : exam header : interesting
        exam_header = paragraph_list[4]
        exam_header_list = re.split(r'\n{1,}', exam_header)
        exam_header_list = [ re.sub(r'\t', '', line) for line in exam_header_list ]
        matchObjList = map(lambda line: re.match(r'(.*) = (.*)',line),exam_header_list)
        dictObj = {}
        for matchObj in matchObjList:
            if matchObj!= None:
                dictObj[matchObj.group(1)] = matchObj.group(2)
        self.ExamHdrDict = dictObj
