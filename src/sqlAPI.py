from sqlite3 import *

""" 
Basically this is how the database looks, i wrote everything using an example from the documentation of SQLite.
There was no maual labour here what so ever,
I pulled the names of the pokemon from the main bot and just placed the first fiveas they should be, the other ones dont matter.
"""
# if __name__ == '__main__':
#     conn = None
#     try:
#         conn = connect('best.sql')
#         c = conn.cursor()
#         c.execute(""" CREATE TABLE bestfive (
#             ptype text,
#             first text
#         )""")
#         c.execute("INSERT INTO bestfive VALUES ('Dragon','Dragonite, Dragonair, Dratini')")
#         c.execute("INSERT INTO bestfive VALUES ('Fairy','Clefable, Mr. Mime, Wigglytuff, Jigglypuff, Clefairy')")
#         c.execute("INSERT INTO bestfive VALUES ('Grass','Exeggutor, Venusaur, Vectreebel, Vileplume, Tangela, Parasect, Weepinbell, Gloom, Oddish, Paras, Bellsprout, Exeggcute')")
#         c.execute("INSERT INTO bestfive VALUES ('Fire','Moltres, Charizard, Flareon, Arcanine, Ninetales, Magmar, Charmeleon, Vulpix, Glowlithe, Ponyta, Rapidash, Charmander')")
#         c.execute("INSERT INTO bestfive VALUES ('Water','Vaporeon, Gyarados, Lapras, Blastoise, Starmie, Wartortle, Psyduck, Golduck, Poliwag, Poliwhirl, Poliwrath, Tentacool, Tentacruel, Slowpoke, Slowbro, Seel, Dewgong, Shellder, Cloyster, Krabby, Kingler, Horsea, Seadra, Goldeen, Seaking, Staryu, Magikarp, Omanyte, Omastar, Kabuto, Kabutops')")
#         c.execute("INSERT INTO bestfive VALUES ('Bug','Beedrill, Scyther, Parasect, Pinsir, Butterfree, Metapod, Weedle, Kakuna, Paras, Venonat, Venomoth')")
#         c.execute("INSERT INTO bestfive VALUES ('Normal','Tauros, Chansey, Snorlax, Pidgeot, Raticate, Pidgeotto, Rattata, Spearow, Fearow, Jigglypuff, Wigglytuff, Meowth, Persian, Farfetchd, Doduo, Dodrio, Lickitung, Kangaskhan, Ditto, Eevee, Porygon, Pidgey')")
#         c.execute("INSERT INTO bestfive VALUES ('Poison','Venusaur, Nidoking, Nidoqueen, Weezing, Muk, Butterfree, Weedle, Kakuna, Ekans, Arbok, Nidoran F, Nidorina, Nidoran M, Nidorino, Zubat, Golbat, Oddish, Gloom, Vileplume, Venonat, Venomoth, Bellsprout, Weepinbell, Victreebel, Tentacool, Tentacruel, Grimer, Gastly, Haunter, Gengar, Koffing')")
#         c.execute("INSERT INTO bestfive VALUES ('Electric','Zapdos, Electabuzz, Jolteon, Raichu, Magneton, Magnemite, Voltorb, Electrode, Pikachu')")
#         c.execute("INSERT INTO bestfive VALUES ('Ground','Rhydon, Sandslash, Marowak, Ryhorn, Golem, Sandshrew, Nidoqueen, Nidoking, Diglett, Dugtrio, Geodude, Graveler, Onix, Cubone')")
#         c.execute("INSERT INTO bestfive VALUES ('Fighting','Machamp, Primape, Hitmonchan, Hitmonlee, Machoke, Mankey, Poliwrath, Machop')")
#         c.execute("INSERT INTO bestfive VALUES ('Psychic','Mewtwo, Mew, Alakazam, Kadabra, Hypno, Abra, Slowpoke, Slowbro, Drowzee, Exeggcute, Exeggutor, Starmie, Mr. Mime, Jynx')")
#         c.execute("INSERT INTO bestfive VALUES ('Rock','Golem, Rhydon, Omastar, Kabutops, Aerodactyl, Graveler, Onix, Rhyhorn, Omanyte, Kabuto, Geodude')")
#         c.execute("INSERT INTO bestfive VALUES ('Ghost','Gengar, Haunter, Gastly')")
#         c.execute("INSERT INTO bestfive VALUES ('Ice','Articuno, Lapras, Cloyster, Jinx, Dewgong')")
#         c.execute("INSERT INTO bestfive VALUES ('Flying','Dragonite, Articuno, Zapdos, Moltres, Gyarados, Charizard, Metapod, Beedrill, Pidgey, Pidgeotto, Spearow, Fearow, Zubat, Golbat, Farfetchd, Doduo, Dodrio, Scyther, Aerodactyl')")
#         c.execute("INSERT INTO bestfive VALUES ('Steel','Magneton, Magnemite')")

#         c.execute("SELECT * FROM bestfive")
#         print(c.fetchall())
#         conn.commit()
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()
"""
The next bit is the actual function used in the bot!
It takes some parameters from the main functions
and searches through the db for the passed strings and integers.
"""


def best_pokemon(best, number, types):
    conn = connect("best.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM bestfive")
    rows = c.fetchall()  # everything gets "fetched" in "rows"
    types.append("")
    if len(types[1]) < 1:  # Now I test if there are 2 types passed through my function.
        for i in range(len(rows)):  # If it passes the IF statement there is only one type passed to the function!
            if types[0] == str(rows[i][0]):
                iType = i
        a = rows[iType][1]  # Some basic string manipulation. Got the idea from Meldas's code, and implemented it into mine
        a = a.replace(",", "")
        a = a.rsplit()
        b = []
        if (best == False):  # This line makes the list go backwards. Thats how we get the worst pokemon.
            for i in range(1, number + 1):
                if i < len(a):
                    b.append(a[-i])
        else:  # And thats how get the best pokemon.
            for i in range(number):
                if i < len(a):
                    b.append(a[i])
    else:  # This ELSE statement deals with the request for dual type pokemon.
        for i in range(len(rows)):  # It is mostly the same as the one above, but with one difference.
            if types[0] == str(rows[i][0]):
                iType = i
        a = rows[iType][1]
        a = a.replace(",", "")
        a = a.rsplit()
        b = []
        for i in range(len(rows)):
            if types[1] == str(rows[i][0]):
                iType = i
        c = rows[iType][1]
        c = c.replace(",", "")
        c = c.rsplit()

        for i in a:  # Which is this nifty loop, that compares the lists contaiting individual types,
            for o in c:  # and every single name that is repeted gets in the final list, that is returned to the user.
                if i == o:
                    b.append(i)
        if best == False:
            for i in range(1, number + 1):
                if i < len(b):
                    b.append(a[-i])
        else:
            for i in range(number):
                if i < len(b):
                    b.append(a[i])
    return b
