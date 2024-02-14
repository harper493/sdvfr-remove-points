This little script removes the detailed annotations from a KML file created by the
SDVFR French VFR navigation app. These are valuable information but when 
superimposed on the IGN geoportail maps, they clutter it up so much you can't
read anything.

To use it, download the code (remove-points.py) and run it as:

python3 remove-points.py <kml file name>

Note that the file is rewritten - if you want to keep the original, copy it
to some other place first.
