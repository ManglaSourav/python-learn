# DataFrame
# Series consisted of one column and DataFrame consists of multiple columns. 
# To explain DataFrame, let’s create toy dataset:
import pandas as pd
data={"name":["Bill","Tom","Tim","John","Alex","Vanessa","Kate"],      
      "score":[90,80,85,75,95,60,65],      
      "sport":["Wrestling","Football","Skiing","Swimming","Tennis",
               "Karete","Surfing"],      
      "sex":["M","M","M","M","F","F","F"]}
# print(data)
df = pd.DataFrame(data)
print(df)

# rearraging columns
df=pd.DataFrame(data,columns=["name","sport","sex","score"])
print(df)


# adding a new column
df=pd.DataFrame(data,columns=["name", "sport", "gender", "score", "age"])
print(df)

# changing the index values
df=pd.DataFrame(data,columns=["name", "sport", "gender", "score", "age"],
                index=["one","two","three","four","five","six","seven"])
values=[18,19,20,18,17,17,18]
df["age"]=values
print(df)
print(df.loc[["one","two"]])

# adding new conditional column
df["pass"]=df.score>=70
print(df)


