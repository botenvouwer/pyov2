from pyov2 import ov2
from pyov2.file import read_ov2, ov2_to_csv, list_to_ov2

path = "C:\\Users\\wloosma2\\OneDrive - Enexis productie\\desktop\\opendata\\poi\\"
csv_path = path + "test_3.csv"
ov2_path = path + "Verdeelkast_test.ov2"

buff = ov2.serialize(5.26360870, 51.70043380, 'MDR.004240 , Schoonloërweg t/o 17 , Schoonloerweg , 17 , 9442 PL , ELP')
back = ov2.deserialize(buff)


print(buff)
print(back)


poi_list = [
    # (5.77623, 51.65313, 'MDR.004240 , Schoonloerweg to 17 , Schoonloerweg , 17 , 9442 PL , ELP')
    (5.77623, 51.65313, 'MDR.004240 , Schoonloërweg t/o 17 , Schoonloerweg , 17 , 9442 PL , ELP')
]

list_to_ov2(poi_list, path + 'debug_1.ov2')

# csv_to_ov2(csv_path, ov2_path)

# t = read_ov2(ov2_path)
# print(t)

# ov2_to_csv(ov2_path, csv_path)

import pyov2
