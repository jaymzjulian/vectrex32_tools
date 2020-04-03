include "small.bai"
include "explosion.bai"

' demo the explosion stuiff
call ScaleSprite(32)
call ReturnToOriginSprite()

' get the object
rose_object = rose()

' prepare the object for exploding - just expanding variables here for clarity :)
world_scale = 40
x_impulse = 2.5
y_impulse = 5.0
x_random = 1.0
y_random = 2.0
rose_explosion = prepare_explosion(2, rose_object, world_scale, {0,-400}, {x_impulse, y_impulse}, {x_random, y_random}, 9.8, -400, true)


' put it on the screen
f=LinesSprite(rose_explosion.dest)
call SpriteClip(f, {{-500, 500}, {500, -500}})
controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
last_time = GetTickCount()
start_time = GetTicKCount()
while controls[1,3] = 0
  call explode2d(rose_explosion)
  ' wait for next frame :)
  controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
endwhile

