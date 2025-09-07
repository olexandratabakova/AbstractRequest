import json
from utils.reading import read_json, read_user_text
from utils.adding_to_history import add_task, result_tr, add_result_prompt

file_path = "files/tasks_data.json"
data = read_json()

while True:
    user_query = input("Створити нове завдання? (Так/Ні) ").lower()
    if user_query == "ні":
        print("Алгоритм закінчено")
        break

    elif user_query == "так":
        request_name = input("Введіть назву для вашого завдання: ")
        user_request = input("Введіть завдання для аналізу вашого тексту: ")
        add_task(data, request_name, user_request)

        print("Поля для шаблоного запиту записуються...")
        result_tr(data, user_request, request_name)
        print("Поля для шаблоного запиту записано")

        full_text = read_user_text()

        if full_text is None:
            continue
            
        else:
            print("Текст прийнято, аналіз розпочався...")
            add_result_prompt(data, full_text, request_name)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    else:
        print("Неправильний запит")