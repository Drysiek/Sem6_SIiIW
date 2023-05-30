aplikacja(netflix).

% Użytkownicy
login(user1).
login(user2).
login(user3).

hasło(password1).
hasło(password2).
hasło(password3).

użytkownik(user1, password1).
użytkownik(user2, password2).
użytkownik(user3, password3).

użytkownik(może, tworzyć_konto).
użytkownik(może, logować_się).
użytkownik(może, przeglądać_filmy).
użytkownik(może, ogladać_film).
użytkownik(może, ściagać_film_na_urzadzenie_mobilne).

% Definicja filmów/seriali
film(black_mirror).
film(narcos).
film(friends).
film(stranger_things).
film(the_crown).
film(the_office).
film(zielona_mila).
film(lucy).
film(pulp_fiction).
film(sully).
film(breaking_bad).
film(money_heist).
film(the_witcher).
film(the_big_bang_theory).

% Definicja gatunków filmów/seriali
gatunek(black_mirror, drama).
gatunek(black_mirror, science_fiction).
gatunek(black_mirror, dystopian).
gatunek(narcos, crime).
gatunek(narcos, drama).
gatunek(friends, comedy).
gatunek(stranger_things, science_fiction).
gatunek(stranger_things, horror).
gatunek(stranger_things, mystery).
gatunek(the_crown, drama).
gatunek(the_crown, history).
gatunek(the_office, comedy).
gatunek(breaking_bad, crime).
gatunek(breaking_bad, drama).
gatunek(breaking_bad, thriller).
gatunek(money_heist, crime).
gatunek(money_heist, thriller).
gatunek(the_witcher, drama).
gatunek(the_witcher, fantasy).
gatunek(the_witcher, action).
gatunek(the_big_bang_theory, comedy).
gatunek(the_big_bang_theory, romance).
gatunek(sully, drama).
gatunek(pulp_fiction, drama).
gatunek(pulp_fiction, drama).
gatunek(lucy, science_fiction).
gatunek(zielona_mila, crime).
gatunek(zielona_mila, drama).


% Polubione filmy
polubione(user1, black_mirror).
polubione(user1, friends).
polubione(user1, the_crown).
polubione(user1, stranger_things).
polubione(user1, breaking_bad).
polubione(user1, the_witcher).
polubione(user1, the_big_bang_theory).
polubione(user1, narcos).
polubione(user1, the_office).
polubione(user2, stranger_things).
polubione(user2, breaking_bad).
polubione(user2, the_witcher).
polubione(user2, the_big_bang_theory).
polubione(user3, narcos).
polubione(user3, the_office).
polubione(user3, the_big_bang_theory).
polubione(user3, stranger_things).
polubione(user3, the_crown).
polubione(user3, breaking_bad).

% Ściągnięte filmy
ściągnięte(user1, 3).
ściągnięte(user2, 5).
ściągnięte(user3, 0).


% Procedura wypisywania rekomendacji
rekomendacja(Film1, Film2, Gatunek) :- 
    gatunek(Film1, Gatunek), 
    gatunek(Film2, Gatunek), 
    Film1 \= Film2.

% Procedura polecenia filmu/serialu dla konkretnego użytkownika
polecenie_filmu_dla_użytkownika(Użytkownik, Film_polubiony, Film_do_polecenia, Gatunek) :- 
    użytkownik(Użytkownik, _),
    użytkownik(może, przeglądać_filmy),
    rekomendacja(Film_polubiony, Film_do_polecenia, Gatunek), 
    polubione(Użytkownik, Film_polubiony),
    \+ polubione(Użytkownik, Film_do_polecenia).

% Procedura logowania
może_się_zalogować(Użytkownik, Hasło) :-
    użytkownik(może, logować_się),
    użytkownik(Użytkownik, Hasło).

% Procedura oglądania filmów/seriali
może_oglądać_film(Użytkownik, Film) :-
    użytkownik(Użytkownik, _),
    użytkownik(może, ogladać_film),
    film(Film).

% Procedura ściągania filmu/serialu na urządzenie mobilne
może_ściągnąć_film(Użytkownik, Film) :-
    użytkownik(Użytkownik, _),
    użytkownik(może, ściagać_film_na_urzadzenie_mobilne),
    film(Film),
    ściągnięte(Użytkownik, Liczba_ściągniętych),
    Liczba_ściągniętych < 5.


% Diagnostyka problemów
problem(logowanie).
problem(odtwarzanie_filmu).
problem(działanie_aplikacji).
problem(ściąganie_filmu).

możliwy_powód(logowanie, brak_konta).
możliwy_powód(logowanie, złe_hasło).
możliwy_powód(logowanie, brak_internetu).
możliwy_powód(odtwarzanie_filmu, brak_dostępu).
możliwy_powód(odtwarzanie_filmu, film_nie_istnieje).
możliwy_powód(odtwarzanie_filmu, brak_internetu).
możliwy_powód(działanie_aplikacji, błąd_synchronizacji).
możliwy_powód(działanie_aplikacji, zakłócenia_urządzenia).
możliwy_powód(działanie_aplikacji, brak_internetu).
możliwy_powód(działanie_aplikacji, brak_najnowszej_aktualizacji).
możliwy_powód(ściąganie_filmu, brak_najnowszej_aktualizacji).
możliwy_powód(ściąganie_filmu, film_nie_istnieje).
możliwy_powód(ściąganie_filmu, za_dużo_ściągniętych_filmów).
możliwy_powód(ściąganie_filmu, brak_internetu).

% dane do sprawdzania problemów
spróbuj(brak_konta, 'stwórz konto').
spróbuj(złe_hasło, 'zresetuj hasło').
spróbuj(brak_internetu, 'sprawdź połączenie z internetem').
spróbuj(film_nie_istnieje, 'wybierz inny film').
spróbuj(zakłócenia_urządzenia, 'wyłącz i włącz aplikację').
spróbuj(za_dużo_ściągniętych_filmów, 'usuń kilk aściągniętych filmów').
spróbuj(brak_dostępu, 'sprawdź czy masz aktywną subskrypcję').
spróbuj(błąd_synchronizacji, 'skontaktuj się z obsługą klienta').
spróbuj(brak_najnowszej_aktualizacji, 'pobierz najnowszą aktualizację').


rozwiązanie(Problem, Działanie) :-
    możliwy_powód(Problem, Powód),
    spróbuj(Powód, Działanie).

znajdź_rozwiązanie_problemu(Problem, Działanie) :-
    problem(Problem),
    rozwiązanie(Problem, Działanie).


rozwiązywanie_problemów_skrypt :-
    write('Z czym jest problem?'), nl,
    read(Problem),
    (problem(Problem) ->
        znajdź_rozwiązanie_problemu(Problem, Działanie),
        write(Działanie), nl
    ;
        write('Nieznany problem.'), nl
    ).

% rekomendacja(stranger_things, black_mirror, G).
% G = science_fiction
% 
% rekomendacja(friends, F2, G).
/*F2 = the_office,
G = comedy
F2 = the_big_bang_theory,
G = comedy*/
% 
% polecenie_filmu_dla_użytkownika(user1, F, F2, G).
/* F = narcos,
F2 = money_heist,
G = crime
F = breaking_bad,
F2 = money_heist,
G = crime
F = breaking_bad,
F2 = money_heist,
G = thriller*/
% 
% może_się_zalogować(user1, password1).
% true
% 
% może_oglądać_film(user1, black_mirror).
% true
% 
% może_ściągnąć_film(user1, money_heist).
% true
% 
% może_ściągnąć_film(user2, money_heist).
% false
% znajdz_rozwiązanie_problemu(logowanie, X).
/*X = 'stwórz konto'
X = 'zresetuj hasło'
X = 'sprawdź połączenie z internetem'*/
%