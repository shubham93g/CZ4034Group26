#TOP LEVEL EVALUATE FILE
import sys
sys.path.append("/Users/Prerna/Desktop/Prerna/NTU/Courses-Year4-Sem1/NLP/SemEval15/code");

import evaluate
E = evaluate.Evaluator();
pPath = "./output_2000train_500val.csv";
#gPath = "../rawdata/test/gold/twitter-dev-gold-B_rmnotav.tsv";
gPath = "./val_gold_500.csv";

E.evalPrediction(pPath, gPath);

print "Average Non-other F-measure = ", E.getAvgNonOtherFmeasure();
print "Average F-measure = ", E.getAvgFmeasure();
print "Average Precision = ", E.getAvgPrecision();
print "Average Recall = ", E.getAvgRecall();

print "APAC F-measure = ", E.getFmeasure_apac();
print "EU F-measure = ", E.getFmeasure_eu();
print "AFRICA F-measure = ", E.getFmeasure_af();
print "AMERICA F-measure = ", E.getFmeasure_am();
print "OTHERS F-measure = ", E.getFmeasure_oth();

print "APAC Precision = ", E.getPrecision_apac();
print "EU Precision = ", E.getPrecision_eu();
print "AFRICA Precision = ", E.getPrecision_af();
print "AMERICA Precision = ", E.getPrecision_am();
print "OTHERS Precision = ", E.getPrecision_oth();

print "APAC Recall = ", E.getRecall_apac();
print "EU Recall = ", E.getRecall_eu();
print "AFRICA Recall = ", E.getRecall_af();
print "AMERICA Recall = ", E.getRecall_am();
print "OTHERS Recall = ", E.getRecall_oth();


print "Percentage Correct = ", E.getPercentCorrect();
