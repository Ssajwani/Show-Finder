from api import *
import os


def main():
    choice = ""
    
    animeAPI = AnimeAPI("animes.csv")

    while choice != "q":
        print("\nWelcome to the anime central hub!")
        print("Please select from the following options:")
        print("(a) : Find one or more animes based on a given genre")
        print("(b) : Find one or more animes based on a given average score")
        print("(c) : Find one or more animes based on a given number of episodes")
        print("(d) : Find the genre of a specific anime")
        print("(e) : Find the average user rating score of a specific anime")
        print("(f) : Find the number of episodes of a specific anime")
        print("(g) : Find the synopsis of a specific anime")
        print("(q) : Quit this program")
        print("")
        choice = input("Make your selection: ")

        if choice not in ["a", "b", "c", "d", "e","f","g","q"]:
            print("Input a valid option.")
            
        if choice == "a":
            genre = input(str("Enter a genre of an anime you're looking for: "))
            expectedInput = genre.title()
            anime = animeAPI.getTitleofAnimefromGenre(expectedInput)
            if not anime:
                print("\nNo anime found with the given genre.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

        elif choice == "b":
            score = input("Enter a score of an anime you're looking for: ")
            score2 = str(float(score))
            anime = animeAPI.getTitleofAnimefromScore(score2)

            if not anime:
                print("\nThere is no anime found with this given score.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

        elif choice == "c":
            episodes = input("Enter the number of episodes for an anime you're looking for: ")
            episodes2 = str(int(episodes))
            anime = animeAPI.getTitleofAnimefromNumberOfepisodes(episodes2)
        
            if not anime:
                print("\nThere is no anime found with this given amount of episodes.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

        elif choice == "d":
            anime = input("Enter title of anime: ")
            expectedInput = anime.title()            

            genre = animeAPI.getGenre(expectedInput).strip('[]')

            if genre is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("\nThe anime is of the following genre: " + genre.strip(''))

        elif choice == "e":
            anime = input("Enter title of anime: ")
            expectedInput = anime.title()            

            score = animeAPI.getScoreofAnime(expectedInput)

            if score is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("\nThe anime, " + anime + ", gets an average user rating score of " + str(score) + ".")

        elif choice == "f":
            anime = str(input("Enter title of anime: "))
            expectedInput = anime.title()            
            numOfEpisodes = animeAPI.getNumberofEpisodes(expectedInput)

            if numOfEpisodes is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("The anime, " + anime + ", has " + str(numOfEpisodes) + " episodes.")

        elif choice == "g":
            anime = input(str("Enter title of anime: "))
            # listofwords = anime.split()
            # for words in listofwords:
            #     if len(words) > 2:
            #         words = listofwords.capitalize()
            expectedInput = anime.title()            
            synopsis = animeAPI.getSynopsis(expectedInput)
            if synopsis is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("\nThe anime, " + anime + "'s synopsis that you requested is as follow: ")
                print("'" + str(synopsis) + "'")
        
        elif choice == "q":
            print("Thank you -- I hope you learned something new about animes today!")

  
if __name__ == "__main__":
    main()