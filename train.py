from get_data import get_data
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from cosine_distance import cosine_similarity;
import time
 
localtime = time.asctime( time.localtime(time.time()))
text = get_data()
model = Word2Vec(text, size=100, window=5, min_count=1, workers=4)
model.save('./modelfile/Model%s'%localtime)
model.wv.save_word2vec_format('./modelfile/model%s.txt'%localtime, binary=False)