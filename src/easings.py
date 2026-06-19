import math

# Linear
def Linear(t):
    return t

# Quadratic
def easeInQuad(t):
    return t * t

def easeOutQuad(t):
    return 1 - (1 - t) ** 2

def easeInOutQuad(t):
    return 2 * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 2 / 2

# Cubic
def easeInCubic(t):
    return t * t * t

def easeOutCubic(t):
    return 1 - (1 - t) ** 3

def easeInOutCubic(t):
    return 4 * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2

# Quartic
def easeInQuart(t):
    return t * t * t * t

def easeOutQuart(t):
    return 1 - (1 - t) ** 4

def easeInOutQuart(t):
    return 8 * t * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 4 / 2

# Quintic
def easeInQuint(t):
    return t * t * t * t * t

def easeOutQuint(t):
    return 1 - (1 - t) ** 5

def easeInOutQuint(t):
    return 16 * t * t * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 5 / 2

# Sine
def easeInSine(t):
    return 1 - math.cos((t * math.pi) / 2)

def easeOutSine(t):
    return math.sin((t * math.pi) / 2)

def easeInOutSine(t):
    return -(math.cos(math.pi * t) - 1) / 2

# Exponential
def easeInExpo(t):
    return 0 if t == 0 else 2 ** (10 * t - 10)

def easeOutExpo(t):
    return 1 if t == 1 else 1 - 2 ** (-10 * t)

def easeInOutExpo(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return 2 ** (20 * t - 10) / 2
    else:
        return (2 - 2 ** (-20 * t + 10)) / 2

# Circular
def easeInCirc(t):
    return 1 - math.sqrt(1 - t ** 2)

def easeOutCirc(t):
    return math.sqrt(1 - (t - 1) ** 2)

def easeInOutCirc(t):
    if t < 0.5:
        return (1 - math.sqrt(1 - (2 * t) ** 2)) / 2
    else:
        return (math.sqrt(1 - (-2 * t + 2) ** 2) + 1) / 2

# Back
def easeInBack(t):
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * t * t * t - c1 * t * t

def easeOutBack(t):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

def easeInOutBack(t):
    c1 = 1.70158
    c2 = c1 * 1.525
    if t < 0.5:
        return ((2 * t) ** 2 * ((c2 + 1) * 2 * t - c2)) / 2
    else:
        return ((2 * t - 2) ** 2 * ((c2 + 1) * (t * 2 - 2) + c2) + 2) / 2

# Elastic
def easeInElastic(t):
    c4 = (2 * math.pi) / 3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return -(2 ** (10 * t - 10)) * math.sin((t * 10 - 10.75) * c4)

def easeOutElastic(t):
    c4 = (2 * math.pi) / 3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return 2 ** (-10 * t) * math.sin((t * 10 - 0.75) * c4) + 1

def easeInOutElastic(t):
    c5 = (2 * math.pi) / 4.5
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return -(2 ** (20 * t - 10) * math.sin((20 * t - 11.125) * c5)) / 2
    else:
        return (2 ** (-20 * t + 10) * math.sin((20 * t - 11.125) * c5)) / 2 + 1

# Bounce
def easeOutBounce(t):
    n1 = 7.5625
    d1 = 2.75
    if t < 1 / d1:
        return n1 * t * t
    elif t < 2 / d1:
        return n1 * (t - 1.5 / d1) * (t - 1.5 / d1) + 0.75
    elif t < 2.5 / d1:
        return n1 * (t - 2.25 / d1) * (t - 2.25 / d1) + 0.9375
    else:
        return n1 * (t - 2.625 / d1) * (t - 2.625 / d1) + 0.984375

def easeInBounce(t):
    return 1 - easeOutBounce(1 - t)

def easeInOutBounce(t):
    if t < 0.5:
        return (1 - easeOutBounce(1 - 2 * t)) / 2
    else:
        return (1 + easeOutBounce(2 * t - 1)) / 2
