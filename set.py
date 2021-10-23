import random as rd
import math as m

def checkset(a, b, c, signs):
    for i in range(signs):
        if ((a[i] == b[i] == c[i]) or (a[i] != b[i] and a[i] != c[i] and b[i] != c[i])) != True:
            return False
    return True

def findset(hm, cards, signs):
    checked = []
    for i in range(hm):
        for j in range(hm):
            for k in range(hm):
                if (i != j and i != k and j != k):
                    if (sorted([i, j, k]) not in checked):
                        checked.append(sorted([i, j, k]))
                        if checkset(cards[i], cards[j], cards[k], signs):
                            return True
    return False

def findchance(iter, fromc, toc, signs):
    #iter = 100000
    #fromc = 3
    #toc = 81
    #hm = 3
    #card = [0, 0, 0, 0]

    for hm in range(fromc, toc+1):
        luckoper = 0

        for _ in range(iter):
            cards = []
            for q in range(hm):
                need = True
                while need:
                    if signs == 4:
                        newcard = [rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2)]
                    elif signs == 3:
                        newcard = [rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2)]
                    else:
                        newcard = [rd.randint(0, 2), rd.randint(0, 2)]

                    if (newcard in cards) != True:
                        cards.append(newcard)
                        need = False

            if findset(hm, cards, signs):
                luckoper +=1


        if int(luckoper) != 0:
            #print(luckoper)
            print(str(hm) +  ": " + str(100/(iter/luckoper)) + "%")
        else:
            print(str(hm) + " 0%")

def findallsets(hm, cards, signs):
    checked = []
    res = 0
    for i in range(hm):
        for j in range(hm):
            for k in range(hm):
                if (i != j and i != k and j != k):
                    if (sorted([i, j, k]) not in checked):
                        checked.append(sorted([i, j, k]))
                        if checkset(cards[i], cards[j], cards[k], signs):
                            res+=1
    return res

def maxsetsOLD(iter, fromc, toc, signs):
    for hm in range(fromc, toc+1):
        maxs = 0
        for _ in range(iter):
            cards = []
            thissets = 0
            for q in range(hm):
                need = True
                while need:
                    if signs == 4:
                        newcard = [rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2)]
                    elif signs == 3:
                        newcard = [rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2)]
                    else:
                        newcard = [rd.randint(0, 2), rd.randint(0, 2)]
                    if (newcard in cards) != True:
                        cards.append(newcard)
                        need = False

            thissets = findallsets(hm, cards, signs)

            if thissets > maxs:
                maxs = thissets

        print(str(hm) + ": " + str(maxs))


def maxsets(iter, hm, signs):
    maxs = 0
    comb = m.comb(81, hm)

    if iter > comb:
        iter = comb


    ########################
    for _ in range(iter):
        thiss = 0
        cards = []
        for q in range(hm):
            need = True
            while need:
                if signs == 4:
                    newcard = [rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2)]
                elif signs == 3:
                    newcard = [rd.randint(0, 2), rd.randint(0, 2), rd.randint(0, 2)]
                else:
                    newcard = [rd.randint(0, 2), rd.randint(0, 2)]

                if (newcard in cards) != True:
                    cards.append(newcard)
                    need = False

        ###############

        checked = []
        for i in range(hm):
            for j in range(hm):
                if (i != j) and ((cards[i] not in checked) and (cards[j] not in checked)):
                    needcard = [(0 - cards[i][0] - cards[j][0])%3, (0 - cards[i][1] - cards[j][1])%3, (0 - cards[i][2] - cards[j][2])%3, (0 - cards[i][3] - cards[j][3])%3]
                    checked.append(cards[i])
                    checked.append(cards[j])
                    if needcard in cards:
                        thiss += 1

        ##################

        if thiss > maxs:
            maxs = thiss

    return maxs


for i in range(26, 82):
    print(str(i) + ": " + str(maxsets(1000000, i, 4)))
#print(m.comb(81, 4))