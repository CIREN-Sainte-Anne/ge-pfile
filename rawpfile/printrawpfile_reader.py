# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:27:11 2015

@author: roca
"""
import re


class PrintRawPfileHdrReader():
    def __init__(self,printrawPfileHdr_fname):
        self.printrawPfileHdr_fname = printrawPfileHdr_fname
        file = open(printrawPfileHdr_fname, 'r')
        self.printrawPfileHdr = file.read()
        file.close()
        self.paragraphList = None
        self.SeriesHdrDict = None
        self.ExamHdrDict = None
        self.setParagraphList()
        self.setDictFromExamHeader()
        self.setDictFromSeriesHeader()

    def setParagraphList(self):
        self.paragraphList = re.split(r'\n{2,}', self.printrawPfileHdr)
        # paragraph_list format:
        # 7 elements
        # paragraph_list[0] : version and encoding parameters
        # paragraph_list[3] : Prescan header
        # paragraph_list[4] : exam header : interesting

    def paragraphToDict(self, paragraph):
        one_header = paragraph
        one_header_list = re.split(r'\n{1,}', one_header)
        one_header_list = [ re.sub(r'\t', '', line) for line in one_header_list ]
        matchObjList = map(lambda line: re.match(r'(.*) = (.*)',line),one_header_list)
        dictObj = {}
        for matchObj in matchObjList:
            if matchObj!= None:
                dictObj[matchObj.group(1)] = matchObj.group(2)
        if dictObj.has_key('ex_datetime'):
            dictObj['ex_datetime'] = dictObj['ex_datetime'].replace(' ','-')
            dictObj['ex_datetime'] = dictObj['ex_datetime'].replace('--','-')
        for key in dictObj.keys():
            dictObj[key] = dictObj[key].replace(' ','')
        return dictObj

    def setDictFromSeriesHeader(self):
        series_header = self.paragraphList[5]
        series_header_list = re.split(r'\n{1,}', series_header)
        series_header_list = [ re.sub(r'\t', '', line) for line in series_header_list ]
        self.SeriesHdrDict = series_header_list

    def setDictFromExamHeader(self):
        exam_header = self.paragraphList[4]
        exam_header_list = re.split(r'\n{1,}', exam_header)
        exam_header_list = [ re.sub(r'\t', '', line) for line in exam_header_list ]
        matchObjList = map(lambda line: re.match(r'(.*) = (.*)',line),exam_header_list)
        dictObj = {}
        for matchObj in matchObjList:
            if matchObj!= None:
                dictObj[matchObj.group(1)] = matchObj.group(2)
        if dictObj.has_key('ex_datetime'):
            dictObj['ex_datetime'] = dictObj['ex_datetime'].replace(' ','-')
            dictObj['ex_datetime'] = dictObj['ex_datetime'].replace('--','-')
        for key in dictObj.keys():
            dictObj[key] = dictObj[key].replace(' ','')
        self.ExamHdrDict = dictObj

    def getValuesInString(self,list_of_keys=['patnameff','patage','patsex', 'dateofbirth', 'ex_datetime',\
                                                      'ex_desc','ex_verscre','ex_verscur'], delimiter = ";"):
        output_string = ""
        for key in list_of_keys:
            if self.ExamHdrDict.has_key(key):
                if key == 'patnameff':
                    output_string += self.ExamHdrDict[key].replace("^",delimiter) + delimiter
                else:
                    output_string += self.ExamHdrDict[key] + delimiter
            else:
                output_string += delimiter
        return output_string

    def getVersionNb(self):
        global_header = self.paragraphList[0]
        global_header_list = re.split(r'\n{1,}', global_header)
        version_info = global_header_list[0]
        version_nb = version_info.split(',')[1].split('=')[1].replace(' ','')
        return version_nb

