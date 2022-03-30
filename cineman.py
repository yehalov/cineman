import random
import re
import os

correct = 0
qcount = 0
print('Input \'0\' to stop test, \'1\' to see the name of the movie\n')

for i in os.walk('subs'):
    movie_list = (i[2])
    
while True: #цикл повторения вопросов
    clean_blocks = []
    movie = movie_list[random.randint(0,len(movie_list)-1)]
    with open (u'subs\\'+movie, 'r', encoding='utf-8') as sub: #открываем файл
        blocks = sub.read().split("\n\n") #разбиваем на блоки фраз по пустой строке

    for trash in blocks: #очищаем блоки от мусора, перебираем список blocks
        blocklist = trash.split("\n") #создаем список из строк по разделителю "перенос строки"
        del blocklist[0:2] #удаляем два первых элемента - номер и время
        s = ' ' #из списка фраз из-за лишних переносов объединяем и ставим пробел
        clean_phrase = s.join(blocklist) #превращаем список из одного элемента в строку
        clean_blocks.append(clean_phrase) #добавляем эту строку в общий список фраз clean_blocks

    #получили список из чистых фраз clean_blocks

    q = random.randint(0,len(clean_blocks)-1) #получаем длину списка и помещаем в q случайное число
    phrase = clean_blocks[q] #берем случайную фразу из списка
    phrase_list = phrase.split() #разбиваем фразу на слова, для получения количества слов

    if len(phrase_list) > 3: #отметаем слишком короткие фразы
        phrase_blank = phrase_list.copy() #копируем список слов для удаления последнего слова
        rand = random.randint(0,len(phrase_blank)-1)
        phrase_blank[rand] = '...' #заменяем случайное слово на "..."
        phrase_ask = s.join(phrase_blank) #объединяем список слов с "..." в строку
        phrase_answer = input(phrase_ask+'\n') #выводим фразу-вопрос и просим ввести ответ
    else:
        continue #если в фразе меньше трех слов начинаем цикл заново
    phrase_compare = re.sub(r'[^\w\s]','', phrase_list[rand]) #убираем знаки препинания из случайного слова для корректного сравнения
    if phrase_answer == '0':
        break
    if phrase_answer == '1':
        print(movie)
        phrase_answer = input(phrase_ask+'\n')
    if phrase_answer.lower().strip() == phrase_compare.lower().strip(): #условие: ответ без пробелов и маленькими буквами равен последнему слову без пунктуации
        print(f"\nCorrect! {phrase} ({movie})\n") #если да, печатаем Correct! и всю фразу
        correct =+ 1       
    else:
        print(f"\nWrong. {phrase} ({movie})\n") #если нет, печатаем Wrong. и всю фразу
    qcount =+ 1
        
print('You have '+str(int(correct*100/qcount))+'%'+' of correct answers')
print(len(clean_blocks))
