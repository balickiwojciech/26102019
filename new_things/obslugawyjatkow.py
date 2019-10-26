zmienna = input("podaj liczbę")
try:
    zmienna_integer = int(zmienna)
    print(f"to jest liczba {zmienna_integer}.")
except Exception:
    print("Nie byłem w stanie zrutować na inta")

print("Koniec")
