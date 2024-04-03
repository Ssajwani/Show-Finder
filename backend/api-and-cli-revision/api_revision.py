'''
The user will be limited to entering information by the title of the anime.
The reason for this is because it will prevent issues in the display of anime
that have similar information. In other words, searching for information by means
other than the title of the anime will cause too much ambiguity. Additionally,
anime are more known by their title in comparison to their series number or other
information that is presented within the dataset. 
'''

def getTitleofAnimefromGenre(genre_of_anime):

    '''
    Returns a specific anime title’s name based on the genre entered by the user
    PARAMETER:
    genre_of_anime - the category of the anime (action, adventure, comedy, drama, fantasy, romance, etc. )
    '''
    
    return "Death Note"    
    
def getTitleofAnimefromNumberOfepisodes(num_of_episodes):
    
    '''
    Returns a specific anime title’s name
    PARAMETER:
    num_of_episodes - the number of episodes that a user is looking for within an anime
    '''   

    return "Attack on Titan"

def getTitleofAnimefromScore(score_of_anime):
     
    '''
    Returns a specific anime title’s name
    PARAMETER:
    score_of_anime - the average user rating score for anime, on a scale from 0.0 to 10.0.
    '''
    
    return "Tokyo Mew Mew New"

    
def getSynopsis(title):

    '''
    Returns an anime's synopsis
    PARAMETER:
    title - the name of the anime of interest
    '''
    
    return "A shinigami, as a god of death, can kill any person—provided they see their victim's face and write their victim's name in a notebook called a Death Note. One day, Ryuk, bored by the shinigami lifestyle and interested in seeing how a human would use a Death Note, drops one into the human realm. High school student and prodigy Light Yagami stumbles upon the Death Note and—since he deplores the state of the world—tests the deadly notebook by writing a criminal's name in it. When the criminal dies immediately following his experiment with the Death Note, Light is greatly surprised and quickly recognizes how devastating the power that has fallen into his hands could be. With this divine capability, Light decides to extinguish all criminals in order to build a new world where crime does not exist and people worship him as a god. Police, however, quickly discover that a serial killer is targeting criminals and, consequently, try to apprehend the culprit. To do this, the Japanese investigators count on the assistance of the best detective in the world: a young and eccentric man known only by the name of L. "

def getGenre(title):

    '''
    Returns an anime's genre
    PARAMETER:
    title - the name of the anime of interest
    '''

    return "Drama, Romance"

def getScoreofAnime(title):

    '''
    Returns an anime's average user rating score for anime, on a scale from 0.0 to 10.0
    PARAMETER:
    title - the name of the anime of interest
    '''

    return 6.5

def getNumberofEpisodes(title):

    '''
    Returns an anime's number of episodes
    PARAMETER:
    title - the name of the anime of interest
    '''

    return 12