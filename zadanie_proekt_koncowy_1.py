"""
1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w stringu były najwięcej
i zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4

2. (z gwiazdką) Stworzyć funkcję która przyjmie listę w liście elementem może być kolejna lista, lub liczba całkowita, zadaniem
funkcji jest 'spłaszczenie listy' i podanie wyniku, czyli, jeśli funkcja przyjmie listę [1, 2, [3, [4, 5]], 6, [[[7]]], 8, 9, 10]
to wynik powinien wynosić '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', liczba zagnieżdżeń w liście może być nieskończona, nie możemy zakładać
konkretnej liczby.
"""

"""
Po zrobieniu zadania, pushujemy wynik na nowy branch który stworzyliśmy i tworzymy pull requesta, pull request możemy zmerge;ować tylko
po akceptacji trenera
"""

# text = "lasha tkeshelashvili"
# most_frequent = max(set(text), key=text.count)
# print(most_frequent)

def max_frequent_letter(text):
    max_number  = 0
    any_letter = ""
    for letter in text:
        number = text.count(letter)
        if max_number < number:
            max_number = number
            any_letter = letter
    return f"{any_letter} = {max_number}"
print(max_frequent_letter("laasha tkeshelashvili"))
