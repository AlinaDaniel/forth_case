# Case #4

# The program ...
#

# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).


from textblob import TextBlob


# Choosing the language.
print('Choose language/ Выберите язык.\n1) Englishs/ Английский язык;\n2) '
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

text = TextBlob(text)
polarity = text.polarity

if 0.3 < polarity <= 1:
    polarity = 'позитивный'
elif -1 <= polarity < -0.3:
    polarity = 'негативный'
else:
    polarity = 'нейтральный'

subjectivity = text.subjectivity * 100
objectivity = (100 - subjectivity)

print('Тональность текста:', polarity)
print('Cубъективность: ', '{:.1f}'.format(subjectivity), '%', sep='')
print('Oбъективность: ', '{:.1f}'.format(objectivity), '%', sep='')