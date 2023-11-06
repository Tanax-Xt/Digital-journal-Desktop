
import matplotlib

matplotlib.use("QtAgg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Chart(FigureCanvas):
    def __init__(self, model, db, width=6, height=4, dpi=100):
        self.model = model
        self.db = db
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(Chart, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def marks(self):
        all_subjs = sorted(map(lambda x: x[0], self.db.subjs_list()))
        marks = []
        subjs = []
        bar_labels = []
        bar_colors = []

        for column in range(1, len(all_subjs) + 1):
            mark = self.model.index(1, column).data()
            if mark is not None:
                mark = float(mark)
                if mark < 3:
                    bar_colors.append('tab:red')
                    bar_labels.append('2-3' if '2-3' not in bar_labels else '_2-3')
                elif 3 <= mark < 4:
                    bar_colors.append('tab:orange')
                    bar_labels.append('3-4' if '3-4' not in bar_labels else '_3-4')
                else:
                    bar_colors.append('tab:green')
                    bar_labels.append('4-5' if '4-5' not in bar_labels else '_4-5')

                subjs.append(all_subjs[column - 1])
                marks.append(mark)

        self.axes.bar(subjs, marks, label=bar_labels, color=bar_colors)
        self.axes.set_ylabel('Оценки')
        self.axes.set_title('Успеваемость')
        self.axes.legend(title='Легенда')
