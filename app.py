from flask import Flask, render_template, request
from flask import Blueprint
import nltk
import os
from nltk.tokenize import word_tokenize , sent_tokenize
# import numpy as np
# import pandas as pd
# import os
from tqdm import tqdm
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_non_alphanum ,strip_short
from gensim.parsing.preprocessing import preprocess_documents
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
##############################################


# Semantic PART
data = Blueprint('data',__name__ )

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/TakeTour')
def take_tour():  # put application's code here
    return render_template("take_tour.html")


@app.route('/analysis', methods=['POST'])
def analysis():  # put application's code here
    if request.method == 'POST':
        RawText = request.form['RawText']
        # NLP Stuff
        return render_template("index.html")


def clean_data():

    path = 'static/aquaint/RawText/'
    list_txt = []
    tokenized_sent = []
    for txt in os.listdir(path):
        f = open(os.path.join(path, txt), "r")
        _txt = f.read()
        _txt = strip_multiple_whitespaces(_txt)
        _txt = remove_stopwords(_txt)
        _txt = sent_tokenize(_txt)
        for i in _txt:
            t1 = strip_non_alphanum(i)
            t1 = strip_short(t1, minsize=3)
            t2 = remove_stopwords(t1)

            list_txt.append(t2)
            print(list_txt)
            for s in list_txt:
                tokenized_sent.append(word_tokenize(s.lower()))
            len(tokenized_sent)
            tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_sent)]
            return tagged_data


if __name__ == '__main__':
    app.run(debug=True)
