import xml.etree.ElementTree

# Write your code here.
formatstring = "{:<40}{:>10}{:>10}{:>10}{:>10}"
listings = xml.etree.ElementTree.parse('nyse.xml').getroot()
#listings[:] = sorted(listings, key=lambda q: q.text)
listings[:] = sorted(listings, key=lambda q: float(q.attrib['change']), reverse=True)
headers = []
for quote in listings.findall('quote'):
    company = quote.text
    if len(headers) == 0:
        headers = ['COMPANY']
        cols = [x.upper() for x in quote.attrib.keys()]
        headers.extend(cols)
        print(formatstring.format(*headers))
        print("-"*80)
    cols = [f"${float(x):7.3f}" for x in quote.attrib.values()]
    print(formatstring.format(quote.text,*cols))




# for car in cars_for_sale.findall('car'):
#     print('\t', car.tag)
#     for prop in car:
#         print('\t\t', prop.tag, end='')
#         if prop.tag == 'price':
#             print(prop.attrib, end='')
#     print(' =', prop.text)
