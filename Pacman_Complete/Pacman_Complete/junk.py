def checkEvents(self): # Funktsiooni algus, see funktsioon jälgib mängusündmusi.
    for event in pygame.event.get(): # Iterateerib üle kõigi Pygame'i poolt kogutud sündmuste.
        if event.type == QUIT: # Kontrollib, kas sündmuse tüüp on akna sulgemine.
            exit() # Kui akent on üritatud sulgeda, siis lõpetatakse programmi töö.
        elif event.type == KEYDOWN: # Kontrollib, kas sündmuse tüüp on klahvi allavajutamine.
            if event.key == K_SPACE: # Kui vajutati tühikuklahvi.
                if self.pacman.alive: # Kontrollib, kas pacman on elus.
                    self.pause.setPause(playerPaused=True) # Seab pausi, kui mängija pole pausil.
                    if not self.pause.paused: # Kui mäng pole pausil.
                        #newtext::self.textgroup.hideText() # Ajutine kommentaar - varjab tekstigrupi teksti.
                        self.showEntities() # Näitab mänguüksusi.
                    else: # Kui mäng on pausil.
                        #newtext::self.textgroup.showText(PAUSETXT) # Ajutine kommentaar - näitab tekstigrupi teksti.
                        self.hideEntities() # Peidab mänguüksusi.
