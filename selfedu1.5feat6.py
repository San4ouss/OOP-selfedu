class Graph:
    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        print(" ".join(map(str, self.data)) if self.is_show else "Отображение данных закрыто")

    def show_graph(self):
        print(f"Графическое отображение данных: {' '.join(map(str, self.data))}" if self.is_show
              else "Отображение данных закрыто")

    def show_bar(self):
        print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}" if self.is_show
              else "Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
