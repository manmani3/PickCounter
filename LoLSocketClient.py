import socket
import pickle

def parseChampionList(message):
    message = message.split('#')[2]
    messages = message.replace('(', '').replace(')', '').replace('],', ']\n').split('\n')

    myPickList = [int(i) for i in messages[0].replace('[', '').replace(']', '').split(',')]
    yourPickList = [int(i) for i in messages[1].replace('[', '').replace(']', '').split(',')]
    myBanList = [int(i) for i in messages[2].replace('[', '').replace(']', '').split(',')]
    yourBanList = [int(i) for i in messages[3].replace('[', '').replace(']', '').split(',')]

    return myPickList, yourPickList, myBanList, yourBanList

'''
summonerNameField : str
else params : integer lists
'''
def requestRecommendChampionList(position, summonerNameField, myPickList, youPickList, myBanList, yourBanList):
    # HOST = '13.125.182.165'
    HOST = '127.0.0.1'
    PORT = 6677

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    # use '#' as separator
    message = summonerNameField + '#' + position + '#' + str((myPickList, youPickList, myBanList, yourBanList))
    print('message', message)
    print('parsing :', parseChampionList(message))

    client_socket.send(message.encode())

    try:
        response = pickle.loads(client_socket.recv(1024))
    except Exception as e:
        print(e)

    # TODO : decide how to create the recommend champion list format
    print('Received from the server :', response)

    client_socket.close()
    return response
