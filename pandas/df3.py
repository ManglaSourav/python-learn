import pandas as pd

scores={ "Math" : {"A":85,"B":90,"C":95},  
         "Physics" :{"A":90,"B":80,"C":75} 
         }

scores_df=pd.DataFrame(scores)
print(scores_df)

# transpose
print(scores_df.T)

scores_df.index.name="name"
scores_df.columns.name="lesson"

print("\n\n",scores_df)

print(scores_df.values)

# The index attribute makes the data immutable. The user can no longer make changes to the data.
scores_index=scores_df.index
print(scores_index)
scores_index[1]="Jack" #this will throw error
