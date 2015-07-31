__author__ = 'roca'

import os
import bin
binPath = os.path.dirname(bin.__file__)

class PrintRawPfileHdrWriter():
    def __init__(self):
        self.pfiles_list = []
        self.out_printraw_files_list = []
        self.pfiles_nb = 0
        self.size_list = []

    def setPfileFilenameList(self,rawdata_dirname_list, exten= '.7'):
        self.pfiles_list = []
        #function to launch at each iteration of walk:
        def step(ext, dirname, names):
            ext = ext.lower()
            for name in names:
                if name.lower().endswith(ext):
                    self.pfiles_list.append(os.path.join(dirname, name))
        ## Start the walk and put in pfiles_list the list of filenames of each pfile present in the set of directories
        #rawdata_dirname_list.
        map(lambda rawdata_dir: os.path.walk(rawdata_dir, step, exten), rawdata_dirname_list)
        self.pfiles_nb = len(self.pfiles_list)
        self.setSizeOfPFilesInBytes()
        return True

    def setSizeOfPFilesInBytes(self):
        self.size_list = map(lambda path: os.path.getsize(path),self.pfiles_list)

    def writePrintRawFiles(self, directory):
        self.out_printraw_files_list = map(lambda pfilePathName: pfilePathName.replace\
        ('/','_'),self.pfiles_list)
        self.out_printraw_files_list = map(lambda pfilePathName: pfilePathName.replace\
        ('.7','.txt'),self.out_printraw_files_list)
        self.out_printraw_files_list = map(lambda pfilePathName: 'printraw' + pfilePathName\
        ,self.out_printraw_files_list)
        self.out_printraw_files_list  = map(lambda printRawFname: os.path.join(directory\
        ,printRawFname),self.out_printraw_files_list )
        printrawcmd = os.path.join(binPath,'printraw')
        for i in xrange(self.pfiles_nb):
            pfile_pathname = self.pfiles_list[i]
            ouputPrintRawFname = self.out_printraw_files_list[i]
            os.system(printrawcmd + ' ' + pfile_pathname + ">>" + ouputPrintRawFname)

    def writeFoundPfilesInfo(self, out_filename):
        wf = open(out_filename,'w')
        print >> wf, 'pfile_pathname;pfile_size_in_bytes;printraw_pfilehdr_pathname'
        for i in xrange(self.pfiles_nb):
            print >> wf, self.pfiles_list[i] +";" + str(self.size_list[i])+";"+self.out_printraw_files_list[i]
        wf.close()
        return None
