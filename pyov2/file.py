import csv
import struct

# Dialect used in the netherlands, so yeah I use this as default
from pyov2 import ov2

csv.register_dialect('semicolon', delimiter=';')


def csv_to_ov2(csv_path, ov2_path, skip_header=True, dialect='semicolon'):
    """
        Convert a csv to an ov2 file.
        The csv should consist of three columns.
        The columns wil be interpreted like: (longitude, latitude, label).
        Use dialect parameter to fit your csv.

        Parameters
        ----------
        csv_path : str
            Path of csv file to convert.
        ov2_path : str
            Path where to save ov2 file.
        skip_header : bool
            If the csv contains headers use True (default) otherwise use False.
        dialect : str
            Default is 'semicolon' but you can use 'excel' for comma seperated csv.
    """

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
    """
        Save list to ov2 file.

        Parameters
        ----------
        ov2_list : list
            List with poi tuples.
            Tuple should have this structure: (longitude, latitude, label, status)
        ov2_path : str
            Path of ov2 file to write.
    """

    if not ov2_path.endswith('.ov2'):
        ov2_path += '.ov2'

    with open(ov2_path, 'wb') as target_file:

        for row in ov2_list:
            longitude = row[0]
            latitude = row[1]
            label = row[2]
            status = row[3] if len(row) > 3 in row else ov2.STATUS_REGULAR

            buff = ov2.serialize(longitude, latitude, label.strip(), status)
            target_file.write(buff)


def ov2_to_csv(ov2_path, csv_path, headers=('longitude', 'latitude', 'label'), dialect='semicolon'):
    """
        Convert an ov2 to a csv file.
        Use dialect parameter to fit your csv standard.

        Parameters
        ----------
        ov2_path : str
            Path of ov2 file to convert.
        csv_path : str
            Path where to save csv file.
        headers : tuple
            Default: ('longitude', 'latitude', 'label').
            Use None to skip headers.
        dialect : str
            Default is 'semicolon' but you can use 'excel' for comma seperated csv.
    """

    with open(csv_path, 'w', newline='') as f:
        w = csv.writer(f, dialect=dialect)

        if headers is not None:
            w.writerow(headers)

        walk_ov2(ov2_path, lambda r: w.writerow((r[0], r[1], r[2])))


def read_ov2(ov2_path):
    """
        Reads in an ov2 file as a list with tuples.

        Parameters
        ----------
        ov2_path : str
            Path of ov2 file to read.
    """

    res = []
    walk_ov2(ov2_path, lambda r: res.append(r))
    return res


def walk_ov2(ov2_path, callback):
    """
            Walks an ov2 file returning the records to callback function.

            Parameters
            ----------
            ov2_path : str
                Path of ov2 file to read.
            callback : function
                A function that will be called for each record found in ov2 file.
                The function is called with a tuple as first paramer.
                Tuple looks like: (longitude, latitude, label, status).

            Examples
            --------
            >>> walk_ov2('poi.ov2', lambda r: print(r))
        """

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
