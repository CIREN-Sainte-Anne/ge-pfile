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


    def test_getValuesInString(self):
        print_raw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(print_raw_pfile_hdr_fname)
        outputstring = rawpfile_reader.getValuesInString()
        self.assertEqual(str,type(outputstring))
        self.assertEqual('DUPONT', outputstring.split(';')[0])
        self.assertEqual('JEAN', outputstring.split(';')[1])

    def test_getVersionNb(self):
        printraw_pfile_hdr_fname = os.path.join(dataPath,'printraw.txt')
        rawpfile_reader = prp.PrintRawPfileHdrReader(printraw_pfile_hdr_fname)
        version = rawpfile_reader.getVersionNb()
        self.assertEqual('20.006001',version)
