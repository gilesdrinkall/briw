import unittest
from round import create_dictionary, Round


class Test_Methods(unittest.TestCase):
    def test_create_dictionary(self):

        # Arrange

        filesname = "test2.txt"

        expected_output = {'1': 'Dan', '2':'Giles', '3':'David'}

        # Act

        actual_output = create_dictionary(filesname)

        # Assert

        self.assertEqual(actual_output, expected_output)

    def test_get_favourites(self):

        # Arrange

        new_file = "favourites.txt"
        favourites = create_dictionary(new_file)
        test_instance = Round("bob", favourites)

        expected_output = [['Chris', 'Cappuccino'], ['Connor', 'Cappuccino'], ['Ed', 'Latte']]

        # Act

        actual_output = test_instance.get_favourites()

        # Assert

        self.assertEqual(actual_output, expected_output)

    # def test_dictionary_is_populated_with_ids_inputted_by_users(self):
    #
    #     #Arrange
    #
    #     new_file = "favourites.txt"
    #     favourites = create_dictionary(new_file)
    #     test_round = Round("bob", favourites)
    #
    #
    #     expected_output = {'':'', '':''], ['', ''}
    #
    #     # Act
    #
    #     actual_output = test_round.put_order_id()
    #
    #     # Assert
    #
    #     self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()