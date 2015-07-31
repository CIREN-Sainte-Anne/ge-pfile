# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:27:11 2015

@author: roca
"""
import re


class PrintRawPfileHdrReader():
    def __init__(self,printrawPfileHdr_fname = None):
        self.printrawPfileHdr_fname = printrawPfileHdr_fname
        self.printrawPfileHdr = None
        self.paragraphList = None
        self.SeriesHdrDict = None
        self.ExamHdrDict = None
        self.ExamHeaderListOfKeysToExtract = ['patnameff','patage','patsex', 'dateofbirth', 'ex_datetime',\
                                                      'ex_desc','ex_verscre','ex_verscur']
        self.ExamHeaderListOfKeysToExtractGoodNames = 'nom;prenom;age;sex;date_de_naissance;mrscan_start_time;'\
                'exam_desc;version1;version2'
        self.SeriesHeaderListOfKeysToExtract = ['se_desc','se_actual_dt','prtcl']
        self.SeriesHeaderListOfKeysToExtractGoodNames = 'seq_name;mrscan_end_exam;protocol'

        if self.printrawPfileHdr_fname:
            file = open(printrawPfileHdr_fname, 'r')
            self.printrawPfileHdr = file.read()
            file.close()
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
        for key in dictObj.keys():
            if key == 'ex_datetime' or key == 'se_actual_dt':
                dictObj[key] = dictObj[key].replace(' ','-')
                dictObj[key] = dictObj[key].replace('--','-')
            else:
                dictObj[key] = dictObj[key].replace(' ','')
        return dictObj

    def setDictFromExamHeader(self):
        if len(self.paragraphList)>=5:
            self.ExamHdrDict = self.paragraphToDict(self.paragraphList[4])

    def setDictFromSeriesHeader(self):
        if len(self.paragraphList)>=6:
            self.SeriesHdrDict = self.paragraphToDict(self.paragraphList[5])

    def getValuesInStringFromExamHdrDict(self, delimiter = ";"):
        output_string = ""
        for key in self.ExamHeaderListOfKeysToExtract:
            if self.ExamHdrDict:
                if self.ExamHdrDict.has_key(key):
                    if key == 'patnameff':
                        if self.ExamHdrDict[key].count('^'):
                            output_string += self.ExamHdrDict[key].replace("^",delimiter) + delimiter
                        else:
                            if self.ExamHdrDict[key]== "":
                                output_string += 'Nan' + delimiter + 'NaN' + delimiter
                            else:
                                output_string += self.ExamHdrDict[key] + delimiter + 'NaN' + delimiter
                    elif self.ExamHdrDict[key]== "":
                        output_string += 'NaN' + delimiter
                    else:
                        output_string += self.ExamHdrDict[key] + delimiter
                else:
                    if key == 'patnameff':
                        output_string += 'NaN' + delimiter + 'Nan' + delimiter
                    else:   output_string += 'NaN' + delimiter
            else:
                output_string += 'NaN' + delimiter
        if not self.ExamHdrDict:
            output_string += 'NaN' + delimiter
        return output_string[:-1]

    def getValuesInStringFromSeriesHdrDict(self, delimiter = ";"):
        output_string = ""
        for key in self.SeriesHeaderListOfKeysToExtract:
            if self.SeriesHdrDict:
                if self.SeriesHdrDict.has_key(key):
                    output_string += self.SeriesHdrDict[key] + delimiter
                else:
                    output_string += 'NaN' + delimiter
            else:
                output_string += delimiter
        return output_string[:-1]

    def getVersionNb(self):
        global_header = self.paragraphList[0]
        global_header_list = re.split(r'\n{1,}', global_header)
        version_info = global_header_list[0]
        version_nb = version_info.split(',')[1].split('=')[1].replace(' ','')
        return version_nb

    def getFormatedValuesInStringForCsvFile(self):
        return self.getValuesInStringFromExamHdrDict() + ";" + self.getValuesInStringFromSeriesHdrDict()

    def getFormatedKeysInStringForCsvFile(self):
        return self.ExamHeaderListOfKeysToExtractGoodNames +";" + self.SeriesHeaderListOfKeysToExtractGoodNames






