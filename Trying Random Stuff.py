import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
import torch

# df = pd.read_excel("Filtered Data with Subtypes Again.xlsx")

# df_adj = df.shift(1)
# df_adj = df_adj.rename(columns={
#     'ein':'ein_2',
#     'Year':'Previous Year',
#     'Accounts':'Accounts_2',
#     'Contributions': 'Contributions_2',
#     'Grants':'Grants_2',
#     'Assets': 'Assets_2',
# })
# df_adj = df_adj.drop(columns=["Type", "subtype"])
# df_comb = pd.concat([df, df_adj], axis = 1)

# df_comb.to_excel("Appened Years Dataset.xlsx")

df = pd.read_excel("Appened Years Dataset.xlsx")

df = df[df["Year"]==2019]
accounts = df["Accounts"]
contributions = df["Contributions"]
grants = df["Grants"]
assets = df["Assets"]
accounts_2 = df["Accounts_2"]
contributions_2 = df["Contributions_2"]
grants_2 = df["Grants_2"]
assets_2 = df["Assets_2"]

y = pd.concat([accounts, contributions, grants, assets], axis = 1)
x = pd.concat([accounts_2, contributions_2, grants_2, assets_2], axis = 1)

scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)
x_scaled_tensor = torch.tensor(x_scaled, dtype = torch.float32)
y_scaled = scaler.fit_transform(y)
y_scaled_tensor = torch.tensor(y_scaled, dtype = torch.float32)

lr = .0001
epochs = 1000

for epoch in range(epochs):
    loss = (x_scaled_tensor - y_scaled_tensor)**2

    loss.backward()

    with torch.no_grad:
        x-= lr*x.grad

    x.grad.zero_()
    if epoch == 0 % 10:
        print(f"Step {epoch+1:02d}: x = {x.item():.4f}, loss = {loss.item():.6f}")