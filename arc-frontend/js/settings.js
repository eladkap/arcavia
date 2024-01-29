/* Game Physics */
const GRAVITY = 0.1;
const IMAGE_SCALE = 0.2;
const MOVEMENT_UNITS = 5;
const ANGLE_OFFSET = -Math.PI / 2;
const ANGLE_OFFSET_REVERSED = Math.PI / 2;
const FRICTION = 0.95;

/* Game Graphics */

/* Fonts */
const FONT_FAMILY = 'consolas';
const FONTS_SIZE_S = '16';
const FONTS_SIZE_M = '24';
const FONTS_SIZE_L = '32';

/* Spaceship */

/** Bubbles */
const BUBBLES_NUM = 10;
const BUBBLE_MAX_VELOCITY = 4;
const BUBBLE_RADIUS = 30;

/* Colors */
const COLORS = [
    'rgb(255, 50, 50)',
    'rgb(50, 255, 50)',
    'rgb(50, 50, 255)',
    'rgb(127, 0, 255)',
    'rgb(200, 100, 0)',
    'rgb(255, 100, 255)'
]

/* Raptor */
const RAPTOR_POS_X = window.innerWidth * 0.5;
const RAPTOR_POS_Y = window.innerHeight * 0.8;
const RAPTOR_ALTITUDE = 100;
const RAPTOR_HEALTH = 1000;
const RAPTOR_SHIELD = 0;
const RAPTOR_ACC = 0.7;
const RAPTOR_BOOST_ACC = 1;
const RAPTOR_MAX_SPEED = 8;
const RAPTOR_MAX_BOOST_SPEED = 10;
const ROTATE_ACC = 0.1;
const MAX_ROTATE = 1;
const RAPTOR_FRICTION = 0.95;

/* Bullet */
const BULLET_SPEED = 20;
const BULLET_RADIUS = 3;
const BULLET_INTERVAL = 500;
const BULLET_DAMAGE = 5;
const BULLET_COLOR = 'rgba(255,100,100,1)';

/* Rocket */
const ROCKET_SPEED = 10;
const ROCKET_RADIUS = 5;
const ROCKET_HEIGHT = 30;
const ROCKET_DAMAGE = 30;
const ROCKET_COLOR = 'rgba(100,100,255,1)';

/* Enablers */
var ALLOW_SOUND = false;
