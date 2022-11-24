import unittest
from rental_class import Rental


class Test_TestDay(unittest.TestCase):

    def test_parse_file_line(self):
        magazine_1 = [{'Brand': 'rower_1', 'Amount': 1, 'Price': 0.12},
                      {'Brand': 'rower_2', 'Amount': 3, 'Price': 0.12},
                      {'Brand': 'rower_3', 'Amount': 5, 'Price': 0.25},
                      {'Brand': 'rower_4', 'Amount': 1, 'Price': 0.3},
                      {'Brand': 'rower_5', 'Amount': 2, 'Price': 0.3},
                      {'Brand': 'rower_6', 'Amount': 3, 'Price': 0.45},
                      {'Brand': 'rower_7', 'Amount': 2, 'Price': 0.5},
                      {'Brand': 'rower_8', 'Amount': 4, 'Price': 0.5}]

        self.assertEqual(Rental.open_the_bike_magazine('bike_magazine.txt'), magazine_1)

    def test_changing_time(self):
        time_1 = '4:56'
        time_2 = '5:98'
        time_3 = '25:15'
        self.assertEqual(Rental.changing_time(time_1), [4, 56])
        self.assertFalse(Rental.changing_time(time_2))
        self.assertFalse(Rental.changing_time(time_3))

    def test_rent(self):

        dict_with_bike_1 = {'Brand': 'rower_2', 'Amount': 3, 'Price': 0.12}
        dict_with_bike_2 = {'Brand': 'rower_1', 'Amount': 0, 'Price': 0.12}
        who = 'Julia Sadecka'
        bike_1 = 'rower_1'
        bike_2 = 'rower_2'
        time = [3, 45]
        renting_list_1 = []
        renting_list_2 = [{'Name': 'Wojtek', 'Brand': 'rower_3', 'SHour': 6, 'SMinute': 55, 'EHour': '', 'EMinute': '', 'Minutes': '', 'Costs': ''}]

        dict_with_bike_1_after = {'Brand': 'rower_2', 'Amount': 2, 'Price': 0.12}
        renting_list_1_after = [{'Name': 'Julia Sadecka', 'Brand': 'rower_2', 'SHour': 3, 'SMinute': 45, 'EHour': '', 'EMinute': '', 'Minutes': '', 'Costs': ''}]
        renting_list_2_after = [{'Name': 'Wojtek', 'Brand': 'rower_3', 'SHour': 6, 'SMinute': 55, 'EHour': '', 'EMinute': '', 'Minutes': '', 'Costs': ''},
                                {'Name': 'Julia Sadecka', 'Brand': 'rower_2', 'SHour': 3, 'SMinute': 45, 'EHour': '', 'EMinute': '', 'Minutes': '', 'Costs': ''}]

        self.assertEqual(Rental.rent(dict_with_bike_1, who, bike_2, time, renting_list_1),
                         renting_list_1_after)
        self.assertEqual(Rental.rent(dict_with_bike_1, who, bike_2, time, renting_list_2),
                         renting_list_2_after)
        self.assertFalse(Rental.rent(dict_with_bike_2, who, bike_1, time, renting_list_1))

    def test_return_bike(self):
        
        renting_list_1 = [{'Name': 'Wojtek', 'Brand': 'rower_3', 'SHour': 6, 'SMinute': 55, 'EHour': '', 'EMinute': '', 'Minutes': '', 'Costs': '' }]
        dict_with_bike_1 = {'Brand': 'rower_3', 'Amount': 0, 'Price': 0.25}
        who_1 = 'Wojtek'
        who_2 = 'Julia Sadecka'
        bike_1 = 'rower_3'
        bike_2 = 'rower_2'
        time = [8, 45]
        renting_list_1_after = [{'Name': 'Wojtek', 'Brand': 'rower_3', 'SHour': 6, 'SMinute': 55, 'EHour': 8, 'EMinute': 45, 'Minutes': 110.0, 'Costs': 27.5}]

        self.assertEqual(Rental.return_bike(dict_with_bike_1, who_1, bike_1, time, renting_list_1), renting_list_1_after)
        self.assertFalse(Rental.return_bike(dict_with_bike_1, who_2, bike_1, time, renting_list_1))
        self.assertFalse(Rental.return_bike(dict_with_bike_1, who_1, bike_2, time, renting_list_1))


if __name__ == '__main__':
    unittest.main()