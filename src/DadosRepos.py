import requests
import pandas as pd
from math import ceil

class DadosRepositorios:
    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    # Método que vai representar a páginação para EXTRAÇÃO de dados não tratados
    def lista_repositorios(self):
        repos_list = []

        pages_endpoint = f'{self.api_base_url}/users/{self.owner}'
        general_response = requests.get(url=pages_endpoint, headers=self.headers)
        max_pages = ceil(general_response.json()['public_repos']/30)

        for page_num in range(1, (max_pages + 1)):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url=url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list
    
    def nomes_repos(self, lista_repositorios):
        repos_names = []
        try:
            for page in lista_repositorios:
                for repo in page:
                    repos_names.append(repo['name'])        
        except:
            print("Ops! Something went wrong...")
                
        return repos_names

    def linguagens_repos(self, lista_repositorios):
        repos_lings = []
        try:
            for page in lista_repositorios:
                for repo in page:
                    repos_lings.append(repo['language'])        
        except:
            print("Ops! Something went wrong...")

        return repos_lings
    
    def cria_df_linguagens(self):

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(lista_repositorios=repositorios)
        linguagens = self.linguagens_repos(lista_repositorios=repositorios)

        dados_finais = pd.DataFrame()
        dados_finais['repository_name'] = nomes
        dados_finais['programming_language'] = linguagens

        return dados_finais
        