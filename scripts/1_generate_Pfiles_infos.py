__author__ = 'roca'

import rawpfile.rawpfiles_get_info_in_csv as rp

#inputs :
rawdata_dirnames = ['/mnt/POOL_IRM01/IRM01/FARM_MEG_2010/','/mnt/POOL_IRM02/IRM02/FARM/raw_data_2012',\
                    '/mnt/POOL_IRM02/IRM02/FARM/raw-data-2012','/mnt/POOL_IRM02/IRM02/FARM/raw_data_dec_2012',\
                    '/mnt/POOL_IRM02/IRM02/FARM/raw_data_2013','/mnt/POOL_IRM03/IRM03/farm/raw_data_2013',\
                    '/mnt/POOL_IRM03/IRM03/farm/raw_data_2014','/mnt/POOL_IRM03/IRM03/farm/raw_data_2015',\
                    '/mnt/POOL_IRM03/IRM03/farm/pcasl_raw_data_2015']

#outputs:

workdir = '/home/roca/Documents/projets/flow/suivi/sujet_reorga_28_07_2015/workdir3'

rp.getPfilesInfo(rawdata_dirnames, workdir)

