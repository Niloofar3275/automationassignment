import pandas as pd
import numpy as np



def get_top_5():
    # Reading the raw scraped data (a long list of movies and their cast members) as a pandas Dataframe
    movies = pd.read_json('movies.json')

    # Let's see how many cast member
    all_cast_count = sum(len(cast) for cast in movies.Cast)
    all_cast = pd.DataFrame(np.empty(all_cast_count, dtype=str), columns=['Name'])

    i = 0
    for cast_list in movies.Cast:
        for cast_member in cast_list:
            all_cast.loc[i]['Name'] = cast_member
            i += 1

    top_5_final = all_cast['Name'].value_counts()[:5].index.tolist()
    return top_5_final
