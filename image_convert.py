## Import procedure
import PIL
from PIL import Image
import os,sys

# picture dimensions
baseWidth = 74
maxHeight = 134

# list of allowed pictures
suffix = ['jpg','png']
listOfImages = []
listOfImagesThumbnail = []

# get the current path
root_path = os.getcwd()

listOfPaths = ['\\Data\\70X134H96\\Test\\neg\\','\\Data\\70X134H96\\Test\\pos\\']

def convertPicturesInOrder(listOfPath): 

    for data_path in listOfPath:
        # Creation procedure
        files = os.listdir(root_path + data_path)

        for index in range(len(files)):

            pictureFile = files[index]
            wordLen = len(pictureFile)

                
            # check if the picture suffix is within allowed list
            if pictureFile[wordLen-3:wordLen].lower() in suffix: 
                if 'cnv' not in pictureFile:
                    # Save every occurrence of image
                    listOfImages.append(pictureFile) 
                    listOfImagesThumbnail.append(pictureFile[:wordLen-4] + '_bmp.bmp')
                    
                    # create an  empty image instance 
                    img = Image.open(root_path + data_path + pictureFile)
                    #Image.open(root_path + data_path + pictureFile).save(root_path + data_path + pictureFile[:wordLen-4] + 'cnv.bmp')
                    
                    print 'Converting file: ' + pictureFile + ' into .bmp file' '\n'
                    
                    img.load()
                    #print len(img.split())
                    if len(img.split()) == 3:
                        r, g, b = img.split()
                        img = Image.merge("RGB", (r, g, b))
                    else:
                        r, g, b, a = img.split()
                        img = Image.merge("RGB", (r, g, b))
                    # resizing is not neccesary
                    img = img.resize((baseWidth,maxHeight), PIL.Image.ANTIALIAS)
                    try:
                        os.stat(root_path + data_path + "bmp\\")
                    except:
                        os.mkdir(root_path + data_path + "bmp\\")
                        
                    img.save(root_path + data_path + "bmp\\" + pictureFile[:wordLen-4] + '_bmp.bmp')
                        
            else:
                print (pictureFile[wordLen-3:wordLen].lower())


convertPicturesInOrder(listOfPaths)

sys.exit(0) # quit Python
        





