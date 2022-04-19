import json
import os

data = []

def check_data(data_list):
    if not data_list:
        return False
    return True

def get_initial_data():
    file_name = "ChatAppRawData.JSON"
    file_data = open(file_name)
    print("Initialize data with file path: %s" % os.getcwd() + '/' + file_name + "\nInitialize\n")
    return json.load(file_data) 

def get_room_by_id(data_list):
    room_id = int(input("getRoomById: "))
    message = "No room with Id: %s" % room_id
    if not check_data(data_list):
        return print(message)

    res = next((rec for rec in data_list.get('room') if rec["id"] == room_id), False)
    if res:
        return print(res)
    return print(message)

def get_all_room(data_list):
    return print(data_list.get('room') if data_list else list())

def get_chat_by_id(data_list):
    chat_id = int(input("getChatById: "))
    message = "No chat event with Id: %s" % chat_id
    if not check_data(data_list):
        return print(message)

    res = next((rec for rec in data_list.get('chatEvent') if rec["id"] == chat_id), False)
    if res:
        return print(res)
    return print(message)

def get_all_chat_in_room(data_list):
    return print(data_list.get('chatEvent') if data_list else list())

while True:
    action = input("Action\n1. Initialize data\n2. getRoomById\n3. getAllRoom\n4. getChatById\n5. getAllChatInRoom\n\nSelect the action: ")

    if action == "1":
        data = get_initial_data()
    elif action == "2":
        get_room_by_id(data)
    elif action == "3":
        get_all_room(data)
    elif action == "4":
        get_chat_by_id(data)
    elif action == "5":
        get_all_chat_in_room(data)
    else:
        break