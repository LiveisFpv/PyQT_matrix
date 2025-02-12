from views.main_window import MainWindow
from models.matrix import Matrix
class MainController:
    def __init__(self, view:MainWindow, model:Matrix):
        self.view = view
        self.model = model
        self.view.calculate.clicked.connect(self.on_button_click_calculate)

    def on_button_click_calculate(self):
        data = self.model.get_matrixs()  # Получаем данные из модели
        print(data)