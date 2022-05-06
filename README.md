# pyov2
This module can serialize and deserialize in ov2 binary format.
With special thanks to [@mikewatt](https://gis.stackexchange.com/questions/430326/how-to-generate-ov2-poi-programmatically-from-csv-source/430342#430342) for providing guidance.

# ov2 format
ov2 is a point of interest file, also referred to as poi file.
These files store (as the names says) points of interest based on their wgs84 coordinates and label.
You can load ov2 files in tomtom devices to navigate to your own points of interest.

For more info on the format read [this page](https://gordthompson.github.io/ov2optimizer/ov2FileFormat.html).

# Usage
You can use `ov2` and `file` submodules to handle ov2 format. 
The `ov2` module can serialize and deserialize ov2 binary format.
The `file` module can walk through an ov2 file using a callback. 
And it can convert csv, write and read ov2 files.

## Examples

### Write list to ov2

    from pyov2.file import list_to_ov2
    
    poi_list = [
        (5.77674, 51.65315, 'Moms house'),
        (5.77643, 51.65312, 'My house'),
        (5.77623, 51.65313, 'Mats house')
    ]
    
    list_to_ov2(poi_list, 'houses.ov2')

### Convert csv to ov2

    from pyov2.file import ov2_to_csv

    csv_path = "houses.csv"
    ov2_path = "houses.ov2"
    csv_to_ov2(csv_path, ov2_path)
