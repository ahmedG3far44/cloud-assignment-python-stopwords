
import re 
import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords')


with open("textFile.txt") as file:
    text = file.read()


words_list = re.split(r'[ \n.,;!?\(\)\[\]\{\}\'\"]+', text)
words_list = words_list[:-1] 
print('Number of words Including stop words): ', len(words_list))
print('First 20 words:')
print(words_list[:20])
print('Last 20 words:')
print(words_list[-20:])



stop_words = stopwords.words('english')
print('Number of stop words: ', len(stop_words))
print('List of the current stop words: ')
print(stop_words)

filtered_words_list = [word for word in words_list if word.lower() not in stop_words]
print('Number of words after removing stop words: ', len(filtered_words_list))
print('First 20 words:')
print(filtered_words_list[0:20])
print('Last 20 words:')
print(filtered_words_list[-20:])


words_freqs = {}
for word in filtered_words_list:
    if word in words_freqs.keys():
        words_freqs[word]+=1
    else:
        words_freqs[word]=1
        
print('Number of unique words: ', len(words_freqs))

top_words = [word for word in words_freqs.keys() if words_freqs[word]>500]
print('Number of words occuring more than 500 times: ', len(top_words))
print('List of words occuring more than 500 times:')
print(top_words)
