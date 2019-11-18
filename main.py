# Case #4

# The program ...
#

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
    print('Choose language/ Выберите язык./n1) Englishs/ Английский язык;\n2) '
          'Russian/ Русский язык.')
    language = input('Input number/ Введите цифру: ')

text = input('Введите текст: ')

count_rus = 0
count_eng = 0
text_language = ''
for i in text:
    if i.lower() in 'яюэьыъщшчцхфутсрпонмлкйизжёедгвба':
        count_rus += 1
    elif i.lower() in 'abcdefghijklmnopqrstuvwxyz':
        count_eng += 1
if count_rus > count_eng:
    text_language = 'русский'
else:
    text_language = 'english'

letter = ''

blob = TextBlob(text)
count_sentens = len(blob.sentences)
print('Предложений:', count_sentens)


if text_language == 'русский':
    letter = 'аоиеёэыуюя'
elif text_language == 'english':
    letter = 'aoieuy'


count_syllables = 0
for i in range(len(text)):
    if text[i] in letter:
        count_syllables += 1
print('Слогов:', count_syllables)

text = text.split()
count_words = len(text)
print('Слов:', count_words)


ASL = count_sentens / count_words
ASL = ("{:.3f}".format(ASL))
ASW = count_words / count_syllables
ASW = ("{:.3f}".format(ASW))

if text_language == 'русский':
    FRE = 206.835 - (1.3 * float(ASL)) - (60.1 * float(ASW))
    letter = 'аоиеёэыуюя'
elif text_language == 'english':
    FRE = 206.835 - (1.015 * float(ASL)) - (84.6 * float(ASW))
    letter = 'aoieuy'

print('Средняя длина предложения в словах:', ASL)
print('Средняя длина слова в слогах:', ASW)
print('Индекс удобочитаемости Флеша:', FRE)

if FRE > 80:
    print('Текст очень легко читается (для младших школьников).')
elif 50 <= FRE <= 80:
    print('Простой текст (для школьников).')
elif 25 < FRE < 50:
    print('Текст немного трудно читать (для студентов).')
elif FRE <= 25:
    print('Текст трудно читается (для выпускников ВУЗов).')


polarity = blob.polarity

if 0.3 < polarity <= 1:
    polarity = 'позитивный'
elif -1 <= polarity < -0.3:
    polarity = 'негативный'
else:
    polarity = 'нейтральный'

subjectivity = blob.subjectivity * 100
objectivity = (100 - subjectivity)

print('Тональность текста:', polarity)
print('Cубъективность: ', '{:.1f}'.format(subjectivity), '%', sep='')
print('Oбъективность: ', '{:.1f}'.format(objectivity), '%', sep='')