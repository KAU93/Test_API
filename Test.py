import requests

URL = 'https://api.hh.ru/vacancies?text={}'

def connectAPI (text):
    urlAPI = URL.format(text)
    return requests.get(urlAPI)

# Тест на позитивный статус
def Test1():
    response = connectAPI("Менеджер по продажам")
    if response.status_code == 200:
        print("Test1 Ok")
    else:
        print("Test1 Bad")

# Тест на ввод пустого запроса
def Test2():
    response = connectAPI("")
    if response.status_code == 200:
        if response.json()["items"] != 0:
            print("Test2 Ok")
        else:
            print("Test2 Bad")
    else:
         print("Test2 Bad")

# Тест на превышение длинны URL
def Test3():
    response = connectAPI("Работник склада" * 800)
    if response.status_code == 414:
        print("Test3 Ok")
    else:
        print("Test3 Bad")
  
# Тест на граничный переход
def Test3_1():
    response = connectAPI("Работник склада" * 750)
    if response.status_code == 502:
        print("Test3_1 Ok")
    else:
        print("Test3_1 Bad")
        print(response)
        
# Тест на ввод спецсимволов
def Test4():
    response = connectAPI("!!!")
    if response.status_code == 200:
        if len(response.json()["items"]) == 0:
            print("Test4 Ok")
        else:
             print("Test4 Bad")
    else:
        print("Test4 Bad")

# Тест на поиск одного из слов
def Test5():
    response = connectAPI("!программист OR !уборщица")
    if response.status_code == 200:
        if len(response.json()["items"]) > 0:
            print("Test5 Ok")
        else:
            print("Test5 Bad")
    else:
        print("Test5 Bad")

# Тест на SQL инъекцию
def Test6():
    response = connectAPI("SELECT compani_id FROM table;")
    if response.status_code == 200:
        if len(response.json()["items"]) == 0:
            print("Test6 Ok")
        else:
            print("Test6 Bad")
            print(len(response.json()["items"]))
    else:
        print("Test6 Bad")



Test1()
Test2()
Test3()
Test3_1()
Test4()
Test5()
Test6()