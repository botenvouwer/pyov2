import csv
import struct

import ov2

# Dialect used in the netherlands, so yeah I use this as default
csv.register_dialect('semicolon', delimiter=';')


def csv_to_ov2(csv_path, ov2_path, skip_header=True, dialect='semicolon'):

    if not ov2_path.endswith('.ov2'):
        ov2_path += '.ov2'

    with open(csv_path, 'r', newline='') as in_file:
        with open(ov2_path, 'wb') as target_file:
            reader = csv.reader(in_file, dialect=dialect)

            if skip_header:
                next(reader)

            for row in reader:
                longitude = float(row[0])
                latitude = float(row[1])
                label = row[2]

                buff = ov2.serialize(longitude, latitude, label.strip())
                target_file.write(buff)


def list_to_ov2(ov2_list, ov2_path):

    if not ov2_path.endswith('.ov2'):
        ov2_path += '.ov2'

    with open(ov2_path, 'wb') as target_file:

        for row in ov2_list:
            longitude = row[0]
            latitude = row[1]
            label = row[2]
            status = row[3]

            buff = ov2.serialize(longitude, latitude, label.strip(), status)
            target_file.write(buff)


def ov2_to_csv(ov2_path, csv_path, headers=('longitude', 'latitude', 'label'), dialect='semicolon'):
    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f, dialect=dialect)

        if headers is not None:
            w.writerow(headers)

        walk_ov2(ov2_path, lambda r: w.writerow((r[0], r[1], r[2])))


def read_ov2(ov2_path):
    res = []
    walk_ov2(ov2_path, lambda r: res.append(r))
    return res


def walk_ov2(ov2_path, callback):
    try:
        with open(ov2_path, "rb") as f:

            buff_head = f.read(5)
            while buff_head:
                status, size = struct.unpack(f'<Bi', buff_head)

                buff_body = f.read(size - 5)
                buff = buff_head + buff_body
                row = ov2.deserialize(buff)

                callback(row)

                buff_head = f.read(5)
    except IOError:
        print('Could not open ov2 file')
