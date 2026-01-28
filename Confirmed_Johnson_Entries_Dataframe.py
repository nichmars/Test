# %%
import pandas as pd
from sklearn.linear_model import LinearRegression

j_df = pd.read_excel('C:/Users/ryanv/Downloads/Annual+DAF+Report+2025+Dataset.xlsx', sheet_name='data')


j_df_conf = j_df.copy()

j_df_conf.loc[j_df_conf['source_record'] == "IRS 990", 'source_record'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_record'] == "NPT Historical Data", 'source_record'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_record'] == "Paper Submission", 'source_record'] = "Confirmed"

j_df_conf.loc[j_df_conf['source_number_of_accounts'] == "IRS 990", 'source_number_of_accounts'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_number_of_accounts'] == "NPT Historical Data", 'source_number_of_accounts'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_number_of_accounts'] == "Paper Submission", 'source_number_of_accounts'] = "Confirmed"

j_df_conf.loc[j_df_conf['source_total_daf_contributions'] == "IRS 990", 'source_total_daf_contributions'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_total_daf_contributions'] == "NPT Historical Data", 'source_total_daf_contributions'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_total_daf_contributions'] == "Paper Submission", 'source_total_daf_contributions'] = "Confirmed"

j_df_conf.loc[j_df_conf['source_total_daf_grants'] == "IRS 990", 'source_total_daf_grants'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_total_daf_grants'] == "NPT Historical Data", 'source_total_daf_grants'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_total_daf_grants'] == "Paper Submission", 'source_total_daf_grants'] = "Confirmed"

j_df_conf.loc[j_df_conf['source_eoy_daf_assets'] == "IRS 990", 'source_eoy_daf_assets'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_eoy_daf_assets'] == "NPT Historical Data", 'source_eoy_daf_assets'] = "Confirmed"
j_df_conf.loc[j_df_conf['source_eoy_daf_assets'] == "Paper Submission", 'source_eoy_daf_assets'] = "Confirmed"


j_df_conf = j_df_conf[(j_df_conf['source_record'] == 'Confirmed') & (j_df_conf['source_number_of_accounts'] == 'Confirmed') & (j_df_conf['source_total_daf_contributions'] == 'Confirmed') & (j_df_conf['source_total_daf_grants'] == 'Confirmed') & (j_df_conf['source_eoy_daf_assets'] == 'Confirmed')]


j_df_conf_19 = j_df_conf[(j_df_conf['fiscal_year_end'] == 2019)]
j_df_conf_20 = j_df_conf[(j_df_conf['fiscal_year_end'] == 2020)]
j_df_conf_21 = j_df_conf[(j_df_conf['fiscal_year_end'] == 2021)]
j_df_conf_22 = j_df_conf[(j_df_conf['fiscal_year_end'] == 2022)]
j_df_conf_23 = j_df_conf[(j_df_conf['fiscal_year_end'] == 2023)]
j_df_conf_24 = j_df_conf[(j_df_conf['fiscal_year_end'] == 2024)]


#for type: 0=community 1=single-issue 2=national
lin_reg_data_ex = {"2019 noda": [395, 137, 51, 25, 813],
                   "2019 tdc": [20802830, 895180, 127635, 340863, 4309216],
                   "2019 tdg": [21188325, 5006252, 199603, 362279, 4945487],
                   "2019 eda": [218364523, 16720283, 4371183, 445464, 23061204],
                   "2019 type": [0, 0, 0, 2, 1],
                   "2020 tdc": [26448400, 741937, 298502, 98091, 4909710]}

ex_df = pd.DataFrame(lin_reg_data_ex)

x = ex_df[["2019 noda", "2019 tdc", "2019 tdg", "2019 eda", "2019 type"]]
y = ex_df["2020 tdc"]

ex_model = LinearRegression()
ex_model.fit(x, y)

print("Coefficients:")
for name, coef in zip(x.columns, ex_model.coef_):
    print(f"  {name}: {coef:.3f}")

print("\nIntercept:", round(ex_model.intercept_, 3))
print("R² score:", round(ex_model.score(x, y), 4))


def predict_custom(noda_19, tdc_19, tdg_19, eda_19, type_19):
    input_df = pd.DataFrame([{
        "2019 noda": noda_19,
        "2019 tdc": tdc_19,
        "2019 tdg": tdg_19,
        "2019 eda": eda_19,
        "2019 type": type_19
    }])

    prediction = ex_model.predict(input_df)[0]
    return prediction

# Example usage:
example_prediction = predict_custom(200, 10000000, 9000000, 50000000, 0)
print("Example prediction for input:", round(example_prediction, 2))

# %%
