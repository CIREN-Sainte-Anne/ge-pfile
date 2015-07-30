__author__ = 'roca'

import os

exten = '.7'
pfiles_list = []
#function to launch at each iteration of walk:
def step(ext, dirname, names):
	ext = ext.lower()
	for name in names:
		if name.lower().endswith(ext):
			pfiles_list.append(os.path.join(dirname, name))

# Start the walk and put in pfiles_list the list of filenames to each pfile
#inputs : 
rawdata_dir = '/mnt/POOL_IRM01/IRM01/FARM_MEG_2010/'
os.path.walk(rawdata_dir, step, exten)
os.path.walk('/mnt/POOL_IRM02/IRM02/FARM/raw_data_2012', step, exten)
os.path.walk('/mnt/POOL_IRM02/IRM02/FARM/raw-data-2012', step, exten)
os.path.walk('/mnt/POOL_IRM02/IRM02/FARM/raw_data_dec_2012', step, exten)
os.path.walk('/mnt/POOL_IRM02/IRM02/FARM/raw_data_2013', step, exten)
os.path.walk('/mnt/POOL_IRM03/IRM03/farm/raw_data_2013', step, exten)
os.path.walk('/mnt/POOL_IRM03/IRM03/farm/raw_data_2014', step, exten)
os.path.walk('/mnt/POOL_IRM03/IRM03/farm/raw_data_2015', step, exten)
os.path.walk('/mnt/POOL_IRM03/IRM03/farm/pcasl_raw_data_2015', step, exten)

#len(pfiles_list):
#2199
size_list = map(lambda path: os.path.getsize(path),pfiles_list)
pfiles_nb = len(pfiles_list)

##############
#outputs:
##############
workdir = '/home/roca/Documents/projets/flow/suivi/sujet_reorga_28_07_2015/\
read_pfiles_header'
printrawPfilesDir = os.path.join(workdir,'pfilesheader')
os.mkdir(printrawPfilesDir)

#1. File with the list of all pfiles in the previous POOLS and the size of the
# associated files : 
outPfilesPaths_fname = os.path.join(workdir,"pfile_path_and_size_29_07_2015_\
.csv")
wf = open(outPfilesPaths_fname,'w')
print >> wf, 'pathname;size_in_bytes'
for i in xrange(pfiles_nb):
    print >> wf, pfiles_list[i] +";" + str(size_list[i])
wf.close()

# 2. Generate "printraw files: header of the Pfile' (total number of files:2199
printrawcmdfname = os.path.join(workdir,'printraw')
ouputPrintRawFnames = map(lambda pfilePathName: pfilePathName.replace\
('/','_'),pfiles_list)
ouputPrintRawFnames = map(lambda pfilePathName: pfilePathName.replace\
('.7','.txt'),ouputPrintRawFnames)
ouputPrintRawFnames = map(lambda pfilePathName: 'printraw' + pfilePathName\
,ouputPrintRawFnames)
ouputPrintRawFnames = map(lambda printRawFname: os.path.join(printrawPfilesDir\
,printRawFname),ouputPrintRawFnames)
for i in xrange(pfiles_nb):
    pfile_pathname = pfiles_list[i]
    ouputPrintRawFname = ouputPrintRawFnames[i]
    cmd=printrawcmdfname + ' ' + pfile_pathname + ">>" + ouputPrintRawFname
    os.system(cmd)



