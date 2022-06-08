from NotebookSpecification import asus, lenovo, hp, razer


class NotebookInfo(object):
    def __init__(self, manufacturer, model, screensize, CPU, memory, storage):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Screensize = screensize
        self.CPU = CPU
        self.Memory = memory
        self.Storage = storage

    def get_info(self):
        pass


if __name__ == "__main__":
    pc1 = NotebookInfo("Asus", "ZenBook OLED 13", "13.3", "Intel Core i5-1135G7", "16G", "512G SSD")
    pc2 = NotebookInfo("Lenovo", "Legion 5", "15.6", "Intel Core i5 - 10300H", "8G", "512G SSD")
    pc3 = NotebookInfo("HP", "OMEN 15", "15.6", "Ryzen 7 5800H", "16G", "512G SSD")
    pc4 = NotebookInfo("Razer", "Blade", "17", "Intel Core i7-12800H", "16G", "1000G SSD")
    pc5 = NotebookInfo("Asus", "ROG Strix G15", "15.6", "AMD Ryzen 7 6800H ", "8G", "512G SSD")
    