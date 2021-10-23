from flask import Flask, render_template, request 

import pickle 
import numpy as np 

from pre_processer import pre_processer

app = Flask(__name__)




@app.route('/')
def main():
    # return "This is my name"
    return render_template('index.html')




model = pickle.load(open('model.pkl','rb'))

tfidf_vectorizer = pickle.load(open('transformer.pkl','rb'))
# incomming = pre_processer("dont like it that much not so good")

labels = ['Negative', 'Neutral', 'Positive']

@app.route('/predict',methods=['POST'])
def get_sentiment():
    
    review = request.form['review']

    x = pre_processer(review)
    
    x = tfidf_vectorizer.transform([x])
    
    y = int(model.predict(x.reshape(1,-1)))
    
    prediction = labels[y]
    
    return render_template('after.html',data=prediction)

# result = get_sentiment("This is nice ")

# print(f"This  is a {result} sentiment")


if __name__=="__main__":
    app.debug = True
    app.run()
