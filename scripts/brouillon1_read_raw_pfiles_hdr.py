# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:30:35 2015

@author: roca
"""


import os # operating system module
import re # regular expression module

workdir = '/home/roca/Documents/projets/flow/suivi/sujet_reorga_28_07_2015/\
read_pfiles_header'
os.chdir(workdir)


##ex: (from http://www.thegeekstuff.com/2014/07/python-regex-examples/)
rawProfiles = '''
... Tim Fake, 1982/03/21, I like to
... eat, sleep and
... relax
... 
... Lisa Test, 1990/05/12, I like long
... walks of the beach, watching sun-sets,
... and listening to slow jazz
... '''

profilesList = re.split(r'\n{2,}', rawProfiles)
#profilesLis2t = re.split(r'\n{1,}', rawProfiles)
profilesList = [ re.sub(r'\n', ' ', profile) for profile in profilesList ]

#autre exemple:
contactInfo = 'Doe, John: 555-1212'
re.search(r'\w+, \w+: \S+', contactInfo)
match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
match.group(1)
#'Doe'
match.group(2)
#'John'
match.group(3)
#'555-1212'
# Reading of the complet pfile header #
file = open(os.path.join(workdir,'printraw.txt'), 'r')
all_file = file.read()
file.close()
paragraph_list = re.split(r'\n{2,}', all_file)
# paragraph_list format: 
# 7 elements
# paragraph_list[0] : version and encoding parameters
# paragraph_list[3] : Prescan header
# paragraph_list[4] : exam header : interesting
exam_header = paragraph_list[4]
exam_header_list = re.split(r'\n{1,}', exam_header)
exam_header_list = [ re.sub(r'\t', '', line) for line in exam_header_list ]
matchObjList = map(lambda line: re.match(r'(.*) = (.*)',line),exam_header_list)
dictObj = {}
for matchObj in matchObjList:
    if matchObj!= None:
        dictObj[matchObj.group(1)] = matchObj.group(2)

