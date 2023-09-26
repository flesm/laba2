def process_types(variable):
    if isinstance(variable, list):
        variable = [i for i in variable if isinstance(i, int)]
        if len(variable) == 0:
            print("Спіс пусты або не ўтрымлівае лікаў")
        else:
            counter, sum1 = 0, 0

            for i in variable:
                if counter == 2:
                    sum1 += i

                elif i < 0:
                    counter += 1

            if counter == 2:
                print(f"Сума элементаў спісу пасля другога адмоўнага элмента {sum1}")
            else:
                print("Сума элементаў ня можа быць паллічана, так як у спісе няма хаця б 2-ух адмоўных элементаў")

            print(f"Усе цотныя лікі спісу: {','.join([str(i) for i in variable if i % 2 == 0])}")

    elif isinstance(variable, set):
        if len(variable) == 0:
            print("Мноства пустое або не ўтрымлівае лікі")
        else:
            variable = [i for i in variable if isinstance(i, int)]
            print(f"Максімальны элемент мноства: {max(variable)}")
            print(f"Мінімальны элемент мноства: {min(variable)}")

    elif isinstance(variable, int):
        if variable < 2:
            print("Уведзены адмоўны лік або ніводнага простага ліку не было знойдзена.")
        else:
            lst = [i for i in range(2, variable + 1)]
            i = 0
            while i < len(lst):
                if lst[i] != 0:
                    j = i + lst[i]
                    while j < len(lst):
                        lst[j] = 0
                        j += lst[i]
                i += 1
            print(f"Усе простыя лікі да ўведзенага: {', '.join([str(i) for i in lst if i != 0])}")

    elif isinstance(variable, str):
        variable = [int(i) for i in variable if i.isdigit()]
        if len(variable) == 0:
            print("Уведзены радок пусты або не ўтрымлівае лікі.")
        else:
            print(f"Спіс лікаў, што былі ў радку: {[i for i in variable]}")



