import base64
import requests
import pandas as pd
from math import ceil

class ReposData:

    def __init__(self, owner, username):
        self.owner = owner
        self.username = username
        self.base_url = 'https://api.github.com'
        self.token = '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'
        self.headers = {'Authorization': 'Bearer ' + self.token,
           "Content-Type": "application/json",
           'X-GitHub-Api-Version': '2022-11-28'}

    def __repos_list(self):
        repos_list = []
        pages = requests.get(f'{self.base_url}/users/{self.owner}')
        num_pages = ceil(pages.json()['public_repos']/30)+1

        for page_num in range(1,num_pages):
            try:
                url_page = f'{self.base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)
        
        return repos_list
    
    def __repos_names(self, repos_list):
        repos_names = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_names.append(repo['name'])
                except:
                    pass

        return repos_names
    
    def __repos_langs(self, repos_list):
        repos_langs = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_langs.append(repo['language'])
                except:
                    pass

        return repos_langs
    
    def lang_table(self):
        repos_list = self.__repos_list()
        repos_names = self.__repos_names(repos_list)
        repos_lang = self.__repos_langs(repos_list)

        df = pd.DataFrame({
                'Repository_Name': repos_names,
                'Repository_Language': repos_lang
                })
        
        return df
    
    def add_arquivo(self, file_name, file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        url = f'{self.base_url}/repos/{self.username}/linguagens-utilizadas/contents/{file_name}'
        data = {'message': 'Criando um arquivo',
            'content': encoded_content.decode('utf-8')}

        response = requests.put(url, json=data, headers=self.headers)
        return response.status_code