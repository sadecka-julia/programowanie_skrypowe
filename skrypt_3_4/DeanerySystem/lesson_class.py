from term import Term
from class_day import Day

class Lesson:
    def __init__(self, term, name:str, teacherName:str, year:int, fullTime = True):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.fullTime = fullTime

    def __str__(self):
        if self.fullTime:
            rodzaj = 'Stacjonarne'
        if not self.fullTime:
            rodzaj = 'Niestacjonarne'
        return f"{self.name} ({self.term.day_of_the_week()} {self.term.hour}:{self.term.minute}-{(self.term.hour + (self.term.duration // 60) + ((self.term.minute +(self.term.duration % 60)) // 60))}:{(self.term.minute +   self.term.duration) % 60}\n{self.year} {rodzaj}\n{self.teacherName}"

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

    def earlierTime(self):
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



