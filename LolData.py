import json
import requests


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
    'Unknown': 0,
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
    'Sett': 875,
    'Senna': 235,
    'Wukong': 62
} # no space, no apostrophe(') in champion name

def getChampionName(championId):
    try:
        result = list(champMap.keys())[list(champMap.values()).index(championId)]
    except Exception as e:
        result = 'Unknown'

    if result == 'Unknown':
        print('can not find matched champion name :', championId)

    return result


def getChampionId(championName):
    championName = championName.replace('\'', '').replace(' ', '').split('&')[0]
    try:
        result = champMap[championName]
    except Exception as e:
        result = 0

    if result == 0:
        print('can not find matched champion id from map :', championName)
    return result


champCluster = { # no space, no apostrophe(') in champion name
    1: ['Darius', 'Yorick', 'Illaoi', 'Udyr'],
    2: ['Aatrox', 'Dr.Mundo', 'Tryndamere', 'Garen', 'Riven', 'Gnar', 'Katarina', 'Kled', 'Mordekaiser', 'Renekton',
        'Rengar', 'Rumble', 'RekSai', 'Shyvana', 'Sett', 'Vladimir', 'Zac', 'Yasuo'],
    3: ['Akali', 'Kennen', 'Zed', 'LeeSin', 'Shen'],
    4: ['Quinn', 'Lucian', 'Jayce', 'Kalista', 'Corki', 'Kindred', 'Vayne', 'Ezreal', 'Varus', 'Aphelios', 'Ashe',
        'Caitlyn', 'MissFortune', 'Draven', 'KaiSa', 'Sivir', 'Jinx', 'Jhin', 'Twitch', 'KogMaw', 'Xayah', 'Tristana',
        'Thresh', 'Senna'],
    5: ['Fiora', 'Camille', 'ChoGath', 'Ekko', 'Galio', 'Gangplank', 'Gragas', 'Singed', 'Hecarim', 'Nasus', 'Urgot',
        'Irelia', 'Jax', 'Sion', 'Talon', 'Malphite', 'Kayn', 'Fizz', 'Diana', 'Pantheon', 'Qiyana', 'Maokai',
        'Nocturne', 'Olaf', 'Ornn', 'Pyke', 'Graves', 'Trundle', 'Shaco', 'Poppy', 'Evelynn', 'Warwick', 'MasterYi',
        'Nunu', 'Ivern', 'JarvanIV', 'Rammus', 'XinZhao', 'KhaZix', 'Vi', 'Sejuani', 'Amumu', 'Sylas', 'Volibear',
        'Blitzcrank', 'Leona', 'Nautilus', 'Taric', 'Wukong', 'MonkeyKing', 'Alistar', 'Rakan', 'Braum', 'TahmKench'],
    6: ['Cassiopeia', 'Teemo', 'Fiddlesticks', 'Heimerdinger', 'Kayle', 'TwistedFate', 'Kassadin', 'Zoe', 'LeBlanc',
        'Ahri', 'Orianna', 'Malzahar', 'Lux', 'Annie', 'Anivia', 'AurelionSol', 'Lissandra', 'Neeko', 'Veigar',
        'Viktor', 'Azir', 'Elise', 'Ryze', 'Nidalee', 'Karthus', 'Swain', 'Taliyah', 'Syndra', 'VelKoz', 'Bard',
        'Yuumi', 'Lulu', 'Morgana', 'Soraka', 'Janna', 'Xerath', 'Karma', 'Zyra', 'Sona', 'Nami', 'Ziggs', 'Brand',
        'Zilean'],
}

def getChampionCluster(championName):
    championName = championName.replace('\'', '').replace(' ', '').split('&')[0]
    for key, value in champCluster.items():
        for champion in value:
            if championName == champion:
                return key
    print('can not find the cluster : ', championName)
    return 0

def request_URL(queryKey):
    base_url = 'https://kr.api.riotgames.com'
    RIOT_API_KEY = 'RGAPI-5b02e909-777a-4ede-b386-02d0be16ceef'

    url = base_url + queryKey + '?api_key=' + RIOT_API_KEY
    try:
        response = requests.get(url)
        # Reference : https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
        retry_code = [429, 500, 503, 504]
        if response.status_code in retry_code:
            print('Warning: %d, %s'%(response.status_code, response.reason))
            response = requests.get(url)
        if response.status_code != 200:
            print('Error: Occured request error!')
            print('- URL :', url)
            print('- status_code :', response.status_code)
            print('- reason :', response.reason)
            # raise SystemExit('Occured request error! (%d, %s)'%(response.status_code, response.reason))
            print(('Occured request error! (%d, %s)'%(response.status_code, response.reason)))
        return response
    except requests.exceptions.RequestException as e:
        # raise SystemExit(e)
        print('request_URL', e)

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