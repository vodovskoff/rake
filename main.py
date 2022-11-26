from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')
r = Rake()
f = open('text1.txt', 'r', encoding='utf8')
text = f.read()
f.close()
r.extract_keywords_from_text(text)

result = r.get_ranked_phrases()

def printWithoutScores():
    result = r.get_ranked_phrases()[:5]
    while result:
        print(result.pop(0) ,'. ')

printWithoutScores()