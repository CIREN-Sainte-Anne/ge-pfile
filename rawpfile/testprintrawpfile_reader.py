# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:28:16 2015

@author: roca
"""
import unittest
from rawpfile import printrawpfile_reader as prp
import os
import datatest as data

dataPath = os.path.dirname(data.__file__)

class TestPrintRawPfileHdrReader(unittest.TestCase):

    def test_setDictFromSeriesHeader(self):
        printraw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(printraw_pfile_hdr_fname)
        series_hdr_dict = rawpfile_reader.SeriesHdrDict
        self.assertEqual(True,series_hdr_dict.has_key('se_desc'))
        self.assertEqual('3DPCVIPR80',series_hdr_dict['se_desc'])
        self.assertEqual('Tue-Apr-3-13:42:25-2012',series_hdr_dict['se_actual_dt'])
        self.assertEqual('Mav',series_hdr_dict['prtcl'])

    def test_setDictFromExamHeader(self):
        print_raw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(print_raw_pfile_hdr_fname)
        dictEx = {}
        examHdrDict = rawpfile_reader.ExamHdrDict
        print examHdrDict
        self.assertEqual(type(dictEx),type(rawpfile_reader.ExamHdrDict))

    def test_setDictFromExamHeader2(self):
        printraw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(printraw_pfile_hdr_fname)
        examHdrDict = rawpfile_reader.ExamHdrDict
        self.assertEqual(True,examHdrDict.has_key('patnameff'))
        self.assertEqual(True,examHdrDict.has_key('patage'))
        self.assertEqual(True,examHdrDict.has_key('patsex'))
        self.assertEqual(True,examHdrDict.has_key('patweight'))
        self.assertEqual(True,examHdrDict.has_key('dateofbirth'))
        self.assertEqual(True,examHdrDict.has_key('ex_datetime'))
        self.assertEqual(True,examHdrDict.has_key('ex_desc'))
        self.assertEqual(True,examHdrDict.has_key('ex_verscre'))
        self.assertEqual(True,examHdrDict.has_key('ex_verscur'))
        self.assertEqual('DUPONT^JEAN',examHdrDict['patnameff'])
        self.assertEqual('Tue-Apr-3-13:07:12-2012',examHdrDict['ex_datetime'])

    def test_getValuesInStringFromExamHdrDict(self):
        print_raw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(print_raw_pfile_hdr_fname)
        outputstring = rawpfile_reader.getValuesInStringFromExamHdrDict()
        self.assertEqual(str,type(outputstring))
        self.assertEqual('DUPONT', outputstring.split(';')[0])
        self.assertEqual('JEAN', outputstring.split(';')[1])

    def test_getValuesInStringFromSeriesHdrDict(self):
        print_raw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(print_raw_pfile_hdr_fname)
        outputstring = rawpfile_reader.getValuesInStringFromSeriesHdrDict()
        self.assertEqual(str,type(outputstring))
        self.assertEqual('3DPCVIPR80', outputstring.split(';')[0])
        self.assertEqual('Tue-Apr-3-13:42:25-2012', outputstring.split(';')[1])
        self.assertEqual('Mav', outputstring.split(';')[2])

    def test_getVersionNb(self):
        printraw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(printraw_pfile_hdr_fname)
        version = rawpfile_reader.getVersionNb()
        self.assertEqual('20.006001',version)

    def test_getFormatedValuesInStringForCsvFile(self):
        printraw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(printraw_pfile_hdr_fname)
        formatedString = rawpfile_reader.getFormatedValuesInStringForCsvFile()
        self.assertEqual('DUPONT;JEAN;26;2;19850411;Tue-Apr-3-13:07:12-2012;CRANE;23;23;3DPCVIPR80;'\
                +'Tue-Apr-3-13:42:25-2012;Mav',formatedString)
        #corresponding to :'patnameff;patage;patsex;dateofbirth;ex_datetime;ex_desc;ex_verscre;ex_verscur;\
        # 'se_desc;se_actual_dt;prtcl'

    def test_getFormatedKeysInStringForCsvFile(self):
        printraw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(printraw_pfile_hdr_fname)
        formated_string = rawpfile_reader.getFormatedKeysInStringForCsvFile()
        self.assertEqual('nom;prenom;age;sex;date_de_naissance;mrscan_start_time;exam_desc;version1;version2;seq_name;'\
                         +'mrscan_end_exam;protocol',formated_string)
