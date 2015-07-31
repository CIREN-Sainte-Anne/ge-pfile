Scripts:
  - 1_generate_printrawPfileshdr.py :
    - search for all file ending with '.7' in a set of directories
    - generate a csv file with for each line: <path to the pfile>; <size of the pfile in bytes>
    - apply printraw command (in bin) to all found pfiles in order to extract for each pfile its header.
    - write the header of each pfile in a file in a specific directory
  - 2_read_printrawPfilehdr.py :
    - generate a csv with information from all previous pfile headers (one line per pfile)