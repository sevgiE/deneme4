# Proje4
from sklearn.externals import joblib
from sklearn import tree

def createDecisionTree():
  
    return tree.DecisionTreeClassifier()

def getClassifier():
    try:
        clf = joblib.load('Data/classifier/classifier.pkl')
    except:
        return None
    return clf

def trainClassifier(clf, X, y):
  
    return clf.fit(X, y)

def getScore(clf, X, y):
    return clf.score(X, y)

def getPredict(clf, img):
 
    return clf.predict(img)

def saveClassifier(clf):

    joblib.dump(clf, 'Data/classifier/classifier.pkl')
