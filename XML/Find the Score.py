import xml.etree.ElementTree as ET

def get_attr_number(node):
    print(node.attrib, len(node.attrib), sep = ' : ')
    return len(node.attrib) + sum(get_attr_number(i) for i in node)


# 從檔案載入並解析 XML 資料
tree = ET.parse('input.xml')
root = tree.getroot()

# 從字串中取得並解析 XML 資料
print(get_attr_number(root))

'''
{} : 0
{'name': 'Liechtenstein'} : 1
{} : 0
{} : 0
{} : 0
{'name': 'Austria', 'direction': 'E'} : 2
{'name': 'Switzerland', 'direction': 'W'} : 2
{'name': 'Singapore'} : 1
{} : 0
{} : 0
{} : 0
{'name': 'Malaysia', 'direction': 'N'} : 2
{'name': 'Panama'} : 1
{} : 0
{} : 0
{} : 0
{'name': 'Costa Rica', 'direction': 'W'} : 2
{'name': 'Colombia', 'direction': 'E'} : 2
'''