import time


class Client:
    def __init__(self, name, surname, address):
        self.client_id = Rental.client_id
        self.name = name
        self.surname = surname
        self.address = address
        Rental.client_id += 1

    def __str__(self):
        return f'{self.client_id}, {self.name} {self.surname}, address: {self.address}'


class Bicycle:
    def __init__(self, brand, price):
        self.bicycle_id = Rental.bicycle_id
        self.client_id = None
        self.brand = brand
        self.price = price
        self.rent_time = None
        self.return_time = None
        Rental.bicycle_id += 1

    def __repr__(self):
        return '''
                self.bicycle_id = Rental.bicycle_id
                self.client_id = None
                self.brand = brand
                self.price = price
                self.rent_time = None
                self.return_time = None
                '''

    def __str__(self):
        return f'Bicycle ID: {self.bicycle_id}, Brand: {self.brand}, Price: {self.price}, Client ID: {self.client_id}, Rent Time: {self.rent_time}, Return Time: {self.return_time} '

    def __lshift__(self, other):
        cur_date = time.ctime()
        cur_time = cur_date[11:16]
        return Rental.rent(other.client_id, self.brand, '12:34')

    def __rshift__(self, other):
        cur_date = time.ctime()
        cur_time = cur_date[11:16]
        return Rental.returning(self.bicycle_id, '17:12')


class Rental(Bicycle, Client):

    bike_list = []
    clients_list = []
    operation_list = []
    client_id = 1000
    bicycle_id = 1000

    @staticmethod
    def changing_time(time):
        new_time = time.split(sep=':')
        if int(new_time[0]) > 23 or int(new_time[0]) < 0 or int(new_time[1]) > 59 or int(new_time[1]) < 0:
            print("The time is wrong.")
            return False
        for i in range(len(new_time)):
            new_time[i] = int(new_time[i])
        return new_time

    @staticmethod
    def add_bike(self):
        bike_info = {'Bike_ID': self.bicycle_id, 'Brand': self.brand, 'Price': self.price, 'Client_ID': self.client_id, 'Rent_Time': self.rent_time, 'Return_time': self.return_time}
        Rental.bike_list.append(bike_info)

    @staticmethod
    def add_client(self):
        client_info = {'Client_ID': self.client_id, 'Name': self.name, 'Surname': self.surname, 'Address': self.address}
        Rental.clients_list.append(client_info)

    @staticmethod
    def rent(client_id, wanted_brand, rent_time):
        list = Rental.bike_list
        for bike in range(len(list)):
            if Rental.bike_list[bike]['Brand'] == wanted_brand and Rental.bike_list[bike]['Client_ID'] is None:
                Rental.bike_list[bike]['Client_ID'] = client_id
                Rental.bike_list[bike]['Rent_Time'] = rent_time
                print(Rental.bike_list)
                return Rental.bike_list
        print('Bike does not exist or is rented')
        return False

    @staticmethod
    def returning(bike_id, return_time):
        list = Rental.bike_list
        for bike in range(len(list)):
            if Rental.bike_list[bike]['Bike_ID'] == bike_id and Rental.bike_list[bike]['Client_ID'] is not None:
                Rental.bike_list[bike]['Return_Time'] = return_time

                rnt_arr = Rental.changing_time(Rental.bike_list[bike]['Rent_Time'])
                rtt_arr = Rental.changing_time(return_time)
                minutes = (rtt_arr[0]-rnt_arr[0])*60 + rtt_arr[1]-rnt_arr[1]
                costs = minutes*(float(Rental.bike_list[bike]['Price']))

                transaction = {'Bike_ID': bike_id, 'Client_ID': Rental.bike_list[bike]['Client_ID'], 'Costs': costs, 'Minutes': minutes}
                Rental.operation_list.append(transaction)
                Rental.bike_list[bike]['Client_ID'] = None
                print(Rental.operation_list)
                return Rental.operation_list
        return False

    # bike_list, clients_list, operation_list
    @staticmethod
    def print_data(magazin):
        for element in magazin:
            print(element)


# bike1 = Bicycle('model_1', 1.2)
# bike2 = Bicycle('model_2', 3.12)
# client1 = Client('Bartek', 'Fober', 'ul.Dojazdowa 43 Gdańsk')
# client2 = Client('Adam', 'Kasielski', 'ul.Dluga 1 Wisła')
# Rental.add_bike(bike1)
# Rental.add_bike(bike2)
# Rental.add_client(client1)
# Rental.add_client(client2)
# bike1 << client1
# bike2 << client1
# Rental.print_data(Rental.bike_list)
# bike1 >> client1
# bike2 >> client1
# Rental.rent(1000, 'model_1', '4:23')
# Rental.rent(1001, 'model_2', '4:56')
# Rental.returning(1000, '6:36')
# Rental.returning(1001, '12:11')
# print(bike1)
# print(client1)
