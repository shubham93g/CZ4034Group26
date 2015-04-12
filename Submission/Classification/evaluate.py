# Code for evaluation of prediction using gold and predicted files.


import string
import csv

class Evaluator:
    def __init__(self):
        #print "constructor called";
        self.TP_apac = 0.0;
        self.TP_eu = 0.0;
        self.TP_af = 0.0;
        self.TP_am = 0.0;
        self.TP_oth = 0.0;
        self.FP_apac = 0.0;
        self.FP_eu = 0.0;
        self.FP_af = 0.0;
        self.FP_am = 0.0;
        self.FP_oth = 0.0;
        self.FN_apac = 0.0;
        self.FN_eu = 0.0;
        self.FN_af = 0.0;
        self.FN_am = 0.0;
        self.FN_oth = 0.0;
	self.lineCount = 0.0;
    def getPrecision_apac(self):
        return (self.TP_apac/(self.TP_apac+self.FP_apac));
        
    def getPrecision_eu(self):
        return (self.TP_eu/(self.TP_eu+self.FP_eu));
        
    def getPrecision_af(self):
        return (self.TP_af/(self.TP_af+self.FP_af));
		
    def getPrecision_am(self):
        return (self.TP_am/(self.TP_am+self.FP_am));
        
    def getPrecision_oth(self):
        return (self.TP_oth/(self.TP_oth+self.FP_oth));

    def getRecall_apac(self):
        return (self.TP_apac/(self.TP_apac+self.FN_apac));
        
    def getRecall_eu(self):
        return (self.TP_eu/(self.TP_eu+self.FN_eu));
        
    def getRecall_af(self):
        return (self.TP_af/(self.TP_af+self.FN_af));
		    
    def getRecall_am(self):
        return (self.TP_am/(self.TP_am+self.FN_am));
        
    def getRecall_oth(self):
        return (self.TP_oth/(self.TP_oth+self.FN_oth));

    def getAvgPrecision(self):
        return ((self.getPrecision_apac()+self.getPrecision_eu()+ self.getPrecision_af()+  self.getPrecision_am() + self.getPrecision_oth())/5.0);

    def getAvgRecall(self):
        return ((self.getRecall_apac()+self.getRecall_eu()+ self.getRecall_af()+ self.getRecall_am()+self.getRecall_oth())/5.0);

    def getFmeasure_apac(self):
        return ((2*self.getPrecision_apac()*self.getRecall_apac())/(self.getPrecision_apac()+self.getRecall_apac()));

    def getFmeasure_eu(self):
        return ((2*self.getPrecision_eu()*self.getRecall_eu())/(self.getPrecision_eu()+self.getRecall_eu()));

    def getFmeasure_af(self):
        return ((2*self.getPrecision_af()*self.getRecall_af())/(self.getPrecision_af()+self.getRecall_af()));
		
    def getFmeasure_am(self):
        return ((2*self.getPrecision_am()*self.getRecall_am())/(self.getPrecision_am()+self.getRecall_am()));

    def getFmeasure_oth(self):
        return ((2*self.getPrecision_oth()*self.getRecall_oth())/(self.getPrecision_oth()+self.getRecall_oth()));
		

    def getAvgFmeasure(self):
        return ((self.getFmeasure_apac()+self.getFmeasure_eu()+ self.getFmeasure_af()+ self.getFmeasure_am()+self.getFmeasure_oth())/5.0);

    def getAvgNonOtherFmeasure(self):
        return ((self.getFmeasure_apac()+self.getFmeasure_eu()+ self.getFmeasure_af()+ self.getFmeasure_am())/4.0);

    def getPercentCorrect(self):
        return ((self.TP_apac+self.TP_eu+self.TP_af+self.TP_am+self.TP_oth)/self.lineCount)*100;
    
    def evalPrediction(self, predictedPath, goldPath):
            pred_csv = open(predictedPath)
            gold_csv = open(goldPath)
            fp = csv.reader(pred_csv)
            fg = csv.reader(gold_csv)
            

            for line_fp in fp:
                    self.lineCount = self.lineCount + 1
                    line_fg = fg.next()
                    labelP = line_fp[0];
                    labelG = line_fg[1];
                    if labelP == "APAC" and labelG == labelP:
                        self.TP_apac=self.TP_apac+1;
                    if labelP == "EU" and labelG == labelP:
                        self.TP_eu=self.TP_eu+1;
                    if labelP == "AMERICA" and labelG == labelP:
                        self.TP_am=self.TP_am+1;
                    if labelP == "AFRICA" and labelG == labelP:
                        self.TP_af=self.TP_af+1;
                    if labelP == "OTHERS" and labelG == labelP:
                        self.TP_oth=self.TP_oth+1;
                        
                    if labelP == "APAC" and labelG != labelP:
                        self.FP_apac=self.FP_apac+1;
                    if labelP == "EU" and labelG != labelP:
                        self.FP_eu=self.FP_eu+1;
                    if labelP == "AMERICA" and labelG != labelP:
                        self.FP_am=self.FP_am+1;
                    if labelP == "AFRICA" and labelG != labelP:
                        self.FP_af=self.FP_af+1;
                    if labelP == "OTHERS" and labelG != labelP:
                        self.FP_oth=self.FP_oth+1;

                    

                    if labelG == "APAC" and labelG != labelP:
                        self.FN_apac=self.FN_apac+1;
                    if labelG == "EU" and labelG != labelP:
                        self.FN_eu=self.FN_eu+1;
                    if labelG == "AMERICA" and labelG != labelP:
                        self.FN_am=self.FN_am+1;
                    if labelG == "AFRICA" and labelG != labelP:
                        self.FN_af=self.FN_af+1;
                    if labelG == "OTHERS" and labelG != labelP:
                        self.FN_oth=self.FN_oth+1;
                        
            #print "Number of lines evaluated = ", self.lineCount;

                        
        
        
