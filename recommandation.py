
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

# Chargement et preprocessing
df = pd.read_csv("data/DF_FILMS_TMDB.csv")

df_trie = df[['original_country', 'title', 'release_date', 'genres', 'averageRating', 'numVotes']]

dummies = df_trie['genres'].str.get_dummies(',')

def categoriser(x):
    pays = str(x)
    if 'FR' in pays: return 'FR'
    elif 'JP' in pays: return 'JP'
    elif 'US' in pays: return 'US'

df_concat = pd.concat([df_trie, dummies], axis=1)
df_concat['pays_categorie'] = df_concat['original_country'].apply(categoriser)
df_concat['pays_categorie'] = df_concat['pays_categorie'].map({"US": 0, "FR": 1, "JP": 2})

df_encode = df_concat.copy()
df_encode['année_sortie'] = pd.to_datetime(df_encode['release_date']).dt.year
df_encode['mois_sortie'] = pd.to_datetime(df_encode['release_date']).dt.month

scaler = MinMaxScaler()
cols_scaler = ['averageRating', 'numVotes', 'année_sortie', 'mois_sortie']
df_encode[cols_scaler] = scaler.fit_transform(df_encode[cols_scaler])

X = df_encode.drop(columns=['original_country', 'title', 'release_date', 'genres'])

model = NearestNeighbors(n_neighbors=6)
model.fit(X)

distance, indices = model.kneighbors(X)

def film_reco(film: str):
    info_film = df_encode[df_encode['title'] == film]
    indice_film = info_film.index[0]
    reco_indices = indices[indice_film][1:]
    df_reco = df_encode.iloc[reco_indices, :4]
    return df_reco