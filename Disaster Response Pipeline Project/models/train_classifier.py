import sys
# import libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize , sent_tokenize
from sklearn.pipeline import Pipeline , FeatureUnion
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split,  GridSearchCV 
from sklearn.metrics import classification_report ,confusion_matrix , accuracy_score
from sklearn.base import BaseEstimator, TransformerMixin
import pickle


def load_data(database_filepath):
    # load data from database
    engine = create_engine('sqlite:///disaster.db')
    df = pd.read_sql_table("disaster",con=engine)
    ## create training data
    X = df['message']
    ## create label data
    Y = df.drop(['id','message',"original","genre"],axis=1)
    ## export features names
    category_names = list(Y.columns.values)
    # return data and labels and feature names
    return X , Y , category_names

def tokenize(text):
    ## create lemmatizer
    lemmatizer = WordNetLemmatizer()
    ## make all text in lower letters
    lower_text = text.lower()
    ## remove all special characters, punctuation
    normalized_text = re.sub(r"[^a-zA-Z0-9]"," ",lower_text)
    ## Return a tokenized copy of text
    text_token = word_tokenize(normalized_text)
    ## Remove all stop words
    remove_stop_words = [word for word in text_token if word not in stopwords.words('english')]
    ## Apply lemmatization on the text
    lemmatized = [lemmatizer.lemmatize(word) for word in remove_stop_words]
    ## return the list of words after processing
    return lemmatized


def build_model():
    """ grid search max feature parameter in our data transformation through AdaBoost classifier! """
    pipeline_adaboost = Pipeline([("vect",CountVectorizer(tokenizer=tokenize)),
          ("tfidf",TfidfTransformer()),
          ('clf', MultiOutputClassifier(AdaBoostClassifier()))])
    parameters = {'vect__max_features' : [200,500,1000]
    }

    CV_adaboost = GridSearchCV(pipeline_adaboost,param_grid=parameters)
    
    return CV_adaboost

    


def evaluate_model(model, X_test, Y_test, category_names):
    """ this functon returns accuracy , precision , f1-score and total accuracy"""
    total_scores = []
    i = 0
    y_pred = model.predict(X_test)
    for feat in Y_test:
        print("Feature {}: {}".format(i+1,feat))
        print(classification_report(Y_test[feat],y_pred[:,i]))
        accuracy = accuracy_score(Y_test.iloc[:,i],y_pred[:,i])
        total_scores.append(accuracy)
        i+=1
    print("Total Accuracy : {:.4f}".format(np.mean(total_scores))) 
    return (np.mean(total_scores))


def save_model(model, model_filepath):
    """ Export the model as a pickle file """
    filename = 'disaster_model.pkl'
    pickle.dump(model, open(filename, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()