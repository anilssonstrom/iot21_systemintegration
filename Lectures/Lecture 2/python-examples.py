
def keep_playing_menu():
    """
    Vill du spela igen? (Y/N)
    """
    keep_playing = True
    while keep_playing:
        # Kastar tärningar
        # Ritar om spelplanen
        # Kollar vem som vann
        # Fråga: Vill du spela igen?
        """
        choice = input("Vill du spela igen? (Y/N): ")   # y = fortsätt, allt annat avslutar programmet
        if not choice.lower().startswith('y'):
            keep_playing = False
        """
        keep_playing = input("Vill du spela igen? (Y/N): ").lower().startswith('y')


def numbered_menu():
    # Ex på hur det kan se ut i labben
    # Hämtar alla stationer
    # Ritar upp alla namn i en meny
    # Välj station
    # Använd stationens id till något

    menu = """
    Välj ett alternativ
    1. Spela
    2. Inställningar
    3. Hjälp
    4. Avsluta
    """

    keep_playing = True
    while keep_playing:
        print(menu)
        choice = int(input("Val: "))

        if choice == 1:
            # Anropa en metod som gör något bra
            # play()
            print("Choice:", choice)
        elif choice == 4:
            keep_playing = False
        else:
            print("Inte implementerat! Oops!")


numbered_menu()
