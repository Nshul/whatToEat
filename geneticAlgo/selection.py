import numpy as np, pandas as pd, random

def selection ( population, noOfElite ):
    """
    This selection algorithm uses Roulette Wheel Algorithm to
    determine mating pool for selection
    """
    matingPool = []
    popuPd = pd.DataFrame(np.array(population),columns = ["Index","Fitness"])
    popuPd["cum_sum"] = pd.Fitness.cumsum()
    popuPd["cum_perc"] = 100*popuPd.cum_sum/popuPd.Fitness.sum()
    print (popuPd)

    for i in range(0,noOfElite):
        matingPool.append(population[i][0])
    for i in range(0,len(population) - noOfElite):
        circlePieToBePicked = 100*random.random()
        for i in range(0, len(population)):
            if circlePieToBePicked <= popuPd.iat[i,3]:
                matingPool.append(population[i][0])
                break
    
    return matingPool


# selection([{1:4},{2:5},{3:6},{4:7},{5:2}],3)

# Custom Test to check how to use pandas
# arr = [[1,4],[2,5],[3,6],[4,7],[5,2]]
# print (arr)
# print ("/*/*")
# sarr = pd.DataFrame(np.array(arr),columns = ["Index","Fitness"])
# print (sarr)
# print ("/*/*")
# sarr["cumsum"] = sarr.Fitness.cumsum()
# print (sarr)