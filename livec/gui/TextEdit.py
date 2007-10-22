import pygame
from Widget import Widget

class TextStyle(object):
    def __init__(self, color, font_size, font_name):
        self.color=color
        self.font_size=font_size
        self.font_name=font_name


class TextEdit(Widget):
    def __init__(self, style, get_text, set_text=None):
        self.get_text = get_text
        self.set_text = set_text
        self.color = style.color
        self._font = pygame.font.Font(style.font_name, style.font_size)

        # TODO: Debugging hack, remove
        import traceback
        self.creator = traceback.format_stack()

    def size(self):
        def func(line, cur_height):
            return self._font.size(line)
        return self._do(func)
    
    def draw(self, surface, pos):
        def func(line, cur_height):
            text_surface = self._font.render(line, True, self.color)
            surface.blit(text_surface, (pos[0], pos[1]+cur_height))
            return text_surface.get_size()
        self._do(func)

    def _do(self, func):
        text = self.get_text()
        size = [0, 0]
        for line in text.split('\n'):
            twidth, theight = func(line, size[1])
            size[0] = max(size[0], twidth)
            size[1] += theight
        return size

def make_label(text, **kw):
    return TextEdit(lambda : text, **kw)
