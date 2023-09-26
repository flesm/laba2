def convert_to_int(value):
    try:
        if isinstance(value, int):
            raise Exception("Уведзенае значэнне і ёсць лік.")
        result = int(value)
        print(f"Вынік пераўтварэння ў цэлы лік: {result}")
    except ValueError:
        print(f"Немагчыма пераўтварыць '{value}' у цэлы лік!")
    except TypeError:
        print("Вы няправільна ўвялі дадзеныя!")
    except Exception as e:
        print(e)
    finally:
        print("Блок finally выкананы.")