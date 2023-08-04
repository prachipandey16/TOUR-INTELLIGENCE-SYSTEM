#Sentiment is Enum Class
class Sentiment:
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"


class Review:
    def __init__(self,text,score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()

    def get_sentiment(self):
        if(self.score>3):
            #return "POSITIVE" without class Sentiment
            return Sentiment.POSITIVE

        elif(self.score==3):
            #return "NEUTRAL" without class Sentiment
            return Sentiment.NEUTRAL

        else:
            #return "NEGATIVE" without class Sentiment
            return Sentiment.NEGATIVE
    

import json 

#file_name = 'C:\\Users\\Public\\Downloads\\Books_small.json'
file_name = 'C:\\Users\\Public\\Downloads\\Books_small_10000.json'


reviews=[]
with open(file_name) as f:
    for line in f:
        #print(line)
        #print(line['reviewText']) will give error because it's just a raw text
        review = json.loads(line)
        #print(review['reviewText'])will print the review
        #print(review['overall'])will print the numeric rating 4.0 etc.
        #reviews.append((review['reviewText'],review['overall'])) without class
        reviews.append(Review(review['reviewText'],review['overall']))

        
#print(reviews[5]) will print the review no 5 with Text and Overall rating without class
#print(reviews[5][0])will print the Text
#print(reviews[5][1]) will print the Overall rating

print(reviews[100].sentiment)
print(reviews[100].score)


#Prep Data
from sklearn.model_selection import train_test_split

#test_size=0.33 means 33% reviews for test and rest for training
#random_state so that we get the same thing every time
training,test =train_test_split(reviews,test_size=0.33,random_state=42)
print(len(training))#length of the training data
print(len(test))#length of our testing data

print(training[0].sentiment)#first training review and it is still an object

#Spiliting the data into text and sentiment
train_x = [x.text for x in training]
train_y = [x.sentiment for x in training]

test_x = [x.text for x in test]
test_y = [x.sentiment for x in test]

print(train_x[0])
print(train_y[0])

print(test_x[0])
print(test_y[0])



#Bag of words for in sklearn(CountVectorizer)
#Extracting features from text files
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
#here we are training our data(text)
train_x_vectors = vectorizer.fit_transform(train_x)

test_x_vectors = vectorizer.transform(test_x)

print(train_x[0])
print(train_x_vectors[0])#Matrix represents the above text

print(train_x_vectors[0].toarray())




#CLASSIFICATION
##Linear SVM
from sklearn import svm

clf_svm = svm.SVC(kernel='rbf', gamma = 0.85, C=1000.0)
clf_svm.fit(train_x_vectors,train_y)

print(test_x[0])
print(train_x_vectors[0])

print(clf_svm.predict(test_x_vectors[0]))


##Decision Tree
from sklearn.tree import DecisionTreeClassifier

clf_dec = DecisionTreeClassifier()
clf_dec.fit(train_x_vectors,train_y)

print(clf_dec.predict(test_x_vectors[0]))


##Naive Bayes
from sklearn.naive_bayes import GaussianNB

clf_gnb = GaussianNB()
clf_gnb.fit(train_x_vectors.toarray(),train_y)

print(clf_gnb.predict(test_x_vectors[0].toarray()))


##Logistic Regression
from sklearn.linear_model import LogisticRegression

clf_log = LogisticRegression()
clf_log.fit(train_x_vectors,train_y)

print(clf_log.predict(test_x_vectors[0]))





#EVALUATION
from sklearn import svm

#Mean Acuuracy all of out test Labels
#Accuract is one thing like how many labels actually predict correctly
print(clf_svm.score(test_x_vectors,test_y))
print(clf_dec.score(test_x_vectors,test_y))
print(clf_gnb.score(test_x_vectors.toarray(),test_y))
print(clf_log.score(test_x_vectors,test_y))

#F1 Scores
from sklearn.metrics import f1_score

#print f1_score for Sentiment.POSITIVE,Sentiment.NEUTRAL,Sentiment.NEGATIVE and trash for NEUTRAL,NEGATIVE
print(f1_score(test_y,clf_svm.predict(test_x_vectors),average=None,labels=[Sentiment.POSITIVE,Sentiment.NEUTRAL,Sentiment.NEGATIVE]))
print(f1_score(test_y,clf_dec.predict(test_x_vectors),average=None,labels=[Sentiment.POSITIVE,Sentiment.NEUTRAL,Sentiment.NEGATIVE]))
print(f1_score(test_y,clf_gnb.predict(test_x_vectors.toarray()),average=None,labels=[Sentiment.POSITIVE,Sentiment.NEUTRAL,Sentiment.NEGATIVE]))
print(f1_score(test_y,clf_log.predict(test_x_vectors),average=None,labels=[Sentiment.POSITIVE,Sentiment.NEUTRAL,Sentiment.NEGATIVE]))


#Our Result is working good for POSITIVE
#Improving our Model for NEGATIVE and NEUTRAL
#Data Issue rather tha Model Issue

print(train_y[0:10])#will show that POSITIVE is highly biased
print(train_y.count(Sentiment.POSITIVE))#will print the count of POSITIVE i.e will show data is Highly Biased
print(train_y.count(Sentiment.NEGATIVE))

#Solution is loading more data
