import matrix
import operations_with_types
import tef
import triangle

while True:
    print("\n\nМеню заданняў:\n"
          "1 - Заданне знаходжання перыметра і плошчы раўнастаронняга трохвугольніка.\n"
          "2 - Задание на гласные и согласные буквы.\n"
          "3 - Заданне з матрыцай.\n"
          "4 - Заданне на try/catch/finally.\n"
          "Іншы лік - Выхад з праграмы")

    while True:
        try:
            var = int(input("Увядзіце лік для выбару задання: "))
            print('\n')
            break
        except ValueError:
            print("Вы ўвялі не лік.")

    match var:
        case 1:

            while True:
                try:
                    a = int(input("Увядзіце значэнне стараны трохвугольніка: "))
                    if a < 0:
                        raise Exception("Старана трохвугольніка ня можа быць адмоўнай.")
                    break
                except ValueError:
                    print("Вы ўвялі не лік.")
                except Exception as e:
                    print(e)

            print(f"Значэнні перыметра і плошчы трохвугольніка адпаведна роўныя: {triangle.triangle(a)}")


        case 2:
            operations_with_types.process_types([1, 2, 3])
            operations_with_types.process_types({1, 2, 3})
            operations_with_types.process_types(1231)
            operations_with_types.process_types("sdfsfs92384273947ksjdhf9832")

        case 3:
            print("Увядзіце памер двумернага масіва лікаў: ")
            while True:
                try:
                    n, m = int(input("Колькасць радкоў: ")), int(input("Колькасць слупкоў: "))
                    if n < 1 or m < 1:
                        print("Двумерны масіў ня можа мець такі памер.")
                        continue
                    break
                except ValueError:
                    print("Вы ўвялі не лік.")

            lst = [[0] * m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    el = input(f"Увядзіце элемент для радка {i} і слупка {j}: ")
                    lst[i][j] = el

            print("Увядзіце індэксы слупкоў, якія вы хацелі б памяняць: ")
            while True:
                try:
                    i, j = int(input("Прешы слупок: ")), int(input("Другі слупок: "))
                    if i < 0 or i > m - 1 or j < 0 or j > m - 1:
                        print("Слупка з такім індэксам няма.")
                        continue
                    break
                except ValueError:
                    print("Вы ўвялі не лік.")

            print("Уведзеная матрыца: ")
            for row in lst:
                print('  '.join(str(elem).rjust(2) for elem in row))

            new_lst = matrix.process_matrix(lst, i, j)

            print("Змененая матрыца: ")
            for row in new_lst:
                print('  '.join(str(elem).rjust(2) for elem in row))

        case 4:
            tef.convert_to_int(123)
            tef.convert_to_int("123")
            tef.convert_to_int("abc")
            tef.convert_to_int(None)

        case _:
            exit()
