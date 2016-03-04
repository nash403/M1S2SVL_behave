TP lgin : différences entre BDD et TDD

La différence d'approche nous a permis de remarquer que nous n'avions pas exactements trouvé les mêmes tests entre une approche TDD et une approche BDD
L'approche TDD a fait ressortir davantage de tests plus précis, tandis que l'approche BDD a fait ressortir moins de tests, et moins précis.
Par exemple, dans le cas où l'on teste en entrant un login à la main, l'approche TDD avait fait apparaître un test si le login était trop long et un test si le login n'est pas en minuscule.
Avec l'approche BDD, ces 2 tests ont été fusionnées en un test de mauvais formatage du login.
