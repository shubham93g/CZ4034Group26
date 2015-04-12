from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
scaler = preprocessing.StandardScaler();
from sklearn import svm
import csv

inputPath = "./training data.csv"
inputIdx = 3
labelIdx = 2

testPath = "./test data.csv"
testIdx = 3

outputPath = "./predicted output.csv"

f_csv = open(inputPath, 'r');
f = csv.reader(f_csv);


corpus = []
labels = []

print "getting corpus"

for line in f:
    corpus.append(line[1])
    labels.append(line[2])
    
f_csv.close()

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



ft_csv = open(testPath, 'rU');
ft = csv.reader(ft_csv)

tcorpus = []
print "getting test data"
for line in ft:
    tcorpus.append(line[1])
ft_csv.close()

print "extracting features from test data"
testfeatureVec = cv.transform(tcorpus).toarray()
print "scaling test features"
testfeatureVec = scaler.transform(testfeatureVec)
print "predicting labels for test data"
predicted = clf.predict(testfeatureVec)


fw_csv = open(outputPath, 'wb');
fw = csv.writer(fw_csv)

for l in predicted:
    fw.writerow(l)
fw_csv.close()



