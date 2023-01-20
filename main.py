def get_words() -> list[str]:
    try:
        with open('./palavras.txt') as f:
            words = f.read().splitlines()
        return words
    except:
        print('couldn\'t find file')
        return []

def match_letter(l: str)-> str:
    match l:
        case ('à' | 'á' | 'ã' | 'â' | 'a') : return 'a'
        case ('é' | 'ê' | 'e')             : return 'e'
        case ('í' | 'í')                    : return 'i'
        case ('ó' | 'ô' | 'õ' | 'o')        : return 'o'
        case ('ú' | 'ü' | 'u')              : return 'u'
        case ('ç' | 'c')                    : return 'c'
        case _                             : return l

def main():
    words = get_words()
    non_repeating = []
    for i in words:
        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        doesnt_repeat = True
        for l in i:
            char = match_letter(l)
            if char in letters:
                letters.remove(char)
            else:
                print(i+' is desqualified')
                doesnt_repeat = False
        if doesnt_repeat:
            non_repeating.append(i)
    print(str(len(non_repeating))+' remain')
    longests = [non_repeating[0]]
    for i in non_repeating:
        if len(i) > len(longests[0]):
            longests = [i]
        elif len(i) == len(longests[0]):
            longests.append(i)

    print(longests)

if __name__ == "__main__":
    main()
