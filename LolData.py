import json


def fileToJson(path):
    file = open(path, 'r')

    string = file.read()

    string = string.replace("", "\"")
    string = string.replace("True", "\"True\"")
    string = string.replace("False", "\"False\"")
    string = string.replace("}}]}", "}}]},")
    string = string[:-1]
    string = '[' + string + ']'

    json_data = json.loads(string)

    return json_data


'''
params
    myPickList, yourPickList, myBanList, yourBanList : integer lists
'''


def extractMatchedGame(myPickList, yourPickList, myBanList, yourBanList):
    games = fileToJson('D:\\Anaconda_3\\envs\pengsu\\kr_top-tier_gameData_v1.txt')

    matchedGame = []
    for game in games:
        blueTeamChampionList = list((player['championId'] for player in game['participants'][:5]))
        redTeamChampionList = list((player['championId'] for player in game['participants'][5:]))

        if all(champ in blueTeamChampionList for champ in myPickList):
            if all(champ in redTeamChampionList for champ in yourPickList):
                matchedGame.append(game)
                continue

        if all(champ in redTeamChampionList for champ in myPickList):
            if all(champ in blueTeamChampionList for champ in yourPickList):
                matchedGame.append(game)
                continue

    return matchedGame


champMap = {
    'Unknown' : 0,
    'Zac': 154,
    'Aatrox': 266,
    'Thresh': 412,
    'Tryndamere': 23,
    'Gragas': 79,
    'Cassiopeia': 69,
    'AurelionSol': 136,
    'Ryze': 13,
    'Poppy': 78,
    'Sion': 14,
    'Annie': 1,
    'Jhin': 202,
    'Karma': 43,
    'Nautilus': 111,
    'Kled': 240,
    'Lux': 99,
    'Ahri': 103,
    'Olaf': 2,
    'Viktor': 112,
    'Anivia': 34,
    'Singed': 27,
    'Garen': 86,
    'Lissandra': 127,
    'Maokai': 57,
    'Morgana': 25,
    'Evelynn': 28,
    'Fizz': 105,
    'Heimerdinger': 74,
    'Zed': 238,
    'Rumble': 68,
    'Mordekaiser': 82,
    'Sona': 37,
    'KogMaw': 96,
    'Katarina': 55,
    'Lulu': 117,
    'Ashe': 22,
    'Karthus': 30,
    'Alistar': 12,
    'Darius': 122,
    'Vayne': 67,
    'Varus': 110,
    'Udyr': 77,
    'Leona': 89,
    'Jayce': 126,
    'Syndra': 134,
    'Pantheon': 80,
    'Riven': 92,
    'KhaZix': 121,
    'Corki': 42,
    'Azir': 268,
    'Caitlyn': 51,
    'Nidalee': 76,
    'Kennen': 85,
    'Galio': 3,
    'Veigar': 45,
    'Bard': 432,
    'Gnar': 150,
    'Malzahar': 90,
    'Graves': 104,
    'Vi': 254,
    'Kayle': 10,
    'Irelia': 39,
    'LeeSin': 64,
    'Illaoi': 420,
    'Elise': 60,
    'Volibear': 106,
    'Nunu': 20,
    'TwistedFate': 4,
    'Jax': 24,
    'Shyvana': 102,
    'Kalista': 429,
    'Dr.Mundo': 36,
    'Ivern': 427,
    'Diana': 131,
    'TahmKench': 223,
    'Brand': 63,
    'Sejuani': 113,
    'Vladimir': 8,
    'RekSai': 421,
    'Quinn': 133,
    'Akali': 84,
    'Taliyah': 163,
    'Tristana': 18,
    'Hecarim': 120,
    'Sivir': 15,
    'Lucian': 236,
    'Rengar': 107,
    'Warwick': 19,
    'Skarner': 72,
    'Malphite': 54,
    'Yasuo': 157,
    'Xerath': 101,
    'Teemo': 17,
    'Nasus': 75,
    'Renekton': 58,
    'Draven': 119,
    'Shaco': 35,
    'Swain': 50,
    'Talon': 91,
    'Janna': 40,
    'Ziggs': 115,
    'Ekko': 245,
    'Orianna': 61,
    'Fiora': 114,
    'Fiddlesticks': 9,
    'ChoGath': 31,
    'Rammus': 33,
    'LeBlanc': 7,
    'Soraka': 16,
    'Zilean': 26,
    'Nocturne': 56,
    'Jinx': 222,
    'Yorick': 83,
    'Urgot': 6,
    'Kindred': 203,
    'MissFortune': 21,
    'MonkeyKing': 62,
    'Blitzcrank': 53,
    'Senna': 235,
    'Shen': 98,
    'Braum': 201,
    'XinZhao': 5,
    'Twitch': 29,
    'MasterYi': 11,
    'Taric': 44,
    'Amumu': 32,
    'Gangplank': 41,
    'Trundle': 48,
    'Kassadin': 38,
    'VelKoz': 161,
    'Zyra': 143,
    'Nami': 267,
    'JarvanIV': 59,
    'Ezreal': 81,
    'Yuumi': 350,
    'KaiSa': 145,
    'Neeko': 518,
    'Zoe': 142,
    'Xayah': 498,
    'Sylas': 517,
    'Kayn': 141,
    'Ornn': 516,
    'Pyke': 555,
    'Camille': 164,
    'Qiyana': 246,
    'Rakan': 497,
    'Aphelios': 523,
    'Sett': 875
}

def getChampionName(championId):
    return list(champMap.keys())[list(champMap.values()).index(championId)]

def getChampionId(championName):
    championName = championName.replace(' ', '')
    return champMap[championName]

### main ###
'''
myPick = [145]
yourPick = [122, 11]
myBan = [236, 117, 99, 54, 90]
yourBan = [57, 11, 21, 62, 82]

matchedGames = extractMatchedGame(myPick, yourPick, myBan, yourBan)
print('myPick', myPick)
print('yourPick', yourPick)
print('matched games : ', len(matchedGames))

print(getChampionId('Kayn'))
print(getChampionName(142))
'''