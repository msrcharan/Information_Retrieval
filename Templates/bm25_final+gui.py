

import os
from nltk.tokenize import word_tokenize

# List the files in the directory
# file_list = os.listdir('/content/drive/MyDrive/tweet_files')
data_dir = 'D:\\Downloads\\IR_Twitter_Project\\tweet_files_\\tweet_file\\'
DATA_SET_DIR = data_dir
print('\nGetting List of text files from' + DATA_SET_DIR)
files = os.listdir(DATA_SET_DIR)
# print((files[1000]))
print('\nFile list retrieved from ' + DATA_SET_DIR)

corpus = []
for f in files:
  strm = open(DATA_SET_DIR + f,'r')
  content = strm.read()
  words = content.split(" ")
  corpus.append(' '.join(words))
  strm.close()

print(corpus[11])

from rank_bm25 import BM25Okapi #imp copy from here
def bm25_precision10(query, corpus):
    tokenized_corpus = [doc.split(" ") for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = query.split(" ")
    doc_scores = bm25.get_scores(tokenized_query)
    print("Top relevant docs are :")
    print(bm25.get_top_n(tokenized_query, corpus, n=5))
    print("Top 10 relevant docs in the query :")
    docscores = list(doc_scores)
    topten = sorted(range(len(docscores)), key=lambda i: docscores[i], reverse=True)[:10]
    print(topten)

bm25_precision10("jeep compass is great to drive",corpus)

tokenized_corpus = [doc.split(" ") for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

import PySimpleGUI as sg

layout = [
    [sg.VPush()],
    [sg.Text("Search: "), sg.Input(key='INPUT')], 
    [sg.Ok()],
    [sg.Text("", size=(50, 50), key='OUTPUT'),  ],
    [sg.VPush()],
]

window = sg.Window("Tweets Database", layout, size=(1400, 600), element_justification='c',background_color='white')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Ok':
        name = values['INPUT']
        tokenized_query = name.split(" ")
        tokenized_corpus = [doc.split(" ") for doc in corpus]
        doc_scores = bm25.get_scores(tokenized_query)
        window['OUTPUT'].update(value=bm25.get_top_n(tokenized_query, corpus, n=5))

window.close()