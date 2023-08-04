# TOUR-INTELLIGENCE-SYSTEM

ABSTRACT The use of recommender systems is widespread. Our primary attention is given to the use of tourism. Since many years ago, conferences have been extensively searched. We present a thorough and up-to-date overview of this topic, taking into account the various types of methods, the diversity of recommendation algorithms, the features these systems have to offer, and their usage of artificial intelligence approaches. The most potential topics of research in this field for the coming years are also suggested by our poll, along with some advice for tourist recommenders. Since quick access to reliable information is the foundation of our system, information overload has become a typical occurrence and a significant problem for those looking for relevant information in this age of the Internet. Additionally, numerous studies have been done on how to improve the effectiveness of the material on tourism websites. Therefore, an intelligent smart tourism management system makes an effort to close the gap by taking note of what a tourist considers pertinent while connecting to tourism products on tourism websites. This study primarily focuses on content because it is seen to be the key component of an efficient and clever website.

METHODOLOGY A growing amount of data is generated each day as a result of the development of information technology and the adoption of wireless networks. Therefore, it has become crucial for technology developers in the present day to figure out ways to enable people to swiftly get the information as they need. As a result, we describe a trip intelligent recommendation system that uses user behavior trail and location data to offer a rich and efficient tour service. This Adventure tour Recommendation System made up by using two major parts i.e Review System and Recommendation System . ∙ Recommendation System Essentially, the model is already pre-loaded with datasets of Indian regions where adventure tourism is plausible.   

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/e9188970-84ac-45dd-aa53-05ef43ff4ac0)

Second, Geopy python libraries enable us to supply the longitude and latitude of the location present in the dataset. K-Means, which is imported from Sklearn Cluster, is the algorithm used by this recommendation system.

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/5b20319c-081a-460e-b232-b2adc8ffa134)

In order to build clusters, including centroids, Kmeans functions were employed along with the longitude and latitude data from Geopy. The user then provides the model with his input in accordance with his preferences, and the model then proposes locations.

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/56065e0f-84a0-4f28-bca2-a9b1bd10a864)

 Review System Here, we have defined some of the scores for review which is givens by tourists.

 ![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/3c16db65-1109-4c44-8c0c-17be79487703)

 Importing the JSON which contains the reviews of the different tourist locations . With the help of Sklearn modules Imported train_test_split where we passed its arguments like test_size of 33% along with Random State.

Spiliting the data into text and sentiment.

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/03c950bb-7bb9-445a-81d2-3a07eb73ca3e)

Now, Using Sklearn Feature Extraction text importing the CountVectorizer where we will be training the data which is in text.

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/ecd7357c-90ad-43e4-9414-2cd388c936df)

Here we are doing the classification Different model is which used here: (A) RBF (Radial Basis Function) SVM (B) Decision Tree (C) Naive Bayes (D) Logistic Regression

Evaluation of Accuracy is being done of different models and giving out the output.

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/4f4c8654-4bb2-4878-b37c-b4c99f34ca03)

Showing the review of based on the scores.

![image](https://github.com/prachipandey16/TOUR-INTELLIGENCE-SYSTEM/assets/115707069/67921ebc-65cc-46fc-9dab-178ff66b2a88)

RESULTS The model is basically already pre-loaded with datasets of Indian locations where adventure tourism is conceivable. As the user inputs the locations that suit his interests, the following enables him to access the other locations of his choice.







