Tools for converting .obj format meshes into vectrex32 basic files

obj-to-vx32
-----------

Usage: `obj-to-vx32 [configuration-file] [object-file] [object-name]`

Example: `obj-to-vx32 standard-configuration.py lightcycle-low.kob lightcycle`

Note that intensities dont yet work, but will soon ;).  Also, only tris or quads

Configuration file: See standard-config.py for example and descriptions of options

svg-to-vx32
-----------
usage `svg-to-vx32 [svgfile] [configuration-file] [object-name]`

Example: `svg-to-vx32 spiral.svg simple-config.py spiral`

Also no intensities yet....
This requires the svgpathtools python module - install it with `pip install svgpathtools`
