import xml.etree.ElementTree as ET
from TempConverter import TempConverter

class ForecastParser:
    def parse(self):
        self.tree = ET.parse('C://Users/Owner/PycharmProjects/PythonLearning/FileClassLab/forecast.xml')
        self.root = self.tree.getroot()
        self.tc = TempConverter()
        for item in self.root:
            c = int(item[1].text)
            print(f"{item[0].text}: {c} Celsius, {self.tc.c_to_f(c)} Fahrenheit")

if __name__ == '__main__':
    fp = ForecastParser()
    fp.parse()
