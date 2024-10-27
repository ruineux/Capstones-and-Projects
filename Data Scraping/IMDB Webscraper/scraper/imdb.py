import requests
from bs4 import BeautifulSoup
import pandas as pd

from functools import reduce

def get_primary_info(tags):

    year = [int(v.text.split()[-1][1:-1]) for v in tags]
    title = [" ".join(v.text.split()[1:-1]) for v in tags]
    number = [int(v.text.split()[0][:-1]) for v in tags]

    return pd.DataFrame({"Rank": number,
                        "Title": title,
                        "Year": year,
                        })


def get_actor_director_info(tags):
    
    dataframe = pd.DataFrame([v.get("title").split(",")[1:] for v in tags],
                             columns=["Lead Actor", "Supporting Actor"])
    
    dataframe["Director"] = [" ".join(v.get("title").split(",")[0].split()[:-1]) for v in tags]
    
    return dataframe


def get_rating_info(tags):
    
    rating = [float(v.get("title").split()[0]) for v in tags]
    votes = [int(v.get("title").split()[3].replace(",","")) for v in tags]
    
    return pd.DataFrame({"Rating": rating,
                        "Votes": votes,
                        })

def get_top_imdb_movies(URL):

    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')
    
    movietags = soup.select('td.titleColumn')
    
    other_movietags = soup.select('td.titleColumn a')
    
    rating_movietags = soup.find_all("td", {"class": "ratingColumn imdbRating"})
    rating_movietags = [movie.find("strong") for movie in rating_movietags]
    
    FIRST_DF = get_primary_info(movietags)
    SECOND_DF = get_actor_director_info(other_movietags)
    THIRD_DF = get_rating_info(rating_movietags)
    
    DFS = [FIRST_DF, SECOND_DF, THIRD_DF]
    
    return reduce(lambda left,right: pd.merge(left, right, left_index=True, right_index=True), DFS)