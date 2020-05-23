airport(madrid, 75, 45).
airport(toronto, 50, 60).
airport(malaga, 50, 30).
airport(valencia, 40, 20).
airport(barcelona, 40, 30).
airport(london, 75, 80).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

flights(madrid, airCanada, toronto, 900, 480).
flights(madrid, united, toronto, 950, 540).
flights(madrid, iberia, toronto, 800, 480).
flights(madrid, airCanada, barcelona, 100, 60).
flights(madrid, iberia, barcelona, 120, 65).
flights(madrid, iberia, valencia, 40, 50).
flights(madrid, iberia, malaga, 50, 60).
flights(malaga, iberia, valencia, 80, 120).
flights(valencia, iberia, barcelona, 110, 75).
flights(barcelona, iberia, london, 220, 240).
flights(toronto, united, london, 640, 420).
flights(toronto, airCanada, london, 500, 360).
flights(paris, united, toulouse, 35, 120).
    
%answers to the last 5 queries:

flight(A, C, B, D, E) :- flights(A, C, B, D, E); flights(B, C, A, D, E).

isFlight(A, B) :- flights(A, _, B, _, _); flights(B, _, A, _, _).

ifFlightExist(A,C,B,D,E) :- flights(A,C,B,D,E); flights(B,C,A,D,E).

isCheap(A, C, B) :- ifFlightExist(A, C, B, D, _), D < 400.

isPrefered(A, C, B) :- isCheap(A, C, B); C = airCanada.

flight_airCanada(A, C, B) :-  ifFlightExist(A, united, B, _, _), C = airCanada. 

isTwoFlight(A, B) :- isFlight(A, F), isFlight(F, B).