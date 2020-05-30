def parsePick(position):
    x = position[0]
    y = position[1]

    if (y < 70):
        if (x < 70):
            result = {'id': 103, 'name': 'Ahri'}
        elif (x < 140):
            result = {'id': 84, 'name': 'Akali'}
        elif (x < 210):
            result = {'id': 12, 'name': 'Alista'}
        elif (x < 280):
            result = {'id': 32, 'name': 'Amumu'}
        elif (x < 350):
            result = {'id': 34, 'name': 'Anivia'}
        elif (x < 420):
            result = {'id': 1, 'name': 'Annie'}
        elif (x < 490):
            result = {'id': 523, 'name': 'Aphelios'}
        elif (x < 560):
            result = {'id': 22, 'name': 'Ashe'}
        elif (x < 630):
            result = {'id': 266, 'name': 'Aatrox'}
        elif (x < 700):
            result = {'id': 136, 'name': 'AurelionSol'}
        elif (x < 770):
            result = {'id': 268, 'name': 'Azir'}
        elif (x < 840):
            result = {'id': 432, 'name': 'Bard'}
        elif (x < 910):
            result = {'id': 53, 'name': 'Blitzcrank'}
        elif (x < 980):
            result = {'id': 63, 'name': 'Brand'}
        else :
            result = {'id': 201, 'name': 'Braum'}

    elif (y < 140):
        if (x < 70):
            result = {'id': 51, 'name': 'Caitlyn'}
        elif (x < 140):
            result = {'id': 164, 'name': 'Camille'}
        elif (x < 210):
            result = {'id': 69, 'name': 'Cassiopeia'}
        elif (x < 280):
            result = {'id': 31, 'name': 'Chogath'}
        elif (x < 350):
            result = {'id': 42, 'name': 'Corki'}
        elif (x < 420):
            result = {'id': 122, 'name': 'Darius'}
        elif (x < 490):
            result = {'id': 131, 'name': 'Diana'}
        elif (x < 560):
            result = {'id': 36, 'name': 'Dr.Mundo'}
        elif (x < 630):
            result = {'id': 119, 'name': 'Draven'}
        elif (x < 700):
            result = {'id': 245, 'name': 'Ekko'}
        elif (x < 770):
            result = {'id': 60, 'name': 'Elise'}
        elif (x < 840):
            result = {'id': 28, 'name': 'Evelynn'}
        elif (x < 910):
            result = {'id': 81, 'name': 'Ezreal'}
        elif (x < 980):
            result = {'id': 9, 'name': 'Fiddlesticks'}
        elif (x < 1050):
            result = {'id': 114, 'name': 'Fiora'}

    elif (y < 210):
        if (x < 70):
            result = {'id': 105, 'name': 'Fizz'}
        elif (x < 140):
            result = {'id': 3, 'name': 'Galio'}
        elif (x < 210):
            result = {'id': 41, 'name': 'Gangplank'}
        elif (x < 280):
            result = {'id': 86, 'name': 'Garen'}
        elif (x < 350):
            result = {'id': 150, 'name': 'Gnar'}
        elif (x < 420):
            result = {'id': 79, 'name': 'Gragas'}
        elif (x < 490):
            result = {'id': 104, 'name': 'Graves'}
        elif (x < 560):
            result = {'id': 120, 'name': 'Hecarim'}
        elif (x < 630):
            result = {'id': 74, 'name': 'Heimerdinger'}
        elif (x < 700):
            result = {'id': 420, 'name': 'Illaoi'}
        elif (x < 770):
            result = {'id': 39, 'name': 'Irelia'}
        elif (x < 840):
            result = {'id': 427, 'name': 'Ivern'}
        elif (x < 910):
            result = {'id': 40, 'name': 'Janna'}
        elif (x < 980):
            result = {'id': 59, 'name': 'Jarvan'}
        elif (x < 1050):
            result = {'id': 24, 'name': 'Jax'}


    elif (y < 280):
        if (x < 70):
            result = {'id': 126, 'name': 'Jayce'}
        elif (x < 140):
            result = {'id': 202, 'name': 'Jhin'}
        elif (x < 210):
            result = {'id': 222, 'name': 'Jinx'}
        elif (x < 280):
            result = {'id': 145, 'name': 'Kaisa'}
        elif (x < 350):
            result = {'id': 429, 'name': 'Kalista'}
        elif (x < 420):
            result = {'id': 43, 'name': 'Karma'}
        elif (x < 490):
            result = {'id': 30, 'name': 'Karthus'}
        elif (x < 560):
            result = {'id': 38, 'name': 'Kassadin'}
        elif (x < 630):
            result = {'id': 55, 'name': 'Katarina'}
        elif (x < 700):
            result = {'id': 10, 'name': 'Kayle'}
        elif (x < 770):
            result = {'id': 141, 'name': 'Kayn'}
        elif (x < 840):
            result = {'id': 85, 'name': 'Kennen'}
        elif (x < 910):
            result = {'id': 121, 'name': 'KhaZix'}
        elif (x < 980):
            result = {'id': 203, 'name': 'Kindred'}
        elif (x < 1050):
            result = {'id': 240, 'name': 'Kled'}


    elif (y < 350):
        if (x < 70):
            result = {'id': 96, 'name': 'KogMaw'}
        elif (x < 140):
            result = {'id': 7, 'name': 'LeBlanc'}
        elif (x < 210):
            result = {'id': 64, 'name': 'LeeSin'}
        elif (x < 280):
            result = {'id': 89, 'name': 'Leona'}
        elif (x < 350):
            result = {'id': 127, 'name': 'Lissandra'}
        elif (x < 420):
            result = {'id': 236, 'name': 'Lucian'}
        elif (x < 490):
            result = {'id': 117, 'name': 'Lulu'}
        elif (x < 560):
            result = {'id': 99, 'name': 'Lux'}
        elif (x < 630):
            result = {'id': 54, 'name': 'Malphite'}
        elif (x < 700):
            result = {'id': 90, 'name': 'Malzahar'}
        elif (x < 770):
            result = {'id': 57, 'name': 'Maokai'}
        elif (x < 840):
            result = {'id': 11, 'name': 'MasterYi'}
        elif (x < 910):
            result = {'id': 21, 'name': 'MissFortune'}
        elif (x < 980):
            result = {'id': 62, 'name': 'MonkeyKing'}
        elif (x < 1050):
            result = {'id': 82, 'name': 'Mordekaiser'}


    elif (y < 420):
        if (x < 70):
            result = {'id': 25, 'name': 'Morgana'}
        elif (x < 140):
            result = {'id': 267, 'name': 'Nami'}
        elif (x < 210):
            result = {'id': 75, 'name': 'Nasus'}
        elif (x < 280):
            result = {'id': 111, 'name': 'Nautilus'}
        elif (x < 350):
            result = {'id': 518, 'name': 'Neeko'}
        elif (x < 420):
            result = {'id': 76, 'name': 'Nidalee'}
        elif (x < 490):
            result = {'id': 56, 'name': 'Nocturne'}
        elif (x < 560):
            result = {'id': 20, 'name': 'Nunu'}
        elif (x < 630):
            result = {'id': 2, 'name': 'Olaf'}
        elif (x < 700):
            result = {'id': 61, 'name': 'Orianna'}
        elif (x < 770):
            result = {'id': 516, 'name': 'Ornn'}
        elif (x < 840):
            result = {'id': 80, 'name': 'Pantheon'}
        elif (x < 910):
            result = {'id': 78, 'name': 'Poppy'}
        elif (x < 980):
            result = {'id': 555, 'name': 'Pyke'}
        elif (x < 1050):
            result = {'id': 246, 'name': 'Qiyana'}


    elif (y < 490):
        
        if (x < 70):
            result = {'id': 133, 'name': 'Quinn'}

        elif (x < 140):
            result = {'id': 497, 'name': 'Rakan'}

        elif (x < 210):
            result = {'id': 33, 'name': 'Rammus'}

        elif (x < 280):
            result = {'id': 421, 'name': 'RekSai'}

        elif (x < 350):
            result = {'id': 58, 'name': 'Renekton'}

        elif (x < 420):
            result = {'id': 107, 'name': 'Rengar'}

        elif (x < 490):
            result = {'id': 92, 'name': 'Riven'}

        elif (x < 560):
            result = {'id': 68, 'name': 'Rumble'}

        elif (x < 630):
            result = {'id': 13, 'name': 'Ryze'}

        elif (x < 700):
            result = {'id': 113, 'name': 'Sejuani'}

        elif (x < 770):
            result = {'id': 235, 'name': 'Senna'}

        elif (x < 840):
            result = {'id': 875, 'name': 'Sett'}

        elif (x < 910):
            result = {'id': 35, 'name': 'Shaco'}

        elif (x < 980):
            result = {'id': 98, 'name': 'Shen'}

        elif (x < 1050):
            result = {'id': 102, 'name': 'Shyvana'}


    elif (y < 560):

        if (x < 70):
            result = {'id': 27, 'name': 'Singed'}

        elif (x < 140):
            result = {'id': 14, 'name': 'Sion'}

        elif (x < 210):
            result = {'id': 15, 'name': 'Sivir'}

        elif (x < 280):
            result = {'id': 72, 'name': 'Skarner'}

        elif (x < 350):
            result = {'id': 37, 'name': 'Sona'}

        elif (x < 420):
            result = {'id': 16, 'name': 'Soraka'}

        elif (x < 490):
            result = {'id': 50, 'name': 'Swain'}

        elif (x < 560):
            result = {'id': 517, 'name': 'Sylas'}

        elif (x < 630):
            result = {'id': 134, 'name': 'Syndra'}

        elif (x < 700):
            result = {'id': 223, 'name': 'Tahm Kench'}

        elif (x < 770):
            result = {'id': 163, 'name': 'Taliyah'}

        elif (x < 840):
            result = {'id': 91, 'name': 'Talon'}

        elif (x < 910):
            result = {'id': 44, 'name': 'Taric'}

        elif (x < 980):
            result = {'id': 17, 'name': 'Teemo'}

        elif (x < 1050):
            result = {'id': 412, 'name': 'Thresh'}


    elif (y < 630):
        
        if (x < 70):
            result = {'id': 18, 'name': 'Tristana'}

        elif (x < 140):
            result = {'id': 48, 'name': 'Trundle'}

        elif (x < 210):
            result = {'id': 23, 'name': 'Tryndamere'}

        elif (x < 280):
            result = {'id': 4, 'name': 'TwistedFate'}

        elif (x < 350):
            result = {'id': 29, 'name': 'Twitch'}

        elif (x < 420):
            result = {'id': 77, 'name': 'Udyr'}

        elif (x < 490):
            result = {'id': 6, 'name': 'Urgot'}

        elif (x < 560):
            result = {'id': 110, 'name': 'Varus'}

        elif (x < 630):
            result = {'id': 67, 'name': 'Vayne'}

        elif (x < 700):
            result = {'id': 45, 'name': 'Veigar'}

        elif (x < 770):
            result = {'id': 161, 'name': 'Velkoz'}

        elif (x < 840):
            result = {'id': 254, 'name': 'Vi'}

        elif (x < 910):
            result = {'id': 112, 'name': 'Viktor'}

        elif (x < 980):
            result = {'id': 8, 'name': 'Vladimir'}

        elif (x < 1050):
            result = {'id': 106, 'name': 'Volibear'}


    elif (y < 700):
        if (x < 70):
            result = {'id': 19, 'name': 'Warwick'}
        elif (x < 140):
            result = {'id': 498, 'name': 'Xayah'}
        elif (x < 210):
            result = {'id': 101, 'name': 'Xerath'}
        elif (x < 280):
            result = {'id': 5, 'name': 'XinZhao'}
        elif (x < 350):
            result = {'id': 157, 'name': 'Yasuo'}
        elif (x < 420):
            result = {'id': 83, 'name': 'Yorick'}
        elif (x < 490):
            result = {'id': 350, 'name': 'Yuumi'}
        elif (x < 560):
            result = {'id': 154, 'name': 'Zac'}
        elif (x < 630):
            result = {'id': 238, 'name': 'Zed'}
        elif (x < 700):
            result = {'id': 115, 'name': 'Ziggs'}
        elif (x < 770):
            result = {'id': 26, 'name': 'Zilean'}
        elif (x < 840):
            result = {'id': 142, 'name': 'Zoe'}
        elif (x < 910):
            result = {'id': 143, 'name': 'Zyra'}

    return result


def parseBan(position):
    y = position[1] - 6

    if (y < 32):
        result = {'id': -1, 'name': 'None'}

    elif (y < 64):
        result = {'id': 266, 'name': 'Aatrox'}

    elif (y < 96):
        result = {'id': 103, 'name': 'Ahri'}

    elif (y < 128):
        result = {'id': 84, 'name': 'Akali'}

    elif (y < 160):
        result = {'id': 12, 'name': 'Alistar'}

    elif (y < 192):
        result = {'id': 32, 'name': 'Amumu'}

    elif (y < 224):
        result = {'id': 34, 'name': 'Anivia'}

    elif (y < 256):
        result = {'id': 1, 'name': 'Annie'}

    elif (y < 288):
        result = {'id': 22, 'name': 'Ashe'}

    elif (y < 320):
        result = {'id': 136, 'name': 'AurelionSol'}

    elif (y < 352):
        result = {'id': 268, 'name': 'Azir'}

    elif (y < 384):
        result = {'id': 432, 'name': 'Bard'}

    elif (y < 416):
        result = {'id': 53, 'name': 'Blitzcrank'}

    elif (y < 448):
        result = {'id': 63, 'name': 'Brand'}

    elif (y < 480):
        result = {'id': 201, 'name': 'Braum'}

    elif (y < 512):
        result = {'id': 51, 'name': 'Caitlyn'}

    elif (y < 544):
        result = {'id': 164, 'name': 'Camille'}

    elif (y < 576):
        result = {'id': 69, 'name': 'Cassiopeia'}

    elif (y < 608):
        result = {'id': 31, 'name': 'ChoGath'}

    elif (y < 640):
        result = {'id': 42, 'name': 'Corki'}

    elif (y < 672):
        result = {'id': 122, 'name': 'Darius'}

    elif (y < 704):
        result = {'id': 131, 'name': 'Diana'}

    elif (y < 736):
        result = {'id': 36, 'name': 'Dr. Mundo'}

    elif (y < 768):
        result = {'id': 119, 'name': 'Draven'}

    elif (y < 800):
        result = {'id': 245, 'name': 'Ekko'}

    elif (y < 832):
        result = {'id': 60, 'name': 'Elise'}

    elif (y < 864):
        result = {'id': 28, 'name': 'Evelynn'}

    elif (y < 896):
        result = {'id': 81, 'name': 'Ezreal'}

    elif (y < 928):
        result = {'id': 9, 'name': 'Fiddlesticks'}

    elif (y < 960):
        result = {'id': 114, 'name': 'Fiora'}

    elif (y < 992):
        result = {'id': 105, 'name': 'Fizz'}

    elif (y < 1024):
        result = {'id': 3, 'name': 'Galio'}

    elif (y < 1056):
        result = {'id': 41, 'name': 'Gangplank'}

    elif (y < 1088):
        result = {'id': 86, 'name': 'Garen'}

    elif (y < 1120):
        result = {'id': 150, 'name': 'Gnar'}

    elif (y < 1152):
        result = {'id': 79, 'name': 'Gragas'}

    elif (y < 1184):
        result = {'id': 104, 'name': 'Graves'}

    elif (y < 1216):
        result = {'id': 120, 'name': 'Hecarim'}

    elif (y < 1248):
        result = {'id': 74, 'name': 'Heimerdinger'}

    elif (y < 1280):
        result = {'id': 420, 'name': 'Illaoi'}

    elif (y < 1312):
        result = {'id': 39, 'name': 'Irelia'}

    elif (y < 1344):
        result = {'id': 427, 'name': 'Ivern'}

    elif (y < 1376):
        result = {'id': 40, 'name': 'Janna'}

    elif (y < 1408):
        result = {'id': 59, 'name': 'Jarvan IV'}

    elif (y < 1440):
        result = {'id': 24, 'name': 'Jax'}

    elif (y < 1472):
        result = {'id': 126, 'name': 'Jayce'}

    elif (y < 1504):
        result = {'id': 202, 'name': 'Jhin'}

    elif (y < 1536):
        result = {'id': 222, 'name': 'Jinx'}

    elif (y < 1568):
        result = {'id': 145, 'name': 'Kaisa'}

    elif (y < 1600):
        result = {'id': 429, 'name': 'Kalista'}

    elif (y < 1632):
        result = {'id': 43, 'name': 'Karma'}

    elif (y < 1664):
        result = {'id': 30, 'name': 'Karthus'}

    elif (y < 1696):
        result = {'id': 38, 'name': 'Kassadin'}

    elif (y < 1728):
        result = {'id': 55, 'name': 'Katarina'}

    elif (y < 1760):
        result = {'id': 10, 'name': 'Kayle'}

    elif (y < 1792):
        result = {'id': 141, 'name': 'Kayn'}

    elif (y < 1824):
        result = {'id': 85, 'name': 'Kennen'}

    elif (y < 1856):
        result = {'id': 121, 'name': 'KhaZix'}

    elif (y < 1888):
        result = {'id': 203, 'name': 'Kindred'}

    elif (y < 1920):
        result = {'id': 240, 'name': 'Kled'}

    elif (y < 1952):
        result = {'id': 96, 'name': 'KogMaw'}

    elif (y < 1984):
        result = {'id': 7, 'name': 'LeBlanc'}

    elif (y < 2016):
        result = {'id': 64, 'name': 'LeeSin'}

    elif (y < 2048):
        result = {'id': 89, 'name': 'Leona'}

    elif (y < 2080):
        result = {'id': 127, 'name': 'Lissandra'}

    elif (y < 2112):
        result = {'id': 236, 'name': 'Lucian'}

    elif (y < 2144):
        result = {'id': 117, 'name': 'Lulu'}

    elif (y < 2176):
        result = {'id': 99, 'name': 'Lux'}

    elif (y < 2208):
        result = {'id': 54, 'name': 'Malphite'}

    elif (y < 2240):
        result = {'id': 90, 'name': 'Malzahar'}

    elif (y < 2272):
        result = {'id': 57, 'name': 'Maokai'}

    elif (y < 2304):
        result = {'id': 11, 'name': 'MasterYi'}

    elif (y < 2336):
        result = {'id': 21, 'name': 'MissFortune'}

    elif (y < 2368):
        result = {'id': 62, 'name': 'MonkeyKing'}

    elif (y < 2400):
        result = {'id': 82, 'name': 'Mordekaiser'}

    elif (y < 2432):
        result = {'id': 25, 'name': 'Morgana'}

    elif (y < 2464):
        result = {'id': 267, 'name': 'Nami'}

    elif (y < 2496):
        result = {'id': 75, 'name': 'Nasus'}

    elif (y < 2528):
        result = {'id': 111, 'name': 'Nautilus'}

    elif (y < 2560):
        result = {'id': 518, 'name': 'Neeko'}

    elif (y < 2592):
        result = {'id': 76, 'name': 'Nidalee'}

    elif (y < 2624):
        result = {'id': 56, 'name': 'Nocturne'}

    elif (y < 2656):
        result = {'id': 20, 'name': 'Nunu'}

    elif (y < 2688):
        result = {'id': 2, 'name': 'Olaf'}

    elif (y < 2720):
        result = {'id': 61, 'name': 'Orianna'}

    elif (y < 2752):
        result = {'id': 516, 'name': 'Ornn'}

    elif (y < 2784):
        result = {'id': 80, 'name': 'Pantheon'}

    elif (y < 2816):
        result = {'id': 78, 'name': 'Poppy'}

    elif (y < 2848):
        result = {'id': 555, 'name': 'Pyke'}

    elif (y < 2880):
        result = {'id': 246, 'name': 'Qiyana'}

    elif (y < 2912):
        result = {'id': 133, 'name': 'Quinn'}

    elif (y < 2944):
        result = {'id': 497, 'name': 'Rakan'}

    elif (y < 2976):
        result = {'id': 33, 'name': 'Rammus'}

    elif (y < 3008):
        result = {'id': 421, 'name': 'RekSai'}

    elif (y < 3040):
        result = {'id': 58, 'name': 'Renekton'}

    elif (y < 3072):
        result = {'id': 107, 'name': 'Rengar'}

    elif (y < 3104):
        result = {'id': 92, 'name': 'Riven'}

    elif (y < 3136):
        result = {'id': 68, 'name': 'Rumble'}

    elif (y < 3168):
        result = {'id': 13, 'name': 'Ryze'}

    elif (y < 3200):
        result = {'id': 113, 'name': 'Sejuani'}

    elif (y < 3264):
        result = {'id': 113, 'name': 'Sejuani'}

    elif (y < 3296):
        result = {'id': 35, 'name': 'Shaco'}

    elif (y < 3328):
        result = {'id': 98, 'name': 'Shen'}

    elif (y < 3360):
        result = {'id': 102, 'name': 'Shyvana'}

    elif (y < 3392):
        result = {'id': 27, 'name': 'Singed'}

    elif (y < 3424):
        result = {'id': 14, 'name': 'Sion'}

    elif (y < 3456):
        result = {'id': 15, 'name': 'Sivir'}

    elif (y < 3488):
        result = {'id': 72, 'name': 'Skarner'}

    elif (y < 3520):
        result = {'id': 37, 'name': 'Sona'}

    elif (y < 3552):
        result = {'id': 16, 'name': 'Soraka'}

    elif (y < 3584):
        result = {'id': 50, 'name': 'Swain'}

    elif (y < 3616):
        result = {'id': 517, 'name': 'Sylas'}

    elif (y < 3648):
        result = {'id': 134, 'name': 'Syndra'}

    elif (y < 3680):
        result = {'id': 223, 'name': 'Tahm Kench'}

    elif (y < 3712):
        result = {'id': 163, 'name': 'Taliyah'}

    elif (y < 3744):
        result = {'id': 91, 'name': 'Talon'}

    elif (y < 3776):
        result = {'id': 44, 'name': 'Taric'}

    elif (y < 3808):
        result = {'id': 17, 'name': 'Teemo'}

    elif (y < 3840):
        result = {'id': 412, 'name': 'Thresh'}

    elif (y < 3872):
        result = {'id': 18, 'name': 'Tristana'}

    elif (y < 3904):
        result = {'id': 48, 'name': 'Trundle'}

    elif (y < 3936):
        result = {'id': 23, 'name': 'Tryndamere'}

    elif (y < 3968):
        result = {'id': 4, 'name': 'TwistedFate'}

    elif (y < 4000):
        result = {'id': 29, 'name': 'Twitch'}

    elif (y < 4032):
        result = {'id': 77, 'name': 'Udyr'}

    elif (y < 4064):
        result = {'id': 6, 'name': 'Urgot'}

    elif (y < 4096):
        result = {'id': 110, 'name': 'Varus'}

    elif (y < 4128):
        result = {'id': 67, 'name': 'Vayne'}

    elif (y < 4160):
        result = {'id': 45, 'name': 'Veigar'}

    elif (y < 4192):
        result = {'id': 161, 'name': 'VelKoz'}

    elif (y < 4224):
        result = {'id': 254, 'name': 'Vi'}

    elif (y < 4256):
        result = {'id': 112, 'name': 'Viktor'}

    elif (y < 4288):
        result = {'id': 8, 'name': 'Vladimir'}

    elif (y < 4320):
        result = {'id': 106, 'name': 'Volibear'}

    elif (y < 4352):
        result = {'id': 19, 'name': 'Warwick'}

    elif (y < 4384):
        result = {'id': 498, 'name': 'Xayah'}

    elif (y < 4416):
        result = {'id': 101, 'name': 'Xerath'}

    elif (y < 4448):
        result = {'id': 5, 'name': 'XinZhao'}

    elif (y < 4480):
        result = {'id': 157, 'name': 'Yasuo'}

    elif (y < 4512):
        result = {'id': 83, 'name': 'Yorick'}

    elif (y < 4544):
        result = {'id': 350, 'name': 'Yuumi'}

    elif (y < 4576):
        result = {'id': 154, 'name': 'Zac'}

    elif (y < 4608):
        result = {'id': 238, 'name': 'Zed'}

    elif (y < 4640):
        result = {'id': 115, 'name': 'Ziggs'}

    elif (y < 4672):
        result = {'id': 26, 'name': 'Zilean'}

    elif (y < 4704):
        result = {'id': 26, 'name': 'Zilean'}

    elif (y < 4736):
        result = {'id': 142, 'name': 'Zoe'}

    elif (y < 4768):
        result = {'id': 143, 'name': 'Zyra'}

    return result
