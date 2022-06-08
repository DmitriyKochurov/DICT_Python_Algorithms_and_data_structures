from NotebookSpecification import asus, lenovo, hp, razer


class NotebookInfo(object):
    def __init__(self, manufacturer, model, screensize, CPU, memory, storage):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Screensize = screensize
        self.CPU = CPU
        self.Memory = memory
        self.Storage = storage


    def un_notebook(self):
        print(f"""Ноутбук производства {self.Manufacturer} {self.Model} с характеристиками: 
                    *Диагональ экрана: {self.Screensize}
                    *Процессор: {self.CPU}
                    *Кол-во оперативной памяти: {self.Memory}
                    *Кол-во памяти : {self.Storage} 
относится к бюджетной или бизнес линейки ноутбуков""")


    def notebook(self, line, segment):
        print(f"""Ноутбук производства {self.Manufacturer} {line} {self.Model} относится к {segment} серии с характеристиками: 
            *Диагональ экрана: {self.Screensize}
            *Процессор: {self.CPU}
            *Кол-во оперативной памяти: {self.Memory}
            *Кол-во памяти : {self.Storage} """)


    def get_info(self):
        line = str
        segment = str
        if len(str(self.Model).split()) == 1:
            if self.Manufacturer == "Asus":
                for i in asus.keys():
                    if str(self.Model).upper() in i:
                        line = asus.get(i)
                        break
                if line == str:
                    line = ""
            elif self.Manufacturer == "Lenovo":
                for i in lenovo.keys():
                    if str(self.Model).upper() in i:
                        line = lenovo.get(i)
                        break
                    if line == str:
                        line = ""
            elif self.Manufacturer == "HP":
                for i in hp.keys():
                    if str(self.Model).upper() in i:
                        line = hp.get(i)
                        break
                    if line == str:
                        line = ""
            elif self.Manufacturer == "Razer":
                for i in razer.keys():
                    if str(self.Model).upper() in i:
                        line = razer.get(i)
                        break
                    if line == str:
                        line = ""
            else:
                line = ""
        elif len(str(self.Model).split()) == 2:
            line, self.Model = str(self.Model).split()
        else:
            line = ""
        if line != "":
            if line[-1] == "7":
                segment = "игровой"
            elif line[-1] == "5":
                segment = "мультимедийный" or "бизнес"
            else:
                segment = "бюджетный"
        if line == "":
            self.un_notebook()
        else:
            self.notebook(line, segment)


if __name__ == "__main__":
    pc1 = NotebookInfo("Asus", "ZenBook OLED 13", "13.3", "Intel Core i5-1135G7", "16G", "512G SSD")
    pc2 = NotebookInfo("Lenovo", "Legion 5", "15.6", "Intel Core i5 - 10300H", "8G", "512G SSD")
    pc3 = NotebookInfo("HP", "OMEN 15", "15.6", "Ryzen 7 5800H", "16G", "512G SSD")
    pc4 = NotebookInfo("Razer", "Blade", "17", "Intel Core i7-12800H", "16G", "1000G SSD")
    pc5 = NotebookInfo("Asus", "ROG Strix G15", "15.6", "AMD Ryzen 7 6800H ", "8G", "512G SSD")
    