import wget
import xml.etree.ElementTree as ET
import time
import os.path
import os

run_loop = True
#file_number = 290290 #starting file # for KDE
file_number = 396643 #starting file # for Gentoo
#file_number = 739078 #starting file # for SUSE
#file_prefix = 'KDE'
file_prefix = 'Gentoo'
#file_prefix = 'SUSE'

while run_loop:
    print('Downloading bug #' + str(file_number) + '.')
    #url = 'https://bugs.kde.org/show_bug.cgi?ctype=xml&id=' + str(file_number) #url to use when downloading KDE
    url = 'https://bugs.gentoo.org/show_bug.cgi?ctype=xml&id=' + str(file_number) #url to use when downloading from Gentoo
    #url = 'https://bugzilla.suse.com/show_bug.cgi?ctype=xml&id=' + str(file_number) #url to use when downloading from SUSE
    if not os.path.isfile(file_prefix+'Bug'+str(file_number)+'.xml'):
        filename = wget.download(url, file_prefix+'Bug'+str(file_number)+'.xml', bar=None)
        tree = ET.parse(filename)
        root = tree.getroot()
        if root[0][0] is None:
            print('Invalid bug, deleting.')
            os.remove(filename)
        elif root[0].attrib == {'error': 'InvalidBugId'}:
            print('Invalid bug, deleting.')
            os.remove(filename)
        else:
            print('Valid bug downloaded.')
        time.sleep(2)
    '''
        if file_number > 515900: #ending number for KDE
            run_loop = False 
    '''
    if file_number > 969900: #ending number for Gentoo
        run_loop = False
    '''
        if file_number > 1258020: #ending number for SUSE
            run_loop = False 
    '''
    file_number+=1