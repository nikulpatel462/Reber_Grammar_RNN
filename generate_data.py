from reber import *
import numpy as np
import tensorflow as tf
from tensorflow import keras
import random, pickle
from sklearn.utils import shuffle

def permute(s):
    extra_vals = ['b', 't', 's', 'x', 'p', 'v', 'e']
    
    #permute string until we obtain a non reber sequence
    #(note: this process will eventually terminate)
    while check_reber(s):
        k = random.choice(extra_vals)
        i = random.randint(0,len(s)-1)
        l = list(s) 
        l[i] = 'k'
        s = ''.join(l)

    return s

def preprocess(x_batch,y_batch):
    tokenizer = keras.preprocessing.text.Tokenizer(char_level=True)
    tokenizer.fit_on_texts(x_batch)
    num_letters = len(tokenizer.word_index)

    #save tokenizer
    with open('tokenizer.pickle',mode='wb') as f:
        pickle.dump(tokenizer,f,protocol=pickle.HIGHEST_PROTOCOL)

    x_batch, y_batch = shuffle(x_batch,y_batch)
    x_batch = np.array(tokenizer.texts_to_sequences(x_batch)) 
    x_batch = [tf.one_hot(x,depth=num_letters) for x in x_batch]

    return x_batch, y_batch

def create_data(true_sample_size = 10000):
    true_sample_size = 10
    true_samples = set()
    
    while len(true_samples) < true_sample_size:
        true_samples.add(generate_reber())
    
    #we modify these samples using the permute function defined above until
    #we have true_sample_size false samples
    
    true_samples = list(true_samples)
    false_samples = [permute(s) for s in true_samples]
    
    x = true_samples + false_samples
    y = [1 for _ in true_samples] + [0 for _ in false_samples]
    
    xb, yb = preprocess(x,y)

    return xb, yb

if __name__ == '__main__':
    xb, yb = create_data(10)
    print(xb, yb)
