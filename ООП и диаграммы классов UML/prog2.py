class Mother:
    def print(self):
        print(self.voice())

    def voice(self):
        return "Вставай, тебе на пары!"


class Daughter(Mother):
    def voice(self):
        return "Мам, мне ко второй!"


a = Daughter()
a.print()
