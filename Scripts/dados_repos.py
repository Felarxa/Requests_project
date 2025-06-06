from repos_class import ReposData
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
companys = ['amzn', 'netflix', 'spotify', 'apple']

for company in companys:
    var = company + '_lang_df'
    data = ReposData(company, 'Felarxa', token)
    vars()[var] = data.lang_table()
    vars()[var].to_csv(f'Data/dados_{company}')
    print(f'Status_code do arquivo dados_{company}: ', str(data.add_arquivo(f'dados_{company}.csv', f'Data/dados_{company}')))

