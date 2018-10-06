from genetic_algo_initial_popu import createInitialPopu
from nextGeneration import nextGeneration

Popu1 = open('./tempFiles/popu1.txt','w')
Popu2 = open('./tempFiles/popu2.txt','w')
Popu3 = open('./tempFiles/popu3.txt','w')

cuisineScore = {"indian":0.33,"italian":0.45,"afghani":0.08,"chinese":0.14}

pop1 = createInitialPopu( 6, 30 )
for item in pop1:
    Popu1.write("%s\n" %item)
pop2 = nextGeneration( pop1, cuisineScore, 3, 0.7 )
for item in pop2:
    Popu2.write("%s\n" %item)
pop3 = nextGeneration( pop2, cuisineScore, 3, 0.6 )
for item in pop3:
    Popu3.write("%s\n" %item)