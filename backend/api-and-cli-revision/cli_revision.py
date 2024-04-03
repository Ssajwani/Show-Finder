from api_revision import *


def main():
    choice = ""

    while choice != "q":
        print("\nWelcome to the anime central hub!")
        print("Please select from the following options:")
        print("(a) : Find one or more anime by inputting a genre")
        print("(b) : Find one or more anime by inputting an average user rating score")
        print("(c) : Find one or more anime by inputting a number of episodes")
        print("(d) : Find the genre(s) of a specific anime title")
        print("(e) : Find the average user rating score of a specific anime title") 
        print("(f) : Find the number of episodes of a specific anime title")
        print("(g) : Find the synopsis of a specific anime title")
        print("(q) : Quit this program")
        print("")
        choice = input("Make your selection: ")

        if choice not in ["a", "b", "c", "d", "e", "f", "g", "q"]:
            print("Input a valid option.")

        if choice == "a":
            genre_input = input(str("Enter a genre of an anime you're looking for: "))
            anime_from_genre = getTitleofAnimefromGenre(genre_input)
            print("\nThe anime you might be looking for with the given genre, " + str(genre_input) + ", is " + str(anime_from_genre) + ".")

        elif choice == "b":
            score_input = input("Enter an average user rating score of an anime you're looking for: ")
            anime_from_score = getTitleofAnimefromScore(score_input)
            print("\nThe anime you might be looking for with the given score, " + str(score_input) + ", is " + str(anime_from_score) + ".")

        elif choice == "c":
           num_of_episodes_input = input("Enter the number of episodes for an anime you're looking for: ")
           anime_from_num = getTitleofAnimefromNumberOfepisodes(num_of_episodes_input)
           print("\nThe anime you might be looking for with the given number of episodes, " + str(num_of_episodes_input) + ", is " + str(anime_from_num) + ".")

        elif choice == "d":
            anime_input = input("Enter the title of an anime for which you want the genres: ")
            genre_from_anime = getGenre(anime_input)
            print("\nThe anime, " + anime_input + ", if of the following genre: " + str(genre_from_anime) + ".")

        elif choice == "e":
            anime_input = input("Enter the title of an anime for which you want the average user rating score: ")
            score_from_anime = getScoreofAnime(anime_input)
            print("\nThe anime, " + anime_input + ", has an average user rating score of " + str(score_from_anime) + ".")

        elif choice == "f":
            anime_input = input("Enter title of anime for which you want the number of episodes: ")
            numOfeps_from_anime = getNumberofEpisodes(anime_input)
            print("The anime, " + anime_input + ", has " + str(numOfeps_from_anime) + " episodes.")

        elif choice == "g":
            anime_input = input("Enter title of anime for which you want the synopsis: ")
            synopsis_from_anime = getSynopsis(anime_input)
            print("\nThe anime, " + anime_input + "'s synopsis that you requested is as follow: ")
            print("'" + str(synopsis_from_anime) + "'")


    print("Thank you -- I hope you learned something about animes today!")

if __name__ == "__main__":
    main()