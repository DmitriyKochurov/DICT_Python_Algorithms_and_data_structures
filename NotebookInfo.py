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
    Business = NotebookInfo("Asus", "ZenBook OLED 13", "13.3'", "Intel Core I5-1135G7", "16 Gb", "512 Gb SSD")
    Business.get_info()
    