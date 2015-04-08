from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
scaler = preprocessing.StandardScaler();
from sklearn import svm

inputPath = "train.txt"
inputIdx = 0
labelIdx = 1

testPath = "val_100.txt"
testIdx = 0

outputPath = "output.txt"

f = open(inputPath, 'r');

corpus = []
labels = []

print "getting corpus"

for line in f:
    lst = line.split()
    capList = lst[:len(lst)-2]
    caption = " ".join(capList)
    corpus.append(caption)
    labels.append(lst[len(lst)-1])
f.close

##print corpus
cv = CountVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0)
print "extracting features from corpus"
sparsefeatureVec = cv.fit_transform(corpus).toarray()
print sparsefeatureVec

##for w in cv.get_feature_names():
##    print w


print "declaring svm"
clf = svm.LinearSVC(C=0.01, class_weight='auto', penalty='l2', dual=0); # linearsvc2
print "scaling features"
sparsefeatureVec = scaler.fit_transform(sparsefeatureVec, labels);
print "training svm"
clf.fit(sparsefeatureVec, labels);

from sklearn.externals import joblib
print "Saving SVM"
fileToSave = "SVMUniBiTri.joblib.pkl";
_ = joblib.dump(clf, fileToSave, compress=9)
print "Classifier saved!";


ft = open(testPath, 'r');
tcorpus = []
print "getting test data"
for line in ft:
    lst = line.split()
    capList = lst[0:]
    caption = " ".join(capList)
    tcorpus.append(caption)
ft.close

print "extracting features from test data"
testfeatureVec = cv.transform(tcorpus).toarray()
print "scaling test features"
testfeatureVec = scaler.transform(testfeatureVec)
print "predicting labels for test data"
predicted = clf.predict(testfeatureVec)


fw = open(outputPath, 'w');
for l in predicted:
    fw.write(l)
    fw.write('\n')
fw.close()



