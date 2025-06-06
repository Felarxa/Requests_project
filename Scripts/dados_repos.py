from repos_class import ReposData

companys = ['amzn', 'netflix', 'spotify', 'apple']

for company in companys:
    var = company + '_lang_df'
    data = ReposData(company, 'Felarxa')
    vars()[var] = data.lang_table()
    vars()[var].to_csv(f'Data/dados_{company}')
    print(f'Status_code do arquivo dados_{company}: ', str(data.add_arquivo(f'dados_{company}.csv', f'Data/dados_{company}')))

