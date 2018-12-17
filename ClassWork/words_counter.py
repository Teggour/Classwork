import operator

txt = (
    "Намереваясь принудить мексиканское правительство к миру, Скотт высадился около Веракруса, захватил этот город "
    "и начал наступление на столицу Мексики, следуя по пути похода Эрнана Кортеса (1519). Разбив мексиканскую армию "
    "при Серро-Гордо и Чурубуско, Скотт подступил к Мехико и в ходе нескольких сражений овладел городом. Падение "
    "Мехико и несколько последующих сражений вынудили мексиканское правительство пойти на переговоры и заключить "
    "договор Гуадалупе-Идальго."
)


def split_reg(x):
    clear_txt = []
    symbs = [',', '.', '-', '?', '!', '(', ')']

    for word in x.split():
        clear_word = ""

        for latter in word:

            if latter is symbs:
                clear_word += ""

            if latter.isalpha():
                clear_word += latter.lower()

        clear_txt.append(clear_word)

    return clear_txt


def find_sort(lst):
    cnt = {}

    for word in lst:
        cnt[word] = cnt.get(word, 0) + 1

    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

    return cnt


arr = split_reg(txt)

count = find_sort(arr)

print(count[0:1])
