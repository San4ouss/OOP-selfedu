class StreamData:
    def create(self, FIELDS, lst_in):
        if len(FIELDS) != len(lst_in):
            return False
        else:
            for i in range(len(FIELDS)):
                setattr(self, FIELDS[i], lst_in[i])
            return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = [10, "Hello", 250]  # задаем список на проверку
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

print(result)
print(data.__dict__)
