import gensim
from get_data import get_data
from gensim.models import Word2Vec
import time
localtime = time.asctime( time.localtime(time.time()))
text = get_data()
model = gensim.models.KeyedVectors.load_word2vec_format('modelfile/GoogleNews-vectors-negative300.bin.gz', binary=True)
model.build_vocab(sentences=text, update=True)
model.train(sentences=text, total_examples=model.corpus_count, epochs=model.iter)
model.save('./modelfile/Model%s'%localtime)
model.wv.save_word2vec_format('./modelfile/model%s.txt'%localtime, binary=False)