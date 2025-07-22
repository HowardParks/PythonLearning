import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('movies.xml', 'UTF-8', True)

root = ET.Element('data')
ET.SubElement(root,'movie',{'title':'Le Petit Prince','rate':'4'})
ET.SubElement(root, 'movie', {'title':'The Princess Bride','rate':'32'})
ET.dump(root)
tree = ET.ElementTree(root)
tree.write('temp.xml', 'UTF-8', True)
