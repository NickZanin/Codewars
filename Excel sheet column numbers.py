def title_to_number(title):
    i = 0
    result = 0
    while i < len(title):
        result += (ord(title[i]) - 64)
        i += 1
        print( i, ' -- ', result)
    return result






if __name__ == '__main__':
    print(title_to_number('AB'))