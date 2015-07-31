__author__ = 'roca'

from rawpfile import printrawpfile_reader as prp
from rawpfile import printrawpfile_writer as prpw
import os

def searchAndWritePfilesInfoAndHdr(rawdata_dirnames, printrawPfilesDir, found_pfiles_csv_fname):
    w = prpw.PrintRawPfileHdrWriter()
    w.setPfileFilenameList(rawdata_dirnames)
    w.writePrintRawFiles(printrawPfilesDir)
    w.writeFoundPfilesInfo(found_pfiles_csv_fname)
    return w

def getPfilesInfo(rawdata_dirnames, workdir):
    '''
    - 1 - search for all file ending with '.7' in a set of directories (rawdata_dirnames)
    - apply printraw command (in bin) to all found pfiles in order to extract for each pfile its header.
    - generate a csv file with for each line: <path to the pfile>; <size of the pfile in bytes>;,
    <header of pfile pathname>, name of csv file: 'found_pfiles.csv'
    - write the header of each pfile in a file in a specific directory (previous <header of pfile pathname>)
    - 2 - generate a csv with information from all previous pfile headers (one line per pfile) :
    "infos_from_pfilesheader.csv"
    '''
    printrawpfiles_hdr_dir = os.path.join(workdir,'pfilesheader')
    found_pfiles_csv_fname = os.path.join(workdir,'found_pfiles.csv')
    output_csv_fname = os.path.join(workdir,'infos_from_pfilesheader.csv')
    os.mkdir(workdir)
    os.mkdir(printrawpfiles_hdr_dir)
    w = searchAndWritePfilesInfoAndHdr(rawdata_dirnames, printrawpfiles_hdr_dir, found_pfiles_csv_fname)

    f = open(output_csv_fname,"w")
    reader = prp.PrintRawPfileHdrReader()
    print >> f, reader.getFormatedKeysInStringForCsvFile() + ";pfile_name;pfile_hdr_fname;size_in_bytes"
    for i in xrange(w.pfiles_nb):
        rawPfile_reader = prp.PrintRawPfileHdrReader(w.out_printraw_files_list[i])
        print >> f, rawPfile_reader.getFormatedValuesInStringForCsvFile() +";" + w.pfiles_list[i] + ";"\
                         + w.out_printraw_files_list[i] + ';' + str(w.size_list[i])
    f.close()
