import DadosRepos as DadosRepositorios
import ManipulaRepos as ManipulaRepositorios

amazon_rep = DadosRepositorios(owner='amzn')
ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

netflix_rep = DadosRepositorios(owner='netflix')
ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

spotify_rep = DadosRepositorios(owner='spotify')
ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

# Salvando os dados
ling_mais_usadas_amzn.to_csv('processed_data/linguagens_amzn.csv')
ling_mais_usadas_netflix.to_csv('processed_data/linguagens_netflix.csv')
ling_mais_usadas_spotify.to_csv('processed_data/linguagens_spotify.csv')

# instanciando um objeto
novo_repo = ManipulaRepositorios('LucianBell')

# Nome do repositório
nome_repo = 'programming-languages-analysis'

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'processed_data/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'processed_data/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'processed_data/linguagens_spotify.csv')