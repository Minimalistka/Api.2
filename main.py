import requests
from translate import Translator


url = "https://www.fruityvice.com/api/fruit/"
en_translator: Translator = Translator(from_lang='russian', to_lang='english')
inp_fruit = input("Введите название фрукта: ")
print("Получаем ответ от API...")
response: requests.Response = requests.get(url=url+en_translator.translate(inp_fruit))
if response.status_code == 200:
    fruit: dict = response.json()
    family: str = fruit['family']
    order: str = fruit['order']
    genus: str = fruit['genus']
    nutritions: dict = fruit['nutritions']
    print(f"Относится к порядку: {order},")
    print(f"Относится к семейству: {family},")
    print(f"Относится к роду: {genus}.")
    print(f"Пищевая ценность:",
          f" * Калорийность: {nutritions['calories']} ккал,",
          f" * Жиры: {nutritions['fat']} г,",
          f" * Сахара: {nutritions['sugar']} г,",
          f" * Углеводы: {nutritions['carbohydrates']} г,",
          f" * Белки: {nutritions['protein']} г.", sep='\n')
else:
    if response.json().get('error') == "Not found":
        print("Фрукт не найден в базе API.")
    else:
        print(f"Ошибка {response.status_code}.")