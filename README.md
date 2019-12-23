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

Notes: 
 * Some svg are actually filled outlines - we, of course, do not handle these usefully :).  In inkscape, you can use the "Centre Line Trace" plugin to fix these - see https://github.com/fablabnbg/inkscape-centerline-trace

 * It can output either a function that generates a display list (for things like title screens and such) or a arrray of commands (for movable sprites and such) - see the rose and spiral examples for details of this

 * There are a bunch of object types currently unimplemented, msotly because of what inkscape outputs - specifically, I haven't done arcs yet.  They "generally will work" once I find an SVG that has them though - the library i'm using supports them, i just haven't hooked it up.

 * It can optimize for either a certain amount of error (say, no more than 0.1 "units"), or a certain amount of vectors (i.e. no more than 512 vectors - which is, btw, approximatly what ends up fitting in DP ram, at least 768 fails for me)

 * If you're importing complex objects, which have a lot of pen drift, the static function variant supports calling ReturnToOrigin every N commands.  Without this, the rose example looks absolutely terrible and jumps all over the place, though the spiral is weirdly fine.

 * I need to improve the MoveTo optimization just a little more - it tries to pick "near origin" as the first thing, but really it should pick "Thing that causes the least MoveTo commands".  I'll probably update that in github soon.
