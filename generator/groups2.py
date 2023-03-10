#
#
# testdata = [Group(group_name="", header_name="", footer_name="")] + [
#     Group(group_name=random_string("", 15), header_name=random_string("", 15), footer_name=random_string("", 15))
#     for i in range(n)
# ]

from comtypes.client import CreateObject
import os
import random
import string
import os.path


# def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_group_id(prefix, length):
    return prefix + "".join([random.choice(string.digits) for i in range(length)])
    # Let us assume we generate groups with data in the following format:
    # Name:   N73058
    # Header: H55399
    # Footer: F03216


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.WorkBooks.Add()

xl.Range["A1"].Value[()] = "Name"
xl.Range["B1"].Value[()] = "Header"
xl.Range["C1"].Value[()] = "Footer"

for i in range(3):
    xl.Range["A%s" % (i+2)].Value[()] = random_group_id("N", 5)
    xl.Range["B%s" % (i+2)].Value[()] = random_group_id("H", 5)
    xl.Range["C%s" % (i+2)].Value[()] = random_group_id("F", 5)
wb.SaveAs(os.path.join(project_dir, "groups2.xlsx"))
xl.Quit()

# for i in range(10):
#     xl.Range["A%s" % (i+1)].Value[()] = "group %s" % i
# wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
# xl.Quit()
