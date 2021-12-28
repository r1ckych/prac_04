class ProgrammingLanguage:
    def __init__(self, name="", typing='', reflection=True and False, year=1980):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        pass

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}\n".format(self.name, self.typing, self.reflection,
                                                                             self.year)
