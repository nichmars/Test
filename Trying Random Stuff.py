import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import torch

df = pd.read_excel("Filtered Data with Subtypes Again.xlsx")

df2 = df[:-1]
last_thing = df.iloc[-1:]
df_adj = pd.concat([last_thing,df2], ignore_index = True)
df_comb = pd.concat([df, df_adj], axis = 1)

df_comb.to_excel("Appened Years Dataset.xlsx")

accounts = df["Accounts"]
contributions = df["Contributions"]
grants = df["Grants"]
assets = df["Assets"]

accounts_tensor = torch.tensor(accounts.values, dtype = torch.float32)
contributions_tensor = torch.tensor(contributions.values, dtype = torch.float32)
grants_tensor = torch.tensor(grants.values, dtype = torch.float32)
assets_tensor = torch.tensor(assets.values, dtype=torch.float32)
lr = .0001
epochs = 1000
x = torch.zeros(len(accounts_tensor))

for epoch in range(epochs):
    loss = ( x - accounts_tensor)

    loss.backward()

    with torch.no_grad:
        x-= lr*x.grad

    x.grad.zero_()
    if epoch == 0 % 10:
        print(f"Step {epoch+1:02d}: x = {x.item():.4f}, loss = {loss.item():.6f}")