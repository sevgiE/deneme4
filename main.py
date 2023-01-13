^#Proje4
import sys
from os import listdir
from img_procedure import *
from classifier_procedure import *

def getDatasetsFromDir(datasets_dir):
 
    X_train, y_train, X_test, y_test = [], [], [], []

 
    try:
        char_dirs = listdir(datasets_dir)
    except:
        return None, None


    if '.DS_Store' in char_dirs:
        char_dirs.remove('.DS_Store')


    for char_dir in char_dirs:
        if len(listdir(datasets_dir+'/'+char_dir)) < 1:
            char_dirs.remove(char_dir)
        else:
            continue

    if len(char_dirs) < 1:
        return None, None

    try:

        emptyBlack = getImg('Data/images/emptyBlack.png')
        X_train.append(getImg('Data/images/emptyWhite.png'))
        X_train.append(getImg('Data/images/emptyBlack.png'))
        y_train.append(ord(' '))
        y_train.append(ord(' '))
    except:
        print('Empty images(for training) not found!')

  
    for char_dir in char_dirs:
        img_dirs = listdir(datasets_dir+'/'+char_dir)

      
        if '.DS_Store' in img_dirs:
            img_dirs.remove('.DS_Store')

        point = int(0.9*len(img_dirs))
        train_imgs, test_imgs = img_dirs[:point], img_dirs[point:]

       
        for img_dir in train_imgs:
            X_train.append(getImg(datasets_dir+'/'+char_dir+'/'+img_dir))
            y_train.append(ord(char_dir))
        for img_dir in test_imgs:
            X_test.append(getImg(datasets_dir+'/'+char_dir+'/'+img_dir))
            y_test.append(ord(char_dir))

    return X_train, y_train, X_test, y_test

def main():
    
    imgDir = getImgDir(sys.argv)
    if imgDir is None:
        print('Image directory not found!')
        return
    img = getImg(imgDir)
    if img is None:
        print('Image not found!')
        return


    clf = getClassifier()

    if clf is None:
        clf = createDecisionTree()
   
        X_train, y_train, X_test, y_test = getDatasetsFromDir('Data/images/train')
        if X_train is None:
            print('Characters datasets not found!')
            return

       
        clf = trainClassifier(clf, X_train, y_train)

        saveClassifier(clf)

  
        print('Train Score:', getScore(clf, X_train, y_train))
        print('Test Score:', getScore(clf, X_test, y_test))

  
    print('Predict:', chr(getPredict(clf, img)))

   
    return


if __name__ == '__main__':
    main()
