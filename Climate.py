from matplotlib import pyplot as plt

file = open("Global Temperatures 1880-2020.csv", "r")
data = file.readlines()

years = []
for line in data:
    years.append(int(line.split(',')[0]))

temp = []
for line in data:
    numlist = line.split(',')[1].split()
    num = float(''.join(numlist))
    temp.append(num)

plt.plot(years,temp)
plt.ylabel('temperature (C)')
plt.xlabel('years')
plt.show()
