from unittest.mock import Mock
import unittest
import mock
from source.persistence.database import *

class TestDictionarySubset(unittest.TestCase):


    @mock.patch("source.persistence.database.get_db_connection")
    def test_dictionary_subset_created_from_database_query(self, get_db_connection):

        #arrange

        db_mock = Mock()

        get_db_connection.return_value = db_mock

        cursor_mock = Mock()

        db_mock.cursor.return_value = cursor_mock

        cursor_mock.fetchall.return_value = [{"person_id": "1", "first_name": "Giles", "surname": "Drinkall"}, {"person_id": "2", "first_name": "Chris", "surname": "Whitlam"}]

        test_table = "test_table"
        pers_id = "person_id"
        first_name = "first_name"

        expected = {"1": "Giles", "2": "Chris"}

        #act

        actual = create_dictionary(test_table, pers_id, first_name)

        #assert

        self.assertEqual(expected, actual)

if __name__=="__main__":
    unittest.main()