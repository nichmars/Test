# Test
# %%
import pandas as pd

j_df = pd.read_excel('../../../Downloads/Annual+DAF+Report+2025+Dataset.xlsx', sheet_name='data')


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

# j_df_conf
# %%

filter_df19 = j_df_conf.loc[(j_df_conf["fiscal_year_end"] == 2019)]
filter_df20 = j_df_conf.loc[(j_df_conf["fiscal_year_end"] == 2020)]
filter_df21 = j_df_conf.loc[(j_df_conf["fiscal_year_end"] == 2021)]
filter_df22 = j_df_conf.loc[(j_df_conf["fiscal_year_end"] == 2022)]
filter_df23 = j_df_conf.loc[(j_df_conf["fiscal_year_end"] == 2023)]
filter_df24 = j_df_conf.loc[(j_df_conf["fiscal_year_end"] == 2024)]
print(filter_df19)
# %%
