import unittest
from unittest import mock
from source.persistence.database import *


class Test_Methods(unittest.TestCase):


    @mock.patch("source.persistence.database.get_db_connection")
    def test_get_maker_name_from_db_calls_cursor_execute(self, get_db_connection):

        db_mock = mock.Mock()

        get_db_connection.return_value = db_mock

        cursor_mock = mock.Mock()

        db_mock.cursor.return_value = cursor_mock

        get_maker_name_from_db()

        expected_sql_query = "SELECT maker_name FROM round ORDER BY round_id DESC LIMIT 1;"

        cursor_mock.execute.assert_called_with(expected_sql_query)


    @mock.patch("source.persistence.database.get_db_connection")
    def test_add_maker_name_to_db_calls_cursor_execute(self, get_db_connection):

        db_mock = mock.Mock()

        get_db_connection.return_value = db_mock

        cursor_mock = mock.Mock()

        db_mock.cursor.return_value = cursor_mock

        maker_name = "Giles"

        add_maker_to_db(maker_name)

        expected_sql_query = 'INSERT INTO round (maker_name) VALUES ("Giles");'

        cursor_mock.execute.assert_called_with(expected_sql_query)


    @mock.patch("source.persistence.database.get_db_connection")
    def test_get_maker_name_from_db_returns_expected_value(self, get_db_connection):

        db_mock = mock.Mock()

        get_db_connection.return_value = db_mock

        cursor_mock = mock.Mock()

        db_mock.cursor.return_value = cursor_mock

        expected_value = "Giles"

        cursor_mock.fetchone.return_value = expected_value

        actual_value = get_maker_name_from_db()

        self.assertEqual(expected_value, actual_value)


    # @mock.patch("source.persistence.database.get_db_connection")
    # def test_add_maker_to_db_(self, get_db_connection):
    #
    #     db_mock = mock.Mock()
    #
    #     get_db_connection.return_value = db_mock
    #
    #     cursor_mock = mock.Mock()
    #
    #     db_mock.cursor.return_value = cursor_mock
    #
    #     maker_name = "John"
    #
    #     expected_value = 1
    #
    #     cursor_mock.lastrowid.return_value = expected_value
    #
    #     actual_value = add_maker_to_db(maker_name)
    #
    #     self.assertEqual(expected_value, actual_value)


    # def test_create_dictionary(self):
    #
    #     # Arrange
    #
    #     filesname = "test2.txt"
    #
    #     expected_output = {'1': 'Dan', '2':'Giles', '3':'David'}
    #
    #     # Act
    #
    #     actual_output = create_dictionary(filesname)
    #
    #     # Assert
    #
    #     self.assertEqual(actual_output, expected_output)
    #
    # def test_get_favourites(self):
    #
    #     # Arrange
    #
    #     new_file = "favourites.txt"
    #     favourites = create_dictionary(new_file)
    #     test_instance = Round("bob", favourites)
    #
    #     expected_output = [['Chris', 'Cappuccino'], ['Connor', 'Cappuccino'], ['Ed', 'Latte']]
    #
    #     # Act
    #
    #     actual_output = test_instance.get_favourites()
    #
    #     # Assert
    #
    #     self.assertEqual(actual_output, expected_output)

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