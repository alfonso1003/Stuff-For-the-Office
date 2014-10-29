import os

def translationCatalogueRenamer(base):
    """
    This assumes there is a "base - subdirectory - files" structure
    
    example usage:
    base = 'C:\Users\\ahernandez\\Desktop\\translationCatalogues_test'
    translationCatalogueRenamer(base)
    
    """
    # get all subdirectories from the base
    directories = os.listdir(base)
    
    # get all files in each subdirectory
    for directory in directories:
        files =  os.listdir(os.path.join(base,directory))
        
        # rename file as per the case
        for file in files:
            if file[-10:] == '_EN-US.xml':
                old_filename = os.path.join(base, directory, file)        
                japan_file = old_filename[0:len(old_filename) - 10] + '_JA.xml'
                new_filename = os.path.join(base, directory, japan_file)
                os.rename(old_filename, new_filename)
            else:
                # log all files that weren't renamed
                print file
