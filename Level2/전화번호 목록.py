from collections import defaultdict

phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    phone_dict = defaultdict()
    phone_book.sort()

    for number in phone_book:
        word = ''
        for i in number:
            word += i
            if phone_dict.get(word, False):
                return False
        phone_dict[number] = True

    return True

print(solution(phone_book))