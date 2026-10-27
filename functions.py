#Palindrom
def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

#Ciąg fibonacciego
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Liczba nie może być ujemna")
        
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    a = 0
    b = 1
    for i in range(2, n + 1):
        wynik = a + b
        a = b
        b = wynik
        
    return b

#volvo
def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1
    return count

#Discount
def calculate_discount(price: float, discount: float) -> float:

    if discount < 0 or discount > 1:
        raise ValueError("Zniżka musi być wartością z zakresu od 0 do 1")
    return price - (price * discount)

#flatten
def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

#word
def word_frequencies(text: str) -> dict:
    for char in ".,!?()[]{};:'\"":
        text = text.replace(char, " ")
        
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True