import struct

STATUS_DELETED = 0
STATUS_REGULAR = 2

# todo: not implemented -> see https://gordthompson.github.io/ov2optimizer/ov2FileFormat.html for more detail
# STATUS_SKIPPER = 1
# STATUS_EXTENDED = 3


def serialize(lon, lat, label, status=STATUS_REGULAR):
    """
        Serialize to an ov2 record.

        Parameters
        ----------
        lon : float
            longitude in wgs84.
        lat : float
            latitude in wgs84.
        label : str
            poi label.
        label : int
            Choose from STATUS_DELETED = 0 or STATUS_REGULAR = 2.

        Returns
        -------
        bytes
            buffer of bytes representing one ov2 record.

        Examples
        --------
        >>> serialize(6.52223, 52.80967, 'my house')
        b'\x02\x16\x00\x00\x00\xbf\xf3\t\x00\xc7\x94P\x00my house\x00'
    """

    size = 14 + len(label)
    lon = int(lon * 100000)
    lat = int(lat * 100000)
    label = label.encode('utf8')
    buff = struct.pack(f'<B3i{len(label) + 1}s', status, size, lon, lat, label)
    return buff


def deserialize(buff):
    """
        Deserialize an ov2 record.

        Parameters
        ----------
        buff : bytes
            buffer of bytes representing one ov2 record.

        Returns
        -------
        tuple
            A tuple with: (lon, lat, label, status).

        Examples
        --------
        >>> deserialize(b'\x02\x16\x00\x00\x00\xbf\xf3\t\x00\xc7\x94P\x00my house\x00')
        (6.52223, 52.80967, 'my house', 2)
    """

    status, size, lon, lat, label = struct.unpack(f'<B3i{len(buff) - 14}sx', buff)
    lon /= 100000
    lat /= 100000
    label = label.decode()
    return lon, lat, label, status
