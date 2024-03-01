# 1 - wczytywanie
# z linii danych z separatorem, separator źródłowy i docelowy
zdanie1 = input('wpisz dane: ')
zdanie2 = input('wpisz separator źródłowy:\n')
zdanie3 = input('wpisz separator docelowy:\n')

nowe = zdanie1.split(zdanie2)
print(nowe)
nowe = zdanie3.join(nowe)
print(nowe)

# 2 - input() do slice
# input = input("podaj łańcuch znaków: \n")
# stop = round(len(input)/2)
# input1 = input[:stop:]
# input2 = input[stop::]

# print(input[-1:0:-2]) # co drugi od końca

# 3 - metody
# ciag = 'skmlKmoiwmMDqow'
# print(ciag.title())
# print(ciag.capitalize())
# print((ciag.zfill(4)))
# print(ciag.upper())
# print((ciag.count('m')))
# print(ciag.center(30,'-'))

# 4 - metody pt 2
# zdanko = input("zadanie 4: ")
# print(zdanko.isalpha())
# print(zdanko.isascii())
# print(zdanko.isprintable())
# print(zdanko.istitle())
# print(zdanko.isupper())
# print(f"Łańcuch {zdanko} isdecimal: {zdanko.isdecimal()}")

# 5
# print('{} - {}'.format('lol', 'olo'))
# a = 'olo'
# b = 'lol'
# print(f"{b} - {a}")
# print(f'{a:>10}')
# print(f'{b:.1}')
# c = 4.593209043829423049582530244823
# d = -45
# print(f'{c:.2f}')
# print(f'{d:=+5d}')

# 6 - listing 7
# symbole = {
#     'alfa greckie': '\u03B1',
#     'beta greckie': '\u03B2',
#     'omega greckie': '\u03C9',
#     'funt': '\u00A3',
#     'bitcoin': '\u20BF',
#     'euro': '\u20AC',
#     'dolar': '\u0024',
#     'yen': '\u00A5',
#     'pieniądze idk': '\u20BD',
#     'celciusz': '\u2103'
# }
#
# for nazwa, symbol in symbole.items():
#     print(f"{nazwa}: {symbol} (Unicode: {ord(symbol)})")


