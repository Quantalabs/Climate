import urllib

URL = 'https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt'
"""
Land-Ocean Temperature Index (C)
--------------------------------

Year No_Smoothing  Lowess(5)
----------------------------
1880     -0.16     -0.08
1881     -0.07     -0.12
1882     -0.10     -0.16
yyyy     (-)#.##   (-)#.##
"""

file = urllib.request.urlopen(URL)
decoded_file = []

for line in file[5:]:
    decoded_line = line.decode("utf-8")
    decoded_file.append(decoded_line)

tsv_save = open('data/nasa-climate-data.tsv', 'w+')
tsv_save.writelines(decoded_file)

print('Process complete: ')
print('Data obtained from nasa.gov and saved to .tsv')
print('See data/nasa-climate-data.tsv')
