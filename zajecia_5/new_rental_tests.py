import unittest
from new_rental_class import Rental, Bicycle, Client


class TestNewRental(unittest.TestCase):

    def test_changing_time(self):
        # Testy funkcji konwertującej czas, która także sprawdza czy podany czas jest poprawny
        time_1 = '4:56'
        time_2 = '5:98'
        time_3 = '25:15'
        self.assertEqual(Rental.changing_time(time_1), [4, 56])
        self.assertFalse(Rental.changing_time(time_2))
        self.assertFalse(Rental.changing_time(time_3))

    def test_rent_and_return(self):
        # Wprowadzone dane
        bike1 = Bicycle('model_1', 1.2)
        bike2 = Bicycle('model_2', 3.12)
        client1 = Client('Bartek', 'Fober', 'ul.Dojazdowa 43 Gdańsk')
        client2 = Client('Adam', 'Kasielski', 'ul.Dluga 1 Wisła')
        Rental.add_bike(bike1)
        Rental.add_bike(bike2)
        Rental.add_client(client1)
        Rental.add_client(client2)

        # Poprawne wyniki wypożyczenia
        result1 = [{'Bike_ID': 1000, 'Brand': 'model_1', 'Price': 1.2,
                    'Client_ID': 1000, 'Rent_Time': '4:23', 'Return_time': None},
                   {'Bike_ID': 1001, 'Brand': 'model_2', 'Price': 3.12,
                    'Client_ID': None, 'Rent_Time': None, 'Return_time': None}]
        result2 = [{'Bike_ID': 1000, 'Brand': 'model_1', 'Price': 1.2,
                    'Client_ID': 1000, 'Rent_Time': '4:23', 'Return_time': None},
                   {'Bike_ID': 1001, 'Brand': 'model_2', 'Price': 3.12,
                    'Client_ID': 1001, 'Rent_Time': '4:56', 'Return_time': None}]

        # Testy wypożyczenia
        self.assertEqual(Rental.rent(1000, 'model_1', '4:23'), result1)
        Rental.rent(1000, 'model_1', '4:23')
        self.assertEqual(Rental.rent(1001, 'model_2', '4:56'), result2)
        Rental.rent(1001, 'model_2', '4:56')
        self.assertFalse(Rental.rent(1000, 'nieistniejący', '1:12'))   # Wypożycznie nieistniejącego modelu
        self.assertFalse(Rental.rent(1001, 'model_2', '16:33'))        # Wypożyczenie modelu już wypożyczonego

        # Wyniki po zwróceniu pojazdu
        result3 = [{'Bike_ID': 1000, 'Client_ID': 1000, 'Costs': 159.6, 'Minutes': 133}]
        result4 = [{'Bike_ID': 1000, 'Client_ID': 1000, 'Costs': 159.6, 'Minutes': 133},
                   {'Bike_ID': 1001, 'Client_ID': 1001, 'Costs': 1357.2, 'Minutes': 435}]

        # Testy zwrotu pojazdu
        self.assertEqual(Rental.returning(1000, '6:36'), result3)
        Rental.returning(1000, '6:36')
        self.assertEqual(Rental.returning(1001, '12:11'), result4)
        Rental.returning(1001, '12:11')
        self.assertFalse(Rental.returning(1012, '12:11'))       # Zwrócenie pojazdu o nieistniejącym ID
        self.assertFalse(Rental.returning(1001, '12:11'))       # Ponowne zwrócenie pojazdu

    def test_magical_function(self):
        bike1 = Bicycle('model_1', 1.2)
        bike2 = Bicycle('model_2', 3.12)
        client1 = Client('Bartek', 'Fober', 'ul.Dojazdowa 43 Gdańsk')
        client2 = Client('Adam', 'Kasielski', 'ul.Dluga 1 Wisła')
        Rental.add_bike(bike1)
        Rental.add_bike(bike2)
        Rental.add_client(client1)
        Rental.add_client(client2)
        result1 = [{'Bike_ID': 1000, 'Brand': 'model_1', 'Price': 1.2,
                    'Client_ID': 1000, 'Rent_Time': '12:34', 'Return_time': None},
                   {'Bike_ID': 1001, 'Brand': 'model_2', 'Price': 3.12,
                    'Client_ID': None, 'Rent_Time': None, 'Return_time': None}]
        result2 = [{'Bike_ID': 1000, 'Brand': 'model_1', 'Price': 1.2,
                    'Client_ID': 1000, 'Rent_Time': '12:34', 'Return_time': None},
                   {'Bike_ID': 1001, 'Brand': 'model_2', 'Price': 3.12,
                    'Client_ID': 1000, 'Rent_Time': '12:34', 'Return_time': None}]
        result3 = [{'Bike_ID': 1000, 'Client_ID': 1000,
                    'Costs': 333.59999999999997, 'Minutes': 278}]
        result4 = [{'Bike_ID': 1000, 'Client_ID': 1000,
                    'Costs': 333.59999999999997, 'Minutes': 278},
                   {'Bike_ID': 1001, 'Client_ID': 1000,
                    'Costs': 867.36, 'Minutes': 278}]

        self.assertEqual(bike1 << client1, result1)
        self.assertEqual(bike2 << client1, result2)
        self.assertFalse(bike1 << client1)

        self.assertEqual(bike1 >> client1, result3)
        self.assertEqual(bike2 >> client1, result4)
        self.assertFalse(bike1 >> client2)


if __name__ == '__main__':
    unittest.main()