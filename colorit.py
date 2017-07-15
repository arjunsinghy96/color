# Copyright(c) 2017 Arjun Singh Yadav

RESET = '\033[0m'

ATTR = { 'bold' : '\033[1m',
         'underline' : '\033[4m',
         'strike' : '\033[9m' 
         }

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
STRIKE = "\033[9m"

class ColorText(str):

    def __init__(self, text=None):
        self.text = text
        self.decorated = text

    def color_front(self, colorname=None, rgb=None, hexvalue=None):
        if not (colorname or rgb or hexvalue):
            raise Exception("Please specify a color parameter")
        if colorname:
            rgb = str_to_rgb(colorname)
        if hexvalue:
            rgb = hex_to_rgb(hexvalue)
        red, green, blue = rgb
        foreground = '\033[38;2;{r};{g};{b}m'.format(r=red, g=green, b=blue)
        self.decorated = foreground + self.decorated + RESET
        return ColorText(self.decorated)

    def color_back(self, colorname=None, rgb=None, hexvalue=None):
        if not (colorname or rgb or hexvalue):
            raise Exception("Please specify a color parameter")
        if colorname:
            rgb = str_to_rgb(colorname)
        if hexvalue:
            rgb = hex_to_rgb(hexvalue)
        red, green, blue = rgb
        background = '\033[48;2;{r};{g};{b}m'.format(r=red, g=green, b=blue)
        self.decorated = background + self.decorated + RESET
        return ColorText(self.decorated)

    def bold(self):
        self.decorated = BOLD + self.text + RESET
        return ColorText(self.decorated)

    def underline(self):
        self.decorated = UNDERLINE + self.decorated + RESET
        return ColorText(self.decorated)

    def strike(self):
        self.decorated = STRIKE + self.decorated + RESET
        return ColorText(self.decorated)

    def __unicode__(self):
        return self.decorated

    def __str__(self):
        return self.decorated

    def raw(self):
        return self.decorated


def color_front(text, red, green, blue):
    """
    wraps the text in appropriate ANSI escape code for foreground color
    param text: text to be colored
    param red: R of RGB value
    param green: G of RGB value
    param blue: B of RGB value

    return: text wrapped in ANSI escape code
    """
    foreground = '\033[38;2;{r};{g};{b}m'.format(r=red, g=green, b=blue)
    text = foreground + text + RESET
    return text

def color_back(text, red, green, blue):
    """
    param text: text for which background is to be set
    param red: R of RGB value
    param green: G of RGB value
    param blue: B of RGB value
    
    return: text wrapped in ANSI escape code for background
    """
    background = '\033[48;2;{r};{g};{b}m'.format(r=red, g=green, b=blue)
    text = background + text + RESET
    return text

def bold(msg):
    """
    param msg: text to be made bold

    return: text wrapped in ANSI escape code for bold
    """
    return ATTR['bold'] + msg + RESET

def under(msg):
    """
    param msg: text to be underlined

    return: text wrapped in ANSI escape code for underline
    """
    return ATTR['underline'] + msg + RESET

def strike(msg):
    """
    param msg: text to be strikethrough

    return: text wrapped in ANSI escape code for strikethrough
    """
    return ATTR['strike'] + msg + RESET
