W pliku zad1.py znajduje sie main, natomiast reszta plikow to moduly. zad1.py przyjmuje
nastepujace parametry i opcje:
1. --comp opcje: '<=', '>='; wymagany,
2. --type opcje: dual, hybrid, insert, quick, merge; wymagany,
3. --stat nazwa_pliku k; opcjonalny,
4. --data opcje: str, int, float; opcjonalny - jezeli nie zostanie podany program dziala na intach,
    podanie go nie ma wplywu na opcje stat - statystyki dalej prowadzone sa na losowych intach.
Parametry moga byc podane w dowolnej kolejnosci. W pliku verify.py znajduja sie funkcje sprawdzajace
poprawnosc podanych parametrow i danych oraz je porzadkujace.

Kazdy z algorytmow na liscie zadan znajduje sie w pliku o odpowiedniej nazwie. Wystepuja one
w dwoch wersjach - podstawowej i statystycznej. Roznia sie one tym, iz podstawowa printuje
porownania i swapy na stderr i podsumowanie na stdout, tymczasem statystyczna wypisuje
czas dzialania algorytmu, rozmiar danych, liczbe porownan i liczbe swapow do podanego pliku.
Wersja statystyczna jest oczywiscie bardziej czytelna.

W pliku wykresy.xlsx znajduja sie wykresy z zadania 2, a w arkuszu z danymi dla k = 50 jest
rowniez eksperymentalnie wyznaczona stala z zadania 3. W wykresach dla k = 10 i k = 50 nie
wzielam pod uwage insertion sorta, poniewaz znacznie odbiega statystykami od pozostalych algorytmow
i sprawia, ze wykresy dla nich staja sie nieczytelne i nie bardzo mozna z nich cokolwiek wyciagnac.
Swoja droga uzyskiwanie danych insertiona dla k = 1 zajmuje 11 minut, wiec pozyskanie ich dla
k = 50 byloby nieco czasochlonne.

Moj hybrid sort to polaczenie merge sorta i insertiona. Jest glownie mergem, ale gdy dostanie
tablice o dlugosci mniejszej niz 20 przelacza sie na insertiona. W pliku merge_10.txt znajduja sie
dane dla zwyklego merge sorta z opcja stat k = 10, a w pliku hybrid_10.txt znajduja sie dane dla
hybrida z tym samym parametrem. Widac, ze dla wiekszych n radzi sobie szybciej niz zwykly merge.

W plikach hybrid_f_n.txt znajduja sie statystyki hybrida dla k = 1 dzialajacego na floatach i 
przelaczajacego sie na insertiona w momencie, gdy dostanie tablicze krotsza niz n. Jak widac
ma to nieznaczny wplyw na czas dzialania algorytmu.
