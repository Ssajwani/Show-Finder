import unittest

import api
api1 = api.AnimeAPI("../unitled folder/animes.csv")

class APITester (unittest.TestCase):
    
    def test_valid_genre(self):
        # This unit test tests for a genre that is within the database and checks to see if these animes are within the returned set. It tests the input as having the first letter capitalized
        result = api1.getTitleofAnimefromGenre("Romance")
        self.assertEqual(result, ["Amagami SS+ Plus Specials", "Koitabi: True Tours Nanto", "To Heart 2 AD Plus", "Ushinawareta Mirai wo Motomete: Ushinawareta Natsuyasumi wo Motomete", "Koikishi Purely☆Kiss The Animation: Special Edition", "True Love Story", "Choujuu Giga", "Sekishoku Elegy","Suki Desu Suzuki-kun!!", "Monogatari no Aru Satou", "Nemuranu Machi no Cinderella: Hirose Ryouichi - Memorial Date", "Steady x Study", "Kagami","Ai (ONA)", "Wedding Park"])


    def test_valid_genre_case_insensitivity_lowercase(self):
        # This unit test tests for a genre that is within the database with case sensitive strings such as the first letter not being capitalize and checks to see if these animes are within the returned set
        result = api1.getTitleofAnimefromGenre("romance")
        self.assertEqual(result, ["Amagami SS+ Plus Specials", "Koitabi: True Tours Nanto", "To Heart 2 AD Plus", "Ushinawareta Mirai wo Motomete: Ushinawareta Natsuyasumi wo Motomete", "Koikishi Purely☆Kiss The Animation: Special Edition", "True Love Story", "Choujuu Giga", "Sekishoku Elegy","Suki Desu Suzuki-kun!!", "Monogatari no Aru Satou", "Nemuranu Machi no Cinderella: Hirose Ryouichi - Memorial Date", "Steady x Study", "Kagami","Ai (ONA)", "Wedding Park"])

    def test_valid_genre_case_insensitivity_capital(self):
        # This unit test tests for a genre that is within the database with case sensitive strings such as all of the letters being capitalized and checks to see if these animes are within the returned set
        result = api1.getTitleofAnimefromGenre("romance")
        self.assertEqual(result, ["Amagami SS+ Plus Specials", "Koitabi: True Tours Nanto", "To Heart 2 AD Plus", "Ushinawareta Mirai wo Motomete: Ushinawareta Natsuyasumi wo Motomete", "Koikishi Purely☆Kiss The Animation: Special Edition", "True Love Story", "Choujuu Giga", "Sekishoku Elegy","Suki Desu Suzuki-kun!!", "Monogatari no Aru Satou", "Nemuranu Machi no Cinderella: Hirose Ryouichi - Memorial Date", "Steady x Study", "Kagami","Ai (ONA)", "Wedding Park"])
    
    
    def test_invalid_genre(self):
        # This unit test tests for a genre that is not in the database 
        result_1 = api1.getTitleofAnimefromGenre("Utopian Russia")
        result_2 = api1.getTitleofAnimefromGenre("RomCom")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])


    def test_valid_score_exact_match(self):
        # Test for valid input, where the score of an anime is present in the list of animes
        result_1 = api1.getTitleofAnimefromScore("8.95")
        result_2 = api1.getTitleofAnimefromScore("9.23")
        result_3 = api1.getTitleofAnimefromScore("8.9")
        self.assertEqual(result_1, ["Gintama Movie 2: Kanketsu-hen - Yorozuya yo Eien Nare"])
        self.assertEqual(result_2, ["Fullmetal Alchemist: Brotherhood"])
        self.assertEqual(result_3, ["Sen to Chihiro no Kamikakushi"])

    
    def test_invalid_negative_score(self):
        # Test for invalid input, where the score of an anime is not present in the list of animes so [] should be returned
        result_1 = api1.getTitleofAnimefromScore("-1.0")
        result_2 = api1.getTitleofAnimefromScore("-7.0")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])
    
    
    def test_invalid_positvie_score(self):
        # Test for invalid input, where the score of an anime is not present in the list of animes so [] should be returned
        result_1 = api1.getTitleofAnimefromScore("1.0")
        result_2 = api1.getTitleofAnimefromScore("12.0")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])


    def test_valid_input_of_episodes(self):
        # Test for valid input, where the number of episodes is present in the list of animes
        result_1 = api1.getTitleofAnimefromNumberOfepisodes("88")
        result_2 = api1.getTitleofAnimefromNumberOfepisodes("500")
        result_3 = api1.getTitleofAnimefromNumberOfepisodes("99")
        result_4 = api1.getTitleofAnimefromNumberOfepisodes("66")
        self.assertEqual(result_1, ["Mahoutsukai Sally 2", "Hong Mao Lan Tu: Konglong Shijie", "Manga Kotowaja Jiten"])
        self.assertEqual(result_2, ["Naruto: Shippuuden"])
        self.assertEqual(result_3, ["Uchuu Kyoudai", "Mister Ajikko"])
        self.assertEqual(result_4, ["Cyborg Kuro-chan", "Mini Moni Yaru no da Pyon!"])


    def test_invalid_whole_positive_num_episodes(self):
        # Test for invalid input, where the number of episodes is not present in the list of animes so "[]" should be returned
        result_1 = api1.getTitleofAnimefromNumberOfepisodes("8043")
        result_2 = api1.getTitleofAnimefromNumberOfepisodes("1959")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])


    def test_invalid_whole_negative_num_episodes(self):
        # Test for invalid input, where the number of episodes is not present in the list of animes so "[]" should be returned
        result_1 = api1.getTitleofAnimefromNumberOfepisodes("-8")
        result_2 = api1.getTitleofAnimefromNumberOfepisodes("-500")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])


    def test_invalid_positive_decimal_input_episodes(self):
        # Test for invalid input, where the number of episodes is a decimal and not present in the list of animes so "[]" should be returned
        result_1 = api1.getTitleofAnimefromNumberOfepisodes("6.3")
        result_2 = api1.getTitleofAnimefromNumberOfepisodes("1.0")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])
    

    def test_invalid_negative_decimal_input_episodes(self):
        # Test for invalid input, where the number of episodes is a decimal and not present in the list of animes so "[]" should be returned
        result_1 = api1.getTitleofAnimefromNumberOfepisodes("-6.3")
        result_2 = api1.getTitleofAnimefromNumberOfepisodes("-2.0")
        self.assertEqual(result_1, [])
        self.assertEqual(result_2, [])


    def test_genre_with_existing_title(self):
        # Test for valid input of an anime title, where the genre returned will match the genre of the anime
        result_1 = api1.getGenre("Made in Abyss")
        result_2 = api1.getGenre("Shigatsu wa Kimi no Uso")
        self.assertEqual(result_1, "Sci-Fi, Adventure, Mystery, Drama, Fantasy")
        self.assertEqual(result_2, "Drama, Music, Romance, School, Shounen")
    

    def test_genre_with_nonexisting_title(self):
        # Test for invalid input of an anime title, where "None" should be returned for the genre
        result_1 = api1.getGenre("Made Here and There")
        result_2 = api1.getGenre("Naruto: Shippuudden")
        self.assertEqual(result_1, None)
        self.assertEqual(result_2, None)

    
    def test_score_with_existing_title(self):
        # Test for valid input of anime title, where the score returned will match the score of the anime
        result_1 = api1.getScoreofAnime("Made in Abyss")
        result_2 = api1.getScoreofAnime("Hello World")
        result_3 = api1.getScoreofAnime("Yuuki no Hana ga Hiraku Toki: Yanase Takashi to Anpanman no Monogatari")
        self.assertEqual(result_1, 8.83)
        self.assertEqual(result_2, 7.9)
        self.assertEqual(result_3, 8.0)
    

    def test_score_with_nonexisting_title(self):
        # Test for invalid input, where the title of the anime does not exist so "None" should be returned
        result_1 = api1.getScoreofAnime("The Way of the Wind")
        result_2 = api1.getScoreofAnime("The World Titans")
        self.assertEqual(result_1, None)
        self.assertEqual(result_2, None)


    def test_episodes_with_existing_title(self):
        # Test for valid input of an anime title, where the episodes returned will match the episodes of the anime
        result_1 = api1.getNumberofEpisodes("Little Witch Academia")
        result_2 = api1.getNumberofEpisodes("Jormungand")
        self.assertEqual(result_1, 1)
        self.assertEqual(result_2, 12)
    

    def test_episodes_with_nonexisting_title(self):
        # Test for invalid input, where the title of the anime does not exist so "None" should be returned
        result_1 = api1.getNumberofEpisodes("Little Person")
        result_2 = api1.getNumberofEpisodes("The Tiger Hero")
        self.assertEqual(result_1, None)
        self.assertEqual(result_2, None)

    def test_synopsis_with_existing_title(self):
        # Test for valid input of an anime title, where the synopsis returned will match the synopsis of the anime
        result_1 = api1.getSynopsis("Code Geass: Hangyaku no Lelouch R2 Special Edition - Zero Requiem")
        result_2 = api1.getSynopsis("Shingeki no Kyojin OVA")
        self.assertEqual(result_1, "An OVA summarizing all 25 episodes of season 2.")
        self.assertEqual(result_2, "Bundled with the 12th, 13th, and 14th limited-edition manga volumes.")

    def test_synopsis_with_nonexisting_title(self):
        # Test for invalid input, where the title of the anime does not exist so "None" should be returned
        result_1 = api1.getSynopsis("The Way of Life")
        result_2 = api1.getSynopsis("The Ninjas of CS")
        self.assertEqual(result_1, None)
        self.assertEqual(result_2, None)

if __name__ == '__main__':
    unittest.main()