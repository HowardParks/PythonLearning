import xml.etree.ElementTree as ET

root = ET.Element('shop')
category = ET.SubElement(root, 'category',{'name':'Vegan Products'})
product1 = ET.SubElement(category,'product',{'name':'Good Morning Sunshine'})
type1 = ET.SubElement(product1,'type')
type1.text='cereal'
producer1 = ET.SubElement(product1,'producer')
producer1.text='OpenEDG Testing Service'
price1 = ET.SubElement(product1,'price')
price1.text="9.90"
currency1 = ET.SubElement(product1,'currency')
currency1.text='USD'
product2 = ET.SubElement(category,'product',{'name':'Spaghetti Veganietto'})
type2 = ET.SubElement(product2,'type')
type2.text='pasta'
producer2 = ET.SubElement(product2,'producer')
producer2.text='Programmers Eat Pasta'
price2 = ET.SubElement(product2,'price')
price2.text="15.49"
currency2 = ET.SubElement(product2,'currency')
currency2.text='EUR'
product3 = ET.SubElement(category,'product',{'name':'Ribeye Steak'})
type3 = ET.SubElement(product3,'type')
type3.text='meat'
producer3 = ET.SubElement(product3,'producer')
producer3.text='Open Minded Vegan Butcher Shop'
price3 = ET.SubElement(product3,'price')
price3.text="19.75"
currency3 = ET.SubElement(product3,'currency')
currency3.text='CAD'
tree = ET.ElementTree(root)
ET.dump(root)
tree.write('vegan.xml','UTF-8',True)
