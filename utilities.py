import numpy as np 
import pandas as pd
import pickle
import sklearn
print("finish")

df = pd.read_csv('models/choosen_dataframe.csv')

loaded_model = pickle.load(open('models/finalized_model.sav', 'rb'))

X = np.load("models/data_similarity.npy")

def predict_pipeline(input):
    df_baju = df[df["subCategory"]!="Bottomwear"]
    df_celana = df[df["subCategory"]=="Bottomwear"]

    df_baju = df_baju[df_baju["gender"]==input["gender"]]
    df_baju = df_baju[df_baju["usage"]==input["usage"]]
    df_baju = df_baju[df_baju["baseColour"]==input["baseColour"]]

    df_celana = df_celana[df_celana["gender"]==input["gender"]]
    df_celana = df_celana[df_celana["usage"]==input["usage"]]
    df_celana = df_celana[df_celana["baseColour"]==input["baseColour"]]

    item =  [df_baju["filename"].sample(n=1).tolist()[0], df_celana["filename"].sample(n=1).tolist()[0]]

    category = ["topWear","bottomWear"]
    row_index = []
    hm = {}
    for i in item:
        row_index.append(df.index[df['filename'] == i].tolist()[0])
    for count,i in enumerate(row_index):
        dist, index = loaded_model.kneighbors(X=X[i,:].reshape(1,-1))
        hm2 = {}
        similar_item = []
        for j in range(10):
            similar_item.append({
                "id":df.loc[index[0][j],"filename"].split(".")[0],
                "link":"https://storage.googleapis.com/image_outfithub/transparent_"+df.loc[index[0][j], "filename"].split(".")[0]+".png"
            })
        hm[f"{category[count]}"] = similar_item
    return hm