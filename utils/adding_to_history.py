from prompts import *
from utils.reading import read_json

data = read_json()

def add_task(data, request_name, user_request):
    data[request_name] = {
        "user_request": user_request,
        "history": []
    }

    print(f"Завдання '{request_name}' було додано.")

def result_tr(data, user_request, request_name):
    result_tr = template_request(user_request)
    data[request_name]["history"].append(result_tr.model_dump())
def add_result_prompt(data, full_text, request_name):
    result_prompt = request(
        full_text,
        data[request_name]["history"][0]["tips"][0]["entities_of_interest"],
        data[request_name]["history"][0]["tips"][0]["relation_types"],
        data[request_name]["history"][0]["tips"][0]["keywords"]
    )

    data[request_name]["history"].append(result_prompt.model_dump())

    print(result_prompt)
    print("Аналіз закінчено")