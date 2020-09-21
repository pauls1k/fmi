import time
import sys

import pygame, sys
n=5
def elem_identice(lista):
    mt = set(lista)
    if (len(mt) == 1):
        castigator = list(mt)[0]
        if castigator != Joc.GOL:
            return castigator
        else:
            return False
    else:
        return False


def deseneaza_grid(display, tabla):
    w_gr = h_gr = 100

    x_img = pygame.image.load('ics.png')
    x_img = pygame.transform.scale(x_img, (w_gr, h_gr))
    zero_img = pygame.image.load('zero.png')
    zero_img = pygame.transform.scale(zero_img, (w_gr, h_gr))
    drt = []
    for ind in range(len(tabla)):
        linie = ind // n
        coloana = ind % n
        patr = pygame.Rect(coloana * (w_gr + 1), linie * (h_gr + 1), w_gr, h_gr)
        print(str(coloana * (w_gr + 1)), str(linie * (h_gr + 1)))
        drt.append(patr)
        pygame.draw.rect(display, (255, 255, 255), patr)
        if tabla[ind] == 'x':
            display.blit(x_img, (coloana * w_gr, linie * h_gr))
        elif tabla[ind] == '0':
            display.blit(zero_img, (coloana * w_gr, linie * h_gr))
    pygame.display.flip()
    return drt


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    JMIN = None
    JMAX = None
    GOL = '#'

    def __init__(self, tabla=None):
        self.matr = tabla or [self.__class__.GOL] * n*n

    def final(self):
        rez = []
        for x in range(n):
            for y in range(n-2):
                if elem_identice(self.matr[x * n + y:x * n + y + 3:1]):
                    rez.append(elem_identice(self.matr[x * n + y:x * n + y + 3:1]))

        for y in range(n):
            for x in range(n-2):
                if elem_identice(self.matr[x * n + y:x * n + y+3*n:n]):
                    rez.append(elem_identice(self.matr[x * n + y:x * n + y+3*n:n]))

        for x in range(n-2):
            for y in range(n-2):
                if elem_identice(self.matr[x * n + y:x * n + y+3*n+2:n+1]):
                    rez.append(elem_identice(self.matr[x * n + y:x * n + y+3*n+2:n+1]))

        for x in range(n-2):
            for y in reversed(range(2,n)):
                if elem_identice(self.matr[x * n + y:x * n + y+3*n-4:n-1]):
                    rez.append(elem_identice(self.matr[x * n + y:x * n + y+3*n-4:n-1]))


        if len(rez)==1:
            return rez[0]
        elif self.__class__.GOL not in self.matr:
            return 'remiza'
        else:
            return False

    def mutari(self, jucator_opus):
        l_mutari = []
        for i in range(len(self.matr)):
            if self.matr[i] == self.__class__.GOL:
                matr_tabla_noua = list(self.matr)
                p=False
                for j in range(len(self.matr)):
                    if self.matr[j]==jucator_opus:
                        p=True
                if p:
                    if i == 0:
                        if (self.matr[i+1] == jucator_opus or
                                self.matr[i+n] == jucator_opus or
                                self.matr[i+n+1] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i==n*n-1:
                        if (self.matr[i - 1] == jucator_opus or
                                self.matr[i - n] == jucator_opus or
                                self.matr[i - n - 1] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i==n-1:
                        if (self.matr[i - 1] == jucator_opus or
                                self.matr[i + n - 1] == jucator_opus or
                                self.matr[i + n] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i==n*n-n:
                        if (self.matr[i + 1] == jucator_opus or
                                self.matr[i - n] == jucator_opus or
                                self.matr[i - n - 1] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i>0 and i<n-1:
                        if (self.matr[i - 1] == jucator_opus or
                                self.matr[i + 1] == jucator_opus or
                                self.matr[i + n - 1] == jucator_opus or
                                self.matr[i + n] == jucator_opus or
                                self.matr[i + n + 1] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i<n*n-1 and i>n*n-n+1:
                        if (self.matr[i - 1] == jucator_opus or
                                self.matr[i + 1] == jucator_opus or
                                self.matr[i - n + 1] == jucator_opus or
                                self.matr[i - n] == jucator_opus or
                                self.matr[i - n - 1] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i+1%n==0 and i!=n-1 and i!=n*n-1:
                        if (self.matr[i - 1] == jucator_opus or
                                self.matr[i - n] == jucator_opus or
                                self.matr[i - n - 1] == jucator_opus or
                                self.matr[i + n - 1] == jucator_opus or
                                self.matr[i + n] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i%n==0 and i!=0 and i!=n*n-n:
                        if (self.matr[i + 1] == jucator_opus or
                                self.matr[i - n + 1] == jucator_opus or
                                self.matr[i - n] == jucator_opus or
                                self.matr[i + n] == jucator_opus or
                                self.matr[i + n + 1] == jucator_opus):
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                    elif i>n and i<n*n-n and i%n!=0 and i-1%n!=0:
                        if (self.matr[i + 1] == jucator_opus or
                                self.matr[i - 1] == jucator_opus or
                                self.matr[i - n + 1] == jucator_opus or
                                self.matr[i + n] == jucator_opus or
                                self.matr[i - n - 1] == jucator_opus or
                                self.matr[i + n - 1] == jucator_opus or
                                self.matr[i + n] == jucator_opus ):  #or
                                #self.matr[i + n + 1] == jucator_opus
                            matr_tabla_noua[i] = jucator_opus
                            l_mutari.append(Joc(matr_tabla_noua))
                else:
                    matr_tabla_noua[i] = jucator_opus
                    l_mutari.append(Joc(matr_tabla_noua))

        return l_mutari

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    def linie_deschisa(self, lista, jucator):
        # obtin multimea simbolurilor de pe linie
        mt = set(lista)
        ll=0
        for x in lista:
            if x==jucator:
                ll=ll+1
        if ll>1:
            return 0
        else:
            return 1

    def linii_deschise(self, jucator):
        ld = 0
        for x in range(n):
            for y in range(n - 2):
                ld = ld + self.linie_deschisa(self.matr[x * n + y:x * n + y + 3:1], jucator)

        for y in range(n):
            for x in range(n - 2):
                ld = ld + self.linie_deschisa(self.matr[x * n + y:x * n + y+3*n:n], jucator)

        for x in range(n - 2):
            for y in range(n - 2):
                ld = ld + self.linie_deschisa(self.matr[x * n + y:x * n + y+3*n+2:n+1], jucator)

        for x in range(n - 2):
            for y in reversed(range(2,n)):
                ld = ld + self.linie_deschisa(self.matr[x * n + y:x * n + y+3*n-4:n-1], jucator)

        return ld

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        # if (adancime==0):
        if t_final == self.__class__.JMAX:
            return (-99 - adancime)
        elif t_final == self.__class__.JMIN:
            return (99 + adancime)

        elif t_final == 'remiza':
            return 0
        else:
            return (self.linii_deschise(self.__class__.JMIN) - self.linii_deschise(self.__class__.JMAX))

    def __str__(self):
        sir = ""

        a = 0
        m = n
        for i in range(n):
            sir = sir + " ".join([str(x) for x in self.matr[a:m]]) + "\n"
            a=m
            m=m+n

        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # scorul starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = self.jucator_opus()
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza scorul
            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent < stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')

        for mutare in stare.mutari_posibile:

            stare_noua = alpha_beta(alpha, beta, mutare)

            if (scor_curent > stare_noua.scor):
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A pierdut " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        tip_dificultate = input("Alegeti dificultatea? (raspundeti cu 1 sau 2 sau 3)\n 1.Easy\n 2.Medium\n 3.Hard ")
        if tip_algoritm in ['1', '2', '3']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    raspuns_valid = False
    #dificultate
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu x sau cu 0? ").lower()
        if (Joc.JMIN in ['x', '0']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie x sau 0.")
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'
    #initializare tabla sau #
    raspuns_valid = False
    while not raspuns_valid:
        tip_joc = input("Doriti sa jucati pe interfata grafica sau in consola? (raspundeti cu 1 sau 2)\n 1.Interfata\n 2.Consola\n ")
        if tip_joc in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")


    # initializare tabla
    tabla_curenta = Joc();
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'x', int(tip_dificultate))

    if tip_joc == '1':
        # setari interf grafica
        pygame.init()
        pygame.display.set_caption('x si 0')
        ecran = pygame.display.set_mode(size=(n*102, n*102))

        patratele = deseneaza_grid(ecran, tabla_curenta.matr)
        while True:

            if (stare_curenta.j_curent == Joc.JMIN):
                # muta jucatorul
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        pos = pygame.mouse.get_pos()

                        for np in range(len(patratele)):
                            if patratele[np].collidepoint(pos):
                                linie = np // n
                                coloana = np % n
                                if stare_curenta.tabla_joc.matr[linie * n + coloana] == Joc.GOL:
                                    valid = False
                                    while not raspuns_valid:
                                        while not valid:
                                            try:
                                                c = 0
                                                for i in range(len(stare_curenta.tabla_joc.matr)):
                                                    if stare_curenta.tabla_joc.matr[i] == stare_curenta.j_curent:
                                                        c = c + 1
                                                if c>0:
                                                    if linie == 0 and coloana == 0:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n + 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie == 0 and coloana == n:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie == n and coloana == 0:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n - 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie == n and coloana == n:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n - 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie == 0 and coloana != 0 and coloana != n:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n + 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie == n and coloana != 0 and coloana != n:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n - 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie != 0 and linie != n and coloana == 0:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n + 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie != 0 and linie != n and coloana == n:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                    if linie > 0 and linie < n and coloana > 0 and coloana < n:
                                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n + 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana - n - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n - 1] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n] == stare_curenta.j_curent or
                                                        stare_curenta.tabla_joc.matr[linie * n + coloana + n + 1] == stare_curenta.j_curent):
                                                            valid = True
                                                        else:
                                                            print("Nu ai vecin de acelasi fel")
                                                else: valid=True
                                            except ValueError:
                                                print("Linia si coloana trebuie sa fie numere intregi")
                                    # dupa iesirea din while sigur am valide atat linia cat si coloana
                                    # deci pot plasa simbolul pe "tabla de joc"
                                    stare_curenta.tabla_joc.matr[linie * n + coloana] = Joc.JMIN

                                    # afisarea starii jocului in urma mutarii utilizatorului
                                    print("\nTabla dupa mutarea jucatorului")
                                    print(str(stare_curenta))
                                    patratele = deseneaza_grid(ecran, stare_curenta.tabla_joc.matr)
                                    # testez daca jocul a ajuns intr-o stare finala
                                    # si afisez un mesaj corespunzator in caz ca da
                                    if (afis_daca_final(stare_curenta)):
                                        break

                                    # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                    stare_curenta.j_curent = stare_curenta.jucator_opus()


            # --------------------------------
            else:  # jucatorul e JMAX (calculatorul)
                # Mutare calculator

                # preiau timpul in milisecunde de dinainte de mutare
                t_inainte = int(round(time.time() * 1000))
                if tip_algoritm == '1':
                    stare_actualizata = min_max(stare_curenta)
                else:  # tip_algoritm==2
                    stare_actualizata = alpha_beta(-500, 500, stare_curenta)
                stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
                print("Tabla dupa mutarea calculatorului")
                print(str(stare_curenta))

                patratele = deseneaza_grid(ecran, stare_curenta.tabla_joc.matr)
                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

                if (afis_daca_final(stare_curenta)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stare_curenta.j_curent = stare_curenta.jucator_opus()
    else:
        while True:
            if (stare_curenta.j_curent == Joc.JMIN):
                # muta jucatorul
                raspuns_valid = False
                valid = False
                while not raspuns_valid:
                    while not valid:
                        try:
                            linie = int(input("linie="))
                            if linie == n+1:
                                sys.exit('s-a iesit din joc')
                            coloana = int(input("coloana="))

                            if (linie in range(0, n+1) and coloana in range(0, n)):

                                if stare_curenta.tabla_joc.matr[linie * n + coloana] == Joc.GOL:
                                    raspuns_valid = True
                                else:
                                    print("Exista deja un simbol in pozitia ceruta.")
                            else:
                                print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0,1,2).")

                            if (linie in range(0, n) and coloana in range(0, n)):
                                c=False
                                for x in stare_curenta.tabla_joc.matr:
                                    if x==stare_curenta.j_curent:
                                        c=True
                                if c:
                                    if linie==0 and coloana==0:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n+1] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie==0 and coloana==n-1:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie==n-1 and coloana==0:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n-1] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie==n-1 and coloana==n-1:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n-1] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie==0 and coloana!=0 and coloana!=n-1:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n+1] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie==n-1 and coloana!=0 and coloana!=n-1:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n-1] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie!=0 and linie!=n-1 and coloana==0:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n+1] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie!=0 and linie!=n-1 and coloana==n-1:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                    if linie>0 and linie<n-1 and coloana>0 and coloana<n-1:
                                        if (stare_curenta.tabla_joc.matr[linie * n + coloana+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n+1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana-n-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n-1] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n] == stare_curenta.j_curent or
                                        stare_curenta.tabla_joc.matr[linie * n + coloana+n+1] == stare_curenta.j_curent
                                        ):
                                            valid=True
                                        else:
                                            print("Nu ai vecin de acelasi fel")
                                else: valid =True
                            else:
                                print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0,1,2).")
                        except ValueError:
                            print("Linia si coloana trebuie sa fie numere intregi")

                # dupa iesirea din while sigur am valide atat linia cat si coloana
                # deci pot plasa simbolul pe "tabla de joc"
                stare_curenta.tabla_joc.matr[linie * n + coloana] = Joc.JMIN

                # afisarea starii jocului in urma mutarii utilizatorului
                print("\nTabla dupa mutarea jucatorului")
                print(str(stare_curenta))

                # testez daca jocul a ajuns intr-o stare finala
                # si afisez un mesaj corespunzator in caz ca da
                if (afis_daca_final(stare_curenta)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stare_curenta.j_curent = stare_curenta.jucator_opus()

            # --------------------------------
            else:  # jucatorul e JMAX (calculatorul)
                # Mutare calculator

                # preiau timpul in milisecunde de dinainte de mutare
                t_inainte = int(round(time.time() * 1000))
                if tip_algoritm == '1':
                    stare_actualizata = min_max(stare_curenta)
                else:  # tip_algoritm==2
                    stare_actualizata = alpha_beta(-500, 500, stare_curenta)
                stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc  # aici se face de fapt mutarea !!!
                print("Tabla dupa mutarea calculatorului")
                print(str(stare_curenta))

                # preiau timpul in milisecunde de dupa mutare
                t_dupa = int(round(time.time() * 1000))
                print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

                if (afis_daca_final(stare_curenta)):
                    break

                # S-a realizat o mutare. Schimb jucatorul cu cel opus
                stare_curenta.j_curent = stare_curenta.jucator_opus()




if __name__ == "__main__":
    main()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
