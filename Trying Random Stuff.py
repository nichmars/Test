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
cf = pd.read_excel("Imputing2.xlsx")
df = df[df["Year"]==2019]
accounts = df["Accounts"]
contributions = df["Contributions"]
grants = df["Grants"]
assets = df["Assets"]
accounts_2 = df["Accounts_2"]
contributions_2 = df["Contributions_2"]
grants_2 = df["Grants_2"]
assets_2 = df["Assets_2"]

x = pd.concat([accounts, contributions, grants, assets], axis = 1)
y = pd.concat([accounts_2, contributions_2, grants_2, assets_2], axis = 1)

x_scaler = StandardScaler()
y_scaler = StandardScaler()

x_scaled = x_scaler.fit_transform(x)
x_scaled_tensor = torch.tensor(x_scaled, dtype = torch.float32)
y_scaled = y_scaler.fit_transform(y)
y_scaled_tensor = torch.tensor(y_scaled, dtype = torch.float32)

lr = .0001
epochs = 1000

model = torch.nn.Linear(4,4)
optimizer = torch.optim.Adam(model.parameters(), lr =lr)
criterion = torch.nn.MSELoss()

for epoch in range(epochs):
    predictions = model(x_scaled_tensor)
    loss = criterion(predictions, y_scaled_tensor)

    optimizer.zero_grad()
    loss.backward()

    optimizer.step()

    if epoch %50 == 0:
        print(f"Step {epoch+1:02d}: loss = {loss.item():.6f}")

# torch.save(model.state_dict(), "2019model.pth")

df2 = df[df[df["Year"]==2020]]
accounts2 = df2["Accounts"]
contributions2 = df2["Contributions"]
grants2 = df2["Grants"]
assets2 = df2["Assets"]
accounts_22 = df2["Accounts_2"]
contributions_22 = df2["Contributions_2"]
grants_22 = df2["Grants_2"]
assets_22 = df2["Assets_2"]

x2020 = pd.concat([accounts2, contributions2, grants2, assets2], axis = 1)
y2020 = pd.concat([accounts_22, contributions_22, grants_22, assets_22], axis = 1)

x2020_scaler = StandardScaler()
y2020_scaler = StandardScaler()

x2020_scaled = x_scaler.transform(x2020)
x2020_scaled_tensor = torch.tensor(x2020_scaled, dtype = torch.float32)
y2020_scaled = y_scaler.transform(y2020)
y2020_scaled_tensor = torch.tensor(y2020_scaled, dtype = torch.float32)  

with torch.no_grad():
    predictions_scaled = model(x2020_scaled_tensor)
loss=criterion(predictions_scaled, y2020_scaled_tensor)
print(loss)
predictions = y_scaler.inverse_transform(predictions_scaled.numpy())

def mse(x, y):
    (x-y)**2/len(x)

pred_cols = cf[["predicted_accounts", "predicted_contributions",  "predicted_grants", "predicted_assets"]]
print(mse(y, pred_cols))