import pygame
import pygame.locals
import logging
class Plansza():

    def __init__(self, width):
        self.surface = pygame.display.set_mode((width, width), 0, 32)
        pygame.display.set_caption('Kolko_i_krzyzyk')

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

        self.znacznik = [None] * 9

    def rysuj(self, *args):
        background = (0, 0, 0)
        self.surface.fill(background)
        self.rysujsiatke()
        self.rysujznaczniki()
        self.napiszwynik()
        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.update()

    def rysujsiatke(self):
        color = (255, 255, 255)
        width = self.surface.get_width()
        for i in range(1, 3):
            pos = width / 3 * i
            pygame.draw.line(self.surface, color, (0, pos), (width, pos), 1)
            pygame.draw.line(self.surface, color, (pos, 0), (pos, width), 1)

    def ruchgracza(self, x, y):
        rozmiarkomorki = self.surface.get_width() / 3
        x /= rozmiarkomorki
        y /= rozmiarkomorki
        self.znacznik[int(x) + int(y) * 3] = znacznikgracza(True)

    def rysujznaczniki(self):
        box_side = self.surface.get_width() / 3
        for x in range(3):
            for y in range(3):
                znacznik = self.znacznik[x + y * 3]
                if not znacznik:
                    continue
                srodekx = x * box_side + box_side / 2
                xrodeky = y * box_side + box_side / 2

                self.teksty(self.surface, znacznik, (srodekx, xrodeky))

    def teksty(self, surface, tekst, center, color=(180, 180, 180)):

        tekst = self.font.render(tekst, True, color)
        kat = tekst.get_rect()
        kat.center = center
        surface.blit(tekst, kat)

    def napiszwynik(self):
        if check_win(self.znacznik, True):
            wynik = u"Wygrałeś(aś)"
        elif check_win(self.znacznik, True):
            wynik = u"Przegrałeś(aś)"
        elif None not in self.znacznik:
            wynik = u"Remis!"
        else:
            return

        i = self.surface.get_width() / 2
        self.teksty(self.surface, wynik, center=(i, i), color=(255, 26, 26))


class Kolka_i_krzyzyk():


    def __init__(self, width, ai_turn=False):

        pygame.init()
        self.fps_clock = pygame.time.Clock()

        self.plansza = Plansza(width)
        self.ai = Ai(self.plansza)
        self.ai_turn = ai_turn

    def Glowna_petla(self):
        while not self.abysieprogramniewywalil():
            self.plansza.rysuj()
            if self.ai_turn:
                self.ai.wykonajruch()
                self.ai_turn = False
            self.fps_clock.tick(15)

    def abysieprogramniewywalil(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if self.ai_turn:
                    continue
                x, y = pygame.mouse.get_pos()
                self.plansza.ruchgracza(x, y)
                self.ai_turn = True


class Ai():
    def __init__(self, plansza):
        self.plansza = plansza

    def wykonajruch(self):
        if not None in self.plansza.znacznik:
            # brak dostępnych ruchów
            return
        move = self.nastepnyruch(self.plansza.znacznik)
        self.plansza.znacznik[move] = znacznikgracza(False)

    @classmethod
    def nastepnyruch(cls, znacznik):
        ruch = cls.mozliweruchy(znacznik, False)
        wynik,ruch = max(ruch, key=lambda m: m[0])
        logging.info("Dostępne ruchy: %s", ruch)
        logging.info("Wybrany ruch: %s %s", ruch, wynik)
        return ruch

    @classmethod
    def mozliweruchy(cls, markers, x_player):
        available_moves = (i for i, m in enumerate(markers) if m is None)
        for move in available_moves:
            from copy import copy
            mozliwosc = copy(markers)
            mozliwosc[move] = znacznikgracza(x_player)

            if check_win(mozliwosc, x_player):
                score = -1 if x_player else 1
                yield score, move
                continue
            next_moves = list(cls.mozliweruchy(mozliwosc, not x_player))
            if not next_moves:
                yield 0, move
                continue

            scores, ruch = zip(*next_moves)
            yield sum(scores), move


def znacznikgracza(x_player):
    return "X" if x_player else "O"


def check_win(znacznik, x_player):
    win = [znacznikgracza(x_player)] * 3
    seq = range(3)

    def znacznikk(xx, yy):
        return znacznik[xx + yy * 3]

    for x in seq:
        row = [znacznikk(x, y) for y in seq]
        if row == win:
            return True

    for y in seq:
        col = [znacznikk(x, y) for x in seq]
        if col == win:
            return True

    diagonal1 = [znacznikk(i, i) for i in seq]
    diagonal2 = [znacznikk(i, abs(i-2)) for i in seq]
    if diagonal1 == win or diagonal2 == win:
        return True

if __name__ == "__main__":
    game = Kolka_i_krzyzyk(300)
    game.Glowna_petla()
