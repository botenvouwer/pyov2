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

    import 