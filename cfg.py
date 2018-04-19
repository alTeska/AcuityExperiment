PATH = 'module/assets/'

# Texture settings
SIZEX = 10000
SIZEY = 10000
SCALE = 25
CYLINDER_TEXTURE = PATH + 'sin_stripes.png'
DPI = 500

# Experiment settings
CYLINDER_POSITION = 0, 0, -2
CYLINDER_SPEEDS = 9., 14.
CYLINDER_ROTATION_X = 90

PHASE_DURATION_SECS = 5.
WAIT_DURATION_SECS = 2
START_TIME = 2

SEQ = None

SEQ = update_attribute(cylinder, 'visible', False),
    wait_duration(START_TIME),
    update_attribute(cylinder, 'visible', True),
    update_attribute(cylinder, 'speed', 10),
    wait_duration(PHASE_DURATION_SECS),
