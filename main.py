from Version import Versions

version1 = Versions('1.2.2.3.4.5')
version2 = Versions('1.2.1.3.4.5')


version1 = Versions('1.2.2.3.4.5')
version2 = Versions('1.2.2.3.4.5')

print(version1.compare(version2))
print(version2.compare(version1))

version1 = Versions('1.2.2.3.4.5')
version2 = Versions('1.2.1.3.4.5.3.3.3')

print(version1.compare(version2))
print(version2.compare(version1))

version1 = Versions('1.2.2.3.4.5')
version2 = Versions('1.2.2.3.4.5.3.3.3')

print(version1.compare(version2))
print(version2.compare(version1))


version1 = Versions('1.2.2.3.4.5')
version2 = Versions('1.2.2.3.4.5')

print(version1.compare(version2))
print(version2.compare(version1))
from LRU import LRU
