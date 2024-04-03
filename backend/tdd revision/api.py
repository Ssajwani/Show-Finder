import csv
'''
The user will be limited to entering information by the title of the anime.
The reason for this is because it will prevent issues in the display of anime
that have similar information. In other words, searching for information by means
other than the title of the anime will cause too much ambiguity. Additionally,
anime are more known by their title in comparison to their series number or other
information that is presented within the dataset. 
'''
class AnimeAPI:


    def __init__(self, filename):
        '''
        Reads in and stores the data from the specified file as a list of dictionaries, for use by the rest of the functions in the class.
        PARAMETER
        filename - the name (and path, if not in the current working directory) of the data file
        '''
        with open('animes.csv', newline='') as animefile:
            self.animes = list(csv.DictReader(animefile))
    
    def getTitleofAnimefromGenre(self, genre):
        genre = genre.title()
        animeTitles = []

        for eachTitle in self.animes: 
            if eachTitle['genre'] == genre: 
                requestedTitle = str(eachTitle['title'])
                animeTitles.append(requestedTitle)
        return animeTitles

    def getTitleofAnimefromNumberOfepisodes(self, num_episodes):

        animeTitlesByNumOfEpisodes = []

        for eachTitle in self.animes: 
            if eachTitle['episodes'] == num_episodes:
                requestedTitle = str(eachTitle['title'])
                animeTitlesByNumOfEpisodes.append(requestedTitle)
        return animeTitlesByNumOfEpisodes

    def getTitleofAnimefromScore(self, score):
     
        animeTitlesByScore = []

        for eachTitle in self.animes: 
            if eachTitle['score'] == score:
                requestedTitle = str(eachTitle['title'])
                animeTitlesByScore.append(requestedTitle)
        return animeTitlesByScore
    
    def getSynopsis(self, title):

        synopsis = None

        for eachSynopsis in self.animes:
            if eachSynopsis['title'] == title: 
                synopsis = eachSynopsis['synopsis'] 
                break
            else:
                synopsis = None
        return synopsis

    def getGenre(self, title):

        genre = None

        for eachGenre in self.animes:
            if eachGenre['title'] == title:
                genre = eachGenre['genre']
                break
            else:
                genre = None
        return genre

    def getScoreofAnime(self, title):

        score = None

        for eachScore in self.animes:
            if eachScore['title'] == title:
                score = float(eachScore['score'])
                break
            else:
                score = None
        return score

    def getNumberofEpisodes(self, title):

        numOfepisodes = None

        for eachNumber in self.animes:
            if eachNumber['title'] == title:
                numOfepisodes = int(float(eachNumber['episodes']))
                break
            else:
                numOfepisodes = None
        return numOfepisodes