from class_day import Day


class Term:
    def __init__(self, day, hour, minute, duration = 90):
        self.__day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def day_of_the_week(self):
        if self.__day.value == 1:
            name = 'Poniedziałek'
        elif self.__day.value == 2:
            name = 'Wtorek'
        elif self.__day.value == 3:
            name = 'Środa'
        elif self.__day.value == 4:
            name = 'Czwartek'
        elif self.__day.value == 5:
            name = 'Piątek'
        elif self.__day.value == 6:
            name = 'Sobota'
        elif self.__day.value == 7:
            name = 'Niedziela'
        return name

    def __str__(self):
        return '"' + Term.day_of_the_week(self) + ' ' + str(self.hour) + ':' + str(self.minute) + ' [' + str(self.duration) + ']"'

    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            return True
        elif self.__day.value > termin.__day.value:
            return False
        if self.hour < termin.hour:
            return True
        elif self.hour > termin.hour:
            return False
        if self.minute < termin.minute:
            return True
        return False

    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            return True
        elif self.__day.value < termin.__day.value:
            return False
        if self.hour > termin.hour:
            return True
        elif self.hour < termin.hour:
            return False
        if self.minute > termin.minute:
            return True
        return False

    def equals(self, termin):
        if self.__day.value == termin.__day.value and self.hour == termin.hour and self.minute == termin.minute:
            return True
        return False

    def __sub__(self, termin):
        day_value = self.__day.value - termin.__day.value
        if day_value < 0:
            day_value += 7
        minutes = day_value*24*60 + (self.hour - termin.hour)*60 + (self.minute - termin.minute) + self.duration
        return Term(termin.__day, termin.hour, termin.minute, minutes)

    def __lt__(self, termin):
        if self.earlierThan(termin):
            return True
        return False

    def __le__(self, termin):
        if self.earlierThan(termin) or self.equals(termin):
            return True
        return False

    def __gt__(self, termin):
        if self.laterThan(termin):
            return True
        return False

    def __ge__(self, termin):
        if self.laterThan(termin) or self.equals(termin):
            return True
        return False

    def __eq__(self, termin):
        if self.equals(termin):
            return True
        return False
