def translationCatalogueRenamer():
    import os

    base = 'C:\Users\\ahernandez\\Desktop\\translationCatalogues_test'

    directories = os.listdir(base)

    for directory in directories:
        files =  os.listdir(os.path.join(base,directory))
        
        for file in files:
            if file[-10:] == '_EN-US.xml':
                old_filename = os.path.join(base, directory, file)        
                japan_file = old_filename[0:len(old_filename) - 10] + '_JA.xml'
                new_filename = os.path.join(base, directory, japan_file)
                os.rename(old_filename, new_filename)
            else:
                print file