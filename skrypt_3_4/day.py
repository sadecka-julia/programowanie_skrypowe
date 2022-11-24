from enum import Enum


class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):
        wyn = day.value-self.value
        if (wyn < 4 and wyn > -4):
            return wyn
        elif (wyn > 4):
            return (-1)*(7-wyn)
        else:
            return 7+wyn


def nthDayFrom(n, day):
    num_of_day = day.value
    if (n+num_of_day) % 7 == 0:
        new_day = 7
    else:
        new_day = (n+num_of_day) % 7
    return Day(new_day)
