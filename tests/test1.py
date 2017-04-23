
from colorit import ColorString

cs = ColorString("This is a test string")
rgb = (222, 55, 111)

print cs.color_front(rgb)
print cs.color_back(rgb)
print cs.bold()
print cs.under()
print cs.strike()
print cs.color_front(rgb).color_back(rgb)
print cs.color_front(rgb).bold()
print cs.color_front(rgb).under()
print cs.color_front(rgb).strike()
print cs.color_back(rgb).bold()
print cs.color_front(rgb).bold().strike().under()
