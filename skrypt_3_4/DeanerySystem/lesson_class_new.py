from class_day import Day
from term import Term

class Lesson():
    def __init__(self):
        self.__term = None
        self.__name = None
        self.__teacherName = None
        self.__year = None
        self.__fullTime = None

    @property
    def term(self):
        return self.__term

    @property
    def name(self):
        return self.__name

    @property
    def teacherName(self):
        return self.__teacherName

    @property
    def year(self):
        return self.__year

    @property
    def fullTime(self):
        return self.__fullTime

    @term.setter
    def term(self, given_term):
        self.__term = given_term

    @name.setter
    def name(self, given_name):
        self.__name = given_name

    @teacherName.setter
    def teacherName(self, given_teacher_name):
        self.__teacherName = given_teacher_name

    @year.setter
    def year(self, year):
        if year in range(1, 6):
            self.__year = year
        else:
            print("Incorrect year.")

    @fullTime.setter
    def fullTime(self, given_data):
        if isinstance(given_data, bool):
            self.__fullTime = given_data
        else:
            print("Incorrect full-time.")

    def laterDay(self):
        if self.fullTime:
            if self.term._Term__day.value == 1:
                if self.term.hour < 16 or (self.term.hour == 16 and self.term.minute <= 30):
                    self.term._Term__day = self.term._Term__day.day_change(-3)
                    return True
                return False
            elif self.term._Term__day.value in [2, 3, 4, 5]:
                self.term._Term__day = self.term._Term__day.day_change(-1)
                return True

        else:
            if self.term._Term__day.value == 7:
                self.term._Term__day = self.term._Term__day.day_change(-1)
                return True
            elif self.term._Term__day.value == 6:
                if 17 < self.term.hour < 19:
                    self.term._Term__day = self.term._Term__day.day_change(-1)
                    return True
                elif self.term.hour == 19 and self.term.minute < 30:
                    self.term._Term__day = self.term._Term__day.day_change(-1)
                    return True
                return False

    def earlierDay(self):
        if self.fullTime:
            if self.term._Term__day.value == 5:
                self.term._Term__day = self.term._Term__day.day_change(3)
                return True
            elif self.term._Term__day.value in [1, 2, 3]:
                self.term._Term__day = self.term._Term__day.day_change(1)
                return True
            elif self.term._Term__day.value == 4:
                if 8 < self.term.hour < 16 or (self.term.hour == 16 and self.term.minute <= 30):
                    self.term._Term__day = self.term._Term__day.day_change(1)
                    return True
                return False
            return False

        else:
            if self.term._Term__day.value in [5, 6]:
                self.term._Term__day = self.term._Term__day.day_change(1)
                return True
            elif self.term._Term__day.value == 7:
                if 17 < self.term.hour < 19:
                    self.term._Term__day = self.term._Term__day.day_change(-2)
                    return True
                elif self.term.hour == 19 and self.term.minute < 30:
                    self.term._Term__day = self.term._Term__day.day_change(-2)
                    return True
                return False

    def ealierTime(self):
        if self.fullTime:
            if self.term._Term__day.value in [1, 2, 3, 4]:
                if self.term.hour*60 + self.term.minute - self.term.duration >= 480:
                    if self.term.hour*60 + self.term.minute + self.term.duration <= 1200:
                        self.term.hour = self.term.hour - (self.term.duration // 60)
                        self.term.minute = self.term.minute - (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            if self.term._Term__day.value == 5:
                if self.term.hour*60 + self.term.minute - self.term.duration >= 480:
                    if self.term.hour*60 + self.term.minute + self.term.duration <= 1020:
                        self.term.hour = self.term.hour - (self.term.duration // 60)
                        self.term.minute = self.term.minute - (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            return False

        else:
            if self.term._Term__day.value in [6, 7]:
                if self.term.hour*60 + self.term.minute - self.term.duration >= 480:
                    if self.term.hour*60 + self.term.minute + self.term.duration <= 1200:
                        self.term.hour = self.term.hour - (self.term.duration // 60)
                        self.term.minute = self.term.minute - (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            if self.term._Term__day.value == 5:
                if self.term.hour*60 + self.term.minute - self.term.duration >= 1020:
                    if self.term.hour*60 + self.term.minute + self.term.duration <= 1200:
                        self.term.hour = self.term.hour - (self.term.duration // 60)
                        self.term.minute = self.term.minute - (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            return False

    def laterTime(self):
        if self.fullTime:
            if self.term._Term__day.value in [1, 2, 3, 4]:
                if self.term.hour*60 + self.term.minute + self.term.duration >= 480:
                    if self.term.hour*60 + self.term.minute - self.term.duration <= 1200:
                        self.term.hour = self.term.hour + (self.term.duration // 60)
                        self.term.minute = self.term.minute + (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            if self.term._Term__day.value == 5:
                if self.term.hour*60 + self.term.minute + self.term.duration >= 480:
                    if self.term.hour*60 + self.term.minute - self.term.duration <= 1020:
                        self.term.hour = self.term.hour + (self.term.duration // 60)
                        self.term.minute = self.term.minute + (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            return False

        else:
            if self.term._Term__day.value in [6, 7]:
                if self.term.hour*60 + self.term.minute + self.term.duration >= 480:
                    if self.term.hour*60 + self.term.minute - self.term.duration <= 1200:
                        self.term.hour = self.term.hour + (self.term.duration // 60)
                        self.term.minute = self.term.minute + (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            
            if self.term._Term__day.value == 5:
                if self.term.hour*60 + self.term.minute + self.term.duration >= 1020:
                    if self.term.hour*60 + self.term.minute - self.term.duration <= 1200:
                        self.term.hour = self.term.hour + (self.term.duration // 60)
                        self.term.minute = self.term.minute + (self.term.duration - ((self.term.duration // 60) * 60))
                        return True
                    return False
                return False
            return False
