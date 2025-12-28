import requests
OMDB_API_KEY = "719fe65e"
TMDB_API_KEY = "f20a5695babfbd95db1c195cbe9f7e2a"
BASE_URL_OMDB = "http://www.omdbapi.com/"
def get_the_list(movie_name):
    '''Rturns the list of IDs of best-match movies. Takes them from OMDB'''
    params = {"apikey": OMDB_API_KEY, "s": movie_name}
    response = requests.get(BASE_URL_OMDB, params=params).json()
    if response['Response'] == 'False':
        raise ValueError("API response is empty")
    list_of_top_movies_found = []
    for list_of_results in response['Search']:
        list_of_top_movies_found.append(list_of_results['imdbID'])
    return list_of_top_movies_found
def format_long_text(raw, tagline = False):
    '''Returns the given raw, oneline string as a formatted and cut one. This gives a userfriendly text for the report.lua file'''
    words = raw.split()
    max_len = 60
    formatted_string = ''
    j = 0; len_tagline = 9 if tagline else 0
    for i in range(len(words)):
        if len(' '.join(words[j:i])) + len_tagline >= max_len:
            len_tagline = 0
            is_equal = len(' '.join(words[j:i])) == max_len
            formatted_string += ' '.join(words[j:i-(0 if is_equal else 1)]) + '\n'
            j = i - (0 if is_equal else 1)
        else:
            if i == len(words) - 1:
                formatted_string += ' '.join(words[j:])
    return formatted_string.strip()
def get_info_of_the_movie(tmdb_movie_id):
    '''Gets full information about the movie by the movie ID. If not available, returns False. Uses the data of TMDB'''
    BASE_URL_TMDB = f"https://api.themoviedb.org/3/movie/{tmdb_movie_id}"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(BASE_URL_TMDB, params=params)
    if response.status_code != 200:
        return False
    data = response.json()
    title = data['title']
    originial_title = data['original_title']
    raw_tagline = data['tagline']
    tagline = format_long_text(raw_tagline, True)
    release_date = data['release_date']
    runtime = data['runtime']
    status = data['status']
    imdb_id = data['imdb_id']
    vote_average = data['vote_average']
    vote_count = data['vote_count']
    popularity = data['popularity']
    genres = '• ' + '\n• '.join([dict_of_genres['name'] for dict_of_genres in data['genres']])
    raw_overview = data['overview']
    overview = format_long_text(raw_overview)
    production_companies = '• ' + '\n• '.join([dict_of_companies['name'] for dict_of_companies in data['production_companies']])
    production_countries = '• ' + '\n• '.join([dict_of_countries['name'] for dict_of_countries in data['production_countries']])
    original_language = data['original_language']
    spoken_languages = '• ' + '\n• '.join([dict_of_spoken_languages['english_name'] for dict_of_spoken_languages in data['spoken_languages']]) 
    budget = data['budget']
    revenue = data['revenue']
    homepage = data['homepage']
    poster_path = data['poster_path']
    backdrop_path = data['backdrop_path']
    tmdb_id = data['id']
    origin_country = data['origin_country']
    return [title, originial_title, tagline, release_date, runtime, status, imdb_id, vote_average, vote_count, popularity, genres, overview,
            production_companies, production_countries, original_language, spoken_languages, budget, revenue, homepage, poster_path, backdrop_path,
            tmdb_id, origin_country]
def write_to_lua(list_of_info):
    '''Writes user-friendly text to the file report.lua'''
    with open('report.lua', 'w', encoding="utf-8") as file:
        text = f'''============================================================
🎬 MOVIE PROFILE
============================================================

Title: {list_of_info[0]}
Original Title: {list_of_info[1]}
{f'Tagline: {list_of_info[2] if list_of_info[2] else 'Not available'}\n'}
Release Date: {list_of_info[3]}
Runtime: {list_of_info[4]} minutes
Status: {list_of_info[5]}

------------------------------------------------------------
📊 RATINGS & POPULARITY
------------------------------------------------------------
IMDb ID: {list_of_info[6]}
Average Rating: {list_of_info[7]} / 10
Total Votes: {list_of_info[8]}
Popularity Score: {list_of_info[9]}

{f"""------------------------------------------------------------
🎭 GENRES
------------------------------------------------------------
{list_of_info[10]}

""" if list_of_info[10].strip('• ') else ''}------------------------------------------------------------
🧠 STORY OVERVIEW
------------------------------------------------------------
{list_of_info[11]}

------------------------------------------------------------
🌍 PRODUCTION DETAILS
------------------------------------------------------------
{f'''Production Companies:
{list_of_info[12]}

''' if list_of_info[12] else ''}Production Countries:
{list_of_info[13]}

Original Language: {list_of_info[14]}
Spoken Languages:
{list_of_info[15]}

------------------------------------------------------------
💰 FINANCIAL PERFORMANCE
------------------------------------------------------------
Budget: ${list_of_info[16]}
Revenue: ${list_of_info[17]}

------------------------------------------------------------
🔗 OFFICIAL LINKS
------------------------------------------------------------
Homepage:
{list_of_info[18] if list_of_info[18] else "Not available"}

Poster Path:
{list_of_info[19]}

Backdrop Path:
{list_of_info[20]}

------------------------------------------------------------
🗂 METADATA
------------------------------------------------------------
TMDB ID: {list_of_info[21]}
Origin Countries: {' '.join(list_of_info[22])}

============================================================
© Data provided by TMDB
============================================================'''
        file.write(text)
def main():
    '''Calls other functions to get or do some tasks in order to find the movie user inserted. If there is no such movie or error occurs, the functions gently handles them'''
    movie_name = input("Please enter the movie name: ")
    try:
        print("Searching for the best matches...")
        list_of_movie_ids = get_the_list(movie_name)
    except Exception as error:
        if error.args[0] == 'API response is empty':
            return "No movies found ☹️"
        return f"Error: {error}"
    try:
        print('Getting full information about the best-match result')
        for ID in list_of_movie_ids:
            list_of_info = get_info_of_the_movie(ID)
            if list_of_info:
                break
    except Exception as error:
        return f'Error: {error}'
    try:
        write_to_lua(list_of_info)
        return "All information successfully saved to report.lua ✅"
    except Exception as error:
        return f"Error: {error}"
print(main())