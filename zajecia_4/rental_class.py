

class Rental:
    @staticmethod
    def open_the_bike_magazine(file):
        all_bikes = []
        with open(file, 'r') as magazine:
            for line in magazine:
                tmp = line.strip().split()
                bikes_dict = {'Brand': tmp[0], 'Amount': int(tmp[1]), 'Price': float(tmp[2])}
                all_bikes.append(bikes_dict)
            print(all_bikes)
        return all_bikes

    @staticmethod
    def print_magazine(all_bikes):
        print(all_bikes)

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
    def rent(dict_with_bike, who, brand, time, renting_list):

        if dict_with_bike['Amount'] == 0:
            print("All bikes of this brand are checked out: ")
            return False
        elif int(dict_with_bike['Amount']) > 0:
            dict_with_bike['Amount'] -= 1

        renting_dict = {'Name': who, 'Brand': brand, 'SHour': int(time[0]), 'SMinute': int(time[1]), 'EHour': '', 'EMinute': '', 'Minutes': '', 'Costs': ''}
        renting_list.append(renting_dict)
        return renting_list

    @staticmethod
    def return_bike(dict_with_bike, who, brand, time, renting_list):
        rent_dict = {}
        for i in renting_list:
            if brand == i['Brand']:
                rent_dict = i
                if i['Name'] != who:
                    print("This person doesn't rent this bike")
                    return False

                i['EHour'] = int(time[0])
                i['EMinute'] = int(time[1])
                minutes = (i['EHour']-i['SHour'])*60.0 + (i['EMinute']-i['SMinute'])
                cost = dict_with_bike['Price'] * minutes
                i['Minutes'] = minutes
                i['Costs'] = cost

        if rent_dict == {}:
            print("This bike wasn't rented")
            return False

        if brand == dict_with_bike['Brand']:
            dict_with_bike['Amount'] += 1

        return renting_list

    @staticmethod
    def taking_data(all_bikes, renting_list):

        try:
            action = input("Choose your action: renting <1> or return <2>")
            if action != '1' and action != '2':
                print("Wrong input!")
                raise ValueError
        except:
            return False

        who = input("Enter name of biker: ")
        brand = input("Enter brand of bike: ")

        dict_with_bike = {}
        for i in all_bikes:
            if brand == i['Brand']:
                dict_with_bike = i
        if dict_with_bike == {}:
            print("Bike doesn't exist")
            return False

        if action == '1':
            tmp_time = input("Enter current time e.g. <12:30>: ")
            try:
                time = Rental.changing_time(tmp_time)
            except:
                return False
            Rental.rent(dict_with_bike, who, brand, time, renting_list)

        elif action == '2':
            tmp_time = input("Enter current time e.g. <12:30>: ")
            try:
                time = Rental.changing_time(tmp_time)
            except:
                return False
            Rental.return_bike(dict_with_bike, who, brand, time, renting_list)

        return dict_with_bike


if __name__ == '__main__':
    bikes = Rental.open_the_bike_magazine('bike_magazine.txt')
    renting_list = []

    while 1:
        Rental.taking_data(bikes, renting_list)
        Rental.print_magazine(bikes)
        print(renting_list)


