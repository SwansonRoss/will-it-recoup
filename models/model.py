import numpy as np
import pandas as pd
from data import columns as c
import pickle

model_ab = pickle.load(open('models/ab_model.pkl', 'rb'))
model_gb = pickle.load(open('models/gb_model.pkl', 'rb'))
#model_bagging = pickle.load(open('models/bagging_model.pkl', 'rb'))

def queryBuilder(q):
    queryFinal = np.zeros(shape=(1, 11099))
    queryFinal = pd.DataFrame(queryFinal, columns=c.columns, dtype="int")

    for x in q[0]:
        queryFinal[x] = 1

    queryFinal[q[1]] = 1

    queryFinal[q[2]] = 1

    queryFinal[q[3]] = 1

    a1g = "actor1gender_" + q[4]
    queryFinal[a1g] = 1

    queryFinal[q[5]] = 1

    a2g = "actor2gender_" + q[6]
    queryFinal[a2g] = 1

    queryFinal[q[7]] = 1

    a3g = "actor3gender_" + q[8]
    queryFinal[a3g] = 1

    queryFinal[q[9]] = 1

    a4g = "actor4gender_" + q[10]
    queryFinal[a4g] = 1

    queryFinal[q[11]] = 1

    queryFinal[q[12]] = 1
    return queryFinal

def voteRecoup(q):
    votes = 0
    #preds = [model_ab.predict(q)[0], model_gb.predict(q)[0], model_bagging.predict(q)[0]]
    preds = [model_ab.predict(q)[0], model_gb.predict(q)[0]]
    for p in preds:
        if(p):
            votes += 1
    return votes, preds

def willItRecoup(q):
    qf = queryBuilder(q)
    votes, preds = voteRecoup(qf)
    return votes, preds