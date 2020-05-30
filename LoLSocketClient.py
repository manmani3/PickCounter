import socket
import json

def parseChampionList(message):
    messages = message.replace('(', '').replace(')', '').replace('],', ']\n').split('\n')

    # data = ast.literal_eval(data)

    result = [[]]

    for i in range(0, len(messages)):
        splitedList = messages[i].replace('[', '').replace(']', '').split('},')

        for j in range(0, len(splitedList)):
            if j == (len(splitedList) - 1):
                result[i].append(json.loads(splitedList[j]))
            else:
                result[i].append(json.loads(splitedList[j] + '}'))

    # return myPickList, yourPickList, myBanList, yourBanList
    return result[0], result[1], result[2], result[3]


def requestRecommendChampionList(myPickList, youPickList, myBanList, yourBanList):
    HOST = '13.125.182.165'
    PORT = 6677

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    message = str((myPickList, youPickList, myBanList, yourBanList))

    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()

    # TODO : decide how to create the recommend champion list format
    print('Received from the server :', parseChampionList(response))

    client_socket.close()
    return parseChampionList(response)
