OUTPUT_TYPE_FUNCTION = 1
OUTPUT_TYPE_COMMANDS = 2
 
# These are the tunables - this will cause the item to be exactly x * y
target_size_x = 512
target_size_y = 512
# Set target_commands to something super high is you just want to set acceptable_error
# So if you want "no more than N vectors", set target_coomands and acceptable_error to 0.0
# 
# If you want "no more than N error", set target_commands to 0, and acceptable_error to some other value
target_commands = 512
acceptable_error = 0.0
#max_acceptable = 1.0

# This is in radians...
angle_error = 0.01

# OUTPUT_TYPE_COMMANDS just outputs a set of commands
# OUTPUT_TYPE_FUNCTION outputs a function
# The difference is, OUTPUT_TYPE_COMMANDS can call return to origin from time to time, but OUTPUT_TYPE_FUNCTION
# cannot
output_type = OUTPUT_TYPE_COMMANDS
origin_return_commands = 64

