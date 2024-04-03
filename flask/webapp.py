import flask
from flask import render_template, request
import json
import sys
from api import AnimeAPI

app = flask.Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/home/')
def homepage():
    return render_template('index.html')

@app.route('/about/')
def aboutpage():
    return render_template('about.html')
 
@app.route('/data/')
def datapage():
    return render_template('datapage.html')

@app.route('/AnimefromGenre', methods=['GET', 'POST'])
def search_from_genre():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:
        genre_for_anime = ''
        anime_from_genre = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            genre_for_anime = request.form['AnimefromGenre']
            animeTitles = animeAPI.getTitleofAnimefromGenre(genre_for_anime)
            if not animeTitles:
                raise ValueError ("Invalid Query")
            anime_from_genre = ', '.join(animeTitles)
            return render_template('results.html', genre_for_anime=genre_for_anime, anime_from_genre=anime_from_genre)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')

@app.route('/AnimefromNumEps', methods=['GET', 'POST'])
def search_from_num_of_eps():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:
        num_eps_for_anime = ''
        anime_from_num_eps = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            num_eps_for_anime = request.form['AnimefromNumEps']
            animeTitles = animeAPI.getTitleofAnimefromNumberOfepisodes(num_eps_for_anime)
            if not animeTitles:
                raise ValueError ("Invalid Query")
            anime_from_num_eps = ', '.join(animeTitles)
            return render_template('results.html', num_eps_for_anime=num_eps_for_anime, anime_from_num_eps=anime_from_num_eps)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')


@app.route('/AnimefromScore', methods=['GET', 'POST'])
def search_from_score():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:

        score_for_anime = ''
        anime_from_score = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            score_for_anime = request.form['AnimefromScore']
            animeTitles = animeAPI.getTitleofAnimefromScore(score_for_anime)
            if not animeTitles:
                raise ValueError ("invalid query")
            anime_from_score = ', '.join(animeTitles)
            return render_template('results.html', score_for_anime=score_for_anime, anime_from_score=anime_from_score)
        else:
            raise ValueError ("Invalid Query")
    except ValueError:
        return render_template('error.html')


@app.route('/AnimefromNumEpsRange', methods=['GET', 'POST'])
def search_from_num_of_eps_range():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:
        num_of_eps_range_for_anime = ''
        anime_from_num_of_eps_range = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            num_of_eps_range_for_anime = request.form['AnimefromNumEpsRange']
            animeTitles = animeAPI.getTitleofAnimefromNumberOfepisodesRange(num_of_eps_range_for_anime)
            if not animeTitles:
                raise ValueError ("Invalid Query")
            anime_from_num_of_eps_range = ', '.join(animeTitles)
        return render_template('results.html', num_of_eps_range_for_anime=num_of_eps_range_for_anime, anime_from_num_of_eps_range=anime_from_num_of_eps_range)
    except ValueError:
        return render_template('error.html')


@app.route('/AnimefromScoreRange', methods=['GET', 'POST'])
def search_from_score_range():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:
        range_of_score_for_anime = ''
        anime_from_score_range = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            range_of_score_for_anime = request.form['AnimefromScoreRange']
            animeTitles = animeAPI.getTitleofAnimefromScoreRange(range_of_score_for_anime)
            if not animeTitles:
                raise ValueError ("invalid Query")
            anime_from_score_range = ', '.join(animeTitles)
            return render_template('results.html', range_of_score_for_anime=range_of_score_for_anime, anime_from_score_range=anime_from_score_range)
        else:
            raise ValueError ("Invalid Query")
    except ValueError:
        return render_template('error.html')



@app.route('/ScorefromAnime', methods=['GET', 'POST'])
def search_for_score():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:

        title_for_score = ''
        score_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_score = request.form['ScorefromAnime']
            scoreS = animeAPI.getScoreofAnime(title_for_score)
            if not scoreS:
                raise ValueError("Invalid query")
            score_from_title = scoreS[0]
            return render_template('results.html', title_for_score=title_for_score, score_from_title=score_from_title)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')

@app.route('/NumEpsfromAnime', methods=['GET', 'POST'])
def search_for_num_of_eps():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:

        title_for_numEps = ''
        numEps_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_numEps = request.form['NumEpsfromAnime']
            numOfEpisodesS = animeAPI.getNumberofEpisodes(title_for_numEps)
            if not numOfEpisodesS:
                raise ValueError("Invalid query")
            numEps_from_title = numOfEpisodesS[0]
            return render_template('results.html', title_for_numEps=title_for_numEps, numEps_from_title=numEps_from_title)
        else:
            raise ValueError("Invalid query")
    except ValueError:
        return render_template('error.html')

@app.route('/SynopsisfromAnime', methods=['GET', 'POST'])
def search_for_synopsis():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:
        title_for_synopsis = ''
        synopsis_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_synopsis = request.form['SynopsisfromAnime']
            synopsisS = animeAPI.getSynopsis(title_for_synopsis)
            if not synopsisS:
                raise ValueError("Invalid query")
            synopsis_from_title = synopsisS[0]
            return render_template('results.html', title_for_synopsis=title_for_synopsis, synopsis_from_title=synopsis_from_title)
        else:
            raise ValueError("Invalid query")
    except ValueError:
        return render_template('error.html')

        
@app.route('/GenresfromAnime', methods=['GET', 'POST'])
def search_for_genre():
    '''
    This method is executed once you submit the simple form. It embeds the form responses
    into a web page.
    '''
    try:

        title_for_genre = ''
        genre_from_title = ''
        if request.method == 'POST':
            animeAPI = AnimeAPI()
            title_for_genre = request.form['GenresfromAnime']
            genreS = animeAPI.getGenre(title_for_genre)
            if not genreS:
                raise ValueError("Invalid Query")
            genre_from_title = genreS[0]
            return render_template('results.html', title_for_genre=title_for_genre, genre_from_title=genre_from_title)
        else:
            raise ValueError("Invalid Query")
    except ValueError:
        return render_template('error.html')

'''
Run the program by typing 'python3 localhost [port]', where [port] is one of 
the port numbers you were sent by Amy earlier during Winter term.
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port, debug = True)

