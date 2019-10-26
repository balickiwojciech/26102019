a = input("podaj liczbę : ")
b = input("podaj liczbę : ")
try:
    a = int(a)
    b = int(b)
    print(f"suma liczb to {a+b}. ")
except Exception:
    print("nie byłem w stanie zrutować na inta")
print("koniec")