#Copy Tables from Website and print out

import pandas as pd

url = input("Enter the URL of the table you want to copy: ")

table = pd.read_html(url)


if len(table) == 1:
    print("There is " + str(len(table)) + " table on this page.")
else:
    print("There are " + str(len(table)) + " tables on this page.")

result = input("Type the number of the table you want to copy: ")

print(table[int(result)])