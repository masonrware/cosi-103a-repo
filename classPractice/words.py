import urllib.request

link = "http://norvig.com/google-books-common-words.txt"
f = urllib.request.urlopen(link)

wordfreqlist = f.read().decode('utf-8').split('\n')  # read the word list as a string

words = [w.split('\t')[0] for w in wordfreqlist]  # take 1st word on each line

print('words is a list of ', len(words), 'words')
words5 = [w for w in words if len(w) == 5]
print('words5 is a list of', len(words5), '5 letter words')
