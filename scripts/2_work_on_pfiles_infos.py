__author__ = 'roca'

import pandas

workdir = '/home/roca/Documents/projets/flow/suivi/sujet_reorga_28_07_2015/fusion'

list_of_pfiles_info_fname = os.path.join(workdir,'infos_from_pfilesheader.csv')
pfiles_df = pandas.read_csv(list_of_pfiles_info_fname,sep = ";")#,encoding='utf-8')

