import pandas as pd
import numpy as np
import copy
import matplotlib
headers = ["a", "b", "c", "e", "f",
           "g", "h", "i", "j",
           "k", "l", "m", "n"]
df=pd.read_csv("mandis_english.csv.csv",
                  header=None, names=headers, na_values="?")
df.info()
print(df.head())
obj_df = df.select_dtypes(include=['object']).copy()
print(obj_df.head())
print(obj_df["c"].value_counts())
cleanup_states = {
                "c": {"Uttar Pradesh": 1,
                 "Punjab ": 2,
                  "Haryana": 3,
"Madhya Pradesh":                  4,
"Kerala":                          5,
"Himachal Pradesh":                6,
"Maharashtra":                     7,
"Uttarakhand":                     8,
"Rajasthan":                       9,
"Odisha":                          10,
"Gujarat":                         11,
"Jammu and Kashmir":               12,
"Karnataka":                       13,
"Jharkhand":                       14,
"West Bengal":                      15,
"Assam":                            16,
"Tripura":                          17,
"Chhattisgarh":                     18,
"Bihar":                            19,
"Tamil Nadu":                       20,
"Delhi":                            21,
"Telangana":                        22,
"Andhra Pradesh":                   23,
"Mizoram":                          24,
"Chandigarh":                       25,
"Nagaland":                         26,
"Andaman and Nicobar Islands":     27,
"Arunachal Pradesh":                28,
"Meghalaya":                        29,
"Goa":                            30,
"Missouri": 31}}
obj_df.replace(cleanup_states, inplace=True)
print(obj_df["c"])
obj_df.to_csv('state_encoded.csv')
