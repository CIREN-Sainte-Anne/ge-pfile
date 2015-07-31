__author__ = 'roca'

import unittest
from rawpfile import printrawpfile_writer as prpw
import os
import datatest as data

dataPath = os.path.dirname(data.__file__)

class TestPrintRawPfileWriter(unittest.TestCase):

    def test_generatePfileFilenameList(self):
        w = prpw.PrintRawPfileHdrWriter()
        w.setPfileFilenameList([dataPath])
        pfile_fname_list = w.pfiles_list
        self.assertEqual('P40448.7',os.path.basename(pfile_fname_list[0]))

    def test_writePrintRawFiles(self):
        w = prpw.PrintRawPfileHdrWriter()
        w.setPfileFilenameList([dataPath])
        w.writePrintRawFiles(dataPath)
        fname = os.path.join(dataPath,'printraw' +dataPath.replace('/','_') + '_P40448.txt')
        self.assertEqual(fname,w.out_printraw_files_list[0])