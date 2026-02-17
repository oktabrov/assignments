import requests
OMDB_API_KEY = "719fe65e"
TMDB_API_KEY = "f20a5695babfbd95db1c195cbe9f7e2a"
BASE_URL_OMDB = "http://www.omdbapi.com/"
# Returns the list of IDs of best-match movies. Takes them from OMDB
def get_the_list(movie_name):
    params = {"apikey": OMDB_API_KEY, "s": movie_name}
    response = requests.get(BASE_URL_OMDB, params=params).json()
    if response['Response'] == 'False':
        raise ValueError("API response is empty")
    list_of_top_movies_found = []
    for list_of_results in response['Search']:
        list_of_top_movies_found.append(list_of_results['imdbID'])
    return list_of_top_movies_found
# Returns the given raw, oneline string as a formatted and cut one. This gives a userfriendly text for the report.lua file
def format_long_text(raw, tagline = False):
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
# Gets full information about the movie by the movie ID. If not available, returns False. Uses the data of TMDB
def get_info_of_the_movie(tmdb_movie_id):
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
    list_of_chars_of_genres = []
    for dict_of_genres in data['genres']:
        list_of_chars_of_genres.append(dict_of_genres['name'])
    genres = '• ' + '\n• '.join(list_of_chars_of_genres)
    raw_overview = data['overview']
    overview = format_long_text(raw_overview)
    list_of_chars_of_production_companies = []
    for dict_of_companies in data['production_companies']:
        list_of_chars_of_production_companies.append(dict_of_companies['name'])
    production_companies = '• ' + '\n• '.join(list_of_chars_of_production_companies)
    list_of_chars_of_production_countries = []
    for dict_of_countries in data['production_countries']:
        list_of_chars_of_production_countries.append(dict_of_countries['name'])
    production_countries = '• ' + '\n• '.join(list_of_chars_of_production_countries)
    original_language = data['original_language']
    list_of_chars_of_spoken_langues = []
    for dict_of_spoken_languages in data['spoken_languages']:
        list_of_chars_of_spoken_langues.append(dict_of_spoken_languages['english_name'])
    spoken_languages = '• ' + '\n• '.join(list_of_chars_of_spoken_langues) 
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
# Writes user-friendly text to the file report.lua
def write_to_lua(list_of_info):
    with open('report.txt', 'w', encoding="utf-8") as file:
        text = f'============================================================\n🎬 MOVIE PROFILE\n============================================================\n\nTitle: {list_of_info[0]}\nOriginal Title: {list_of_info[1]}\n{f'Tagline: {list_of_info[2] if list_of_info[2] else 'Not available'}\n'}\nRelease Date: {list_of_info[3]}\nRuntime: {list_of_info[4]} minutes\nStatus: {list_of_info[5]}\n\n------------------------------------------------------------\n📊 RATINGS & POPULARITY\n------------------------------------------------------------\nIMDb ID: {list_of_info[6]}\nAverage Rating: {list_of_info[7]} / 10\nTotal Votes: {list_of_info[8]}\nPopularity Score: {list_of_info[9]}\n\n{f"------------------------------------------------------------\n🎭 GENRES\n------------------------------------------------------------\n{list_of_info[10]}\n\n" if list_of_info[10].strip('• ') else ''}------------------------------------------------------------\n🧠 STORY OVERVIEW\n------------------------------------------------------------\n{list_of_info[11]}\n\n------------------------------------------------------------\n🌍 PRODUCTION DETAILS\n------------------------------------------------------------\n{f'Production Companies:\n{list_of_info[12]}\n\n' if list_of_info[12] else ''}Production Countries:\n{list_of_info[13]}\n\nOriginal Language: {list_of_info[14]}\nSpoken Languages:\n{list_of_info[15]}\n\n------------------------------------------------------------\n💰 FINANCIAL PERFORMANCE\n------------------------------------------------------------\nBudget: ${list_of_info[16]}\nRevenue: ${list_of_info[17]}\n\n------------------------------------------------------------\n🔗 OFFICIAL LINKS\n------------------------------------------------------------\nHomepage:\n{list_of_info[18] if list_of_info[18] else "Not available"}\n\nPoster Path:\n{list_of_info[19]}\n\nBackdrop Path:\n{list_of_info[20]}\n\n------------------------------------------------------------\n🗂 METADATA\n------------------------------------------------------------\nTMDB ID: {list_of_info[21]}\nOrigin Countries: {' '.join(list_of_info[22])}\n\n============================================================\n© Data provided by TMDB\n============================================================'
        file.write(text)
# Calls other functions to get or do some tasks in order to find the movie user inserted. If there is no such movie or error occurs, the functions gently handles them
def main():
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
        return "All information successfully saved to report.txt ✅"
    except Exception as error:
        return f"Error: {error}"
print(main())