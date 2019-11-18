# Case #4

# The program calculates the Flesch index and displays a textual interpretation of the calculated index.
# The program determines the tonality of the text and how much the statements in the text are objective
# or subjective (in percent).


# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).


from textblob import TextBlob


# Choosing the language.
print('Choose language/ Выберите язык.\n1) English/ Английский язык;\n2) '
      'Russian/ Русский язык.')
language = input('Input number/ Введите цифру: ')

while True:
    if language == '1':
        import eng_local as lc

        break
    elif language == '2':
        import rus_local as lc

        break
    print('Choose language/ Выберите язык./n1) English/ Английский язык;\n2) '
          'Russian/ Русский язык.')
    language = input('Input number/ Введите цифру: ')


text = input(lc.TXT_INPUT_TEXT)

# Determining the language of the text.
count_rus = 0
count_eng = 0
text_language = ''
for i in text:
    if i.lower() in 'яюэьыъщшчцхфутсрпонмлкйизжёедгвба':
        count_rus += 1
    elif i.lower() in 'abcdefghijklmnopqrstuvwxyz':
        count_eng += 1
if count_rus > count_eng:
    text_language = lc.TXT_RUSSIAN_LANGUAGE
else:
    text_language = lc.TXT_ENGLISN_LANGUAGE


# Counter of sentences, syllables and words.
blob = TextBlob(text)
count_sentens = len(blob.sentences)
print(lc.TXT_SENTENCES, count_sentens)

letter = ''
if text_language == 'русский':
    letter = 'аоиеёэыуюя'
elif text_language == 'english':
    letter = 'aoieuy'

count_syllables = 0
for i in range(len(text)):
    if text[i] in letter:
        count_syllables += 1
print(lc.TXT_SYLLABLES, count_syllables)

text = text.split()
count_words = len(text)
print(lc.TXT_WORDS, count_words)


ASL = count_sentens / count_words
ASL = ("{:.3f}".format(ASL))
ASW = count_words / count_syllables
ASW = ("{:.3f}".format(ASW))

# Flash index calculation.
if text_language == lc.TXT_RUSSIAN_LANGUAGE:
    FRE = 206.835 - (1.3 * float(ASL)) - (60.1 * float(ASW))
    letter = 'аоиеёэыуюя'
elif text_language == lc.TXT_ENGLISN_LANGUAGE:
    FRE = 206.835 - (1.015 * float(ASL)) - (84.6 * float(ASW))
    letter = 'aoieuy'

print(lc.TXT_AVERAGE_LENGTH_OF_SENTENCE, ASL)
print(lc.TXT_AVERAGE_LENGTH_OF_WORD, ASW)
print(lc.TXT_FLESCH_INDEX, FRE)

if FRE > 80:
    print(lc.TXT_VERY_EASY_FOR_READING)
elif 50 <= FRE <= 80:
    print(lc.TXT_EASY_FOR_READING)
elif 25 < FRE < 50:
    print(lc.TXT_A_BIT_HARD_FOR_READING)
elif FRE <= 25:
    print(lc.TXT_HARD_FOR_READING)

# Translating of text from Russian into English.
if text_language == lc.TXT_RUSSIAN_LANGUAGE:
    blob = blob.translate(to='en')

# Definition of tonality of the text.
polarity = blob.polarity

if 0.3 < polarity <= 1:
    polarity = lc.TXT_POSITIVE
elif -1 <= polarity < -0.3:
    polarity = lc.TXT_NEGATIVE
else:
    polarity = lc.TXT_NEUTRAL

# Determination of the objectivity / subjectivity of statements in the text.
subjectivity = blob.subjectivity * 100
objectivity = (100 - subjectivity)

print(lc.TXT_POLARITY, polarity)
print(lc.TXT_SUBJECTIVITY, '{:.1f}'.format(subjectivity), '%', sep='')
print(lc.TXT_OBJECTIVITY, '{:.1f}'.format(objectivity), '%', sep='')