# External Imports
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
import discord
from discord.ext import commands

# Internal Imports
from src.discordAPI import *
from src.inputAnalysis import *
from src.inputHandler import *
from src.twitterAPI import *
from src.sqlAPI import *
from src.output import *


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = authorize(creds)
ID = Type = Weight = Description = GoodAgainst = BadAgainst = False
sheet1 = client.open("PDB").worksheet("sheet1")
name_list = sheet1.col_values(2)
file_len = len(name_list)
client = discord.Client()


@client.event
async def on_ready():
    print("The bot is ready.")


def search_name(info_list):
    found_pokemons = False
    pokemon_info_list = []
    for name in info_list[7]:
        name = name.capitalize()
        if name in name_list:
            cell = sheet1.find(name)
            y = cell.row
            found_pokemons = True
            if info_list[9]:
                pokemon_info_list.append(f"ID: {sheet1.cell(y, 1).value}")
            if info_list[0]:
                type_1 = str(sheet1.cell(y, 3).value)
                type_2 = str(sheet1.cell(y, 4).value)
                if not type_2:
                    pokemon_info_list.append(f"Type: {type_1}")
                else:
                    pokemon_info_list.append(f"Type1: {type_1}")
                    pokemon_info_list.append(f"Type2: {type_2}")
            if info_list[1]:
                pokemon_info_list.append(f"Weight: {sheet1.cell(y, 5).value}")
            if info_list[2]:
                pokemon_info_list.append(f"Description: {sheet1.cell(y, 6).value}")
            if info_list[3]:
                pokemon_info_list.append(f"Good Against: {sheet1.cell(y, 7).value}")
            if info_list[4]:
                pokemon_info_list.append(f"Bad Against: {sheet1.cell(y, 8).value}")
            if not any(info_list):
                pokemon_info_list.extend(
                    [
                        f"ID: {sheet1.cell(y, 1).value}",
                        f"Type: {sheet1.cell(y, 3).value}",
                        f"Type2: {sheet1.cell(y, 4).value}",
                        f"Weight: {sheet1.cell(y, 5).value}",
                        f"Description: {sheet1.cell(y, 6).value}",
                        f"Good Against: {sheet1.cell(y, 7).value}",
                        f"Bad Against: {sheet1.cell(y, 8).value}",
                    ]
                )
    return [pokemon_info_list, found_pokemons]


def number_of_types(pokemon_type):
    count = 0
    column1 = sheet1.col_values(3)
    column2 = sheet1.col_values(4)
    num_rows = len(column1)
    column2.extend([""] * (num_rows - len(column2)))
    for i in range(num_rows):
        if pokemon_type[0] in (column1[i], column2[i]):
            if len(pokemon_type) > 1 and pokemon_type[1] in (column1[i], column2[i]):
                count += 1
            elif len(pokemon_type) == 1:
                count += 1
    return [count]


def search_type(pokemon_type, num_pokemons):
    pokemon_type = [t.capitalize() for t in pokemon_type]
    type_columns = sheet1.col_values(3) + [""] * (
        sheet1.row_count - len(sheet1.col_values(3))
    )
    type2_columns = sheet1.col_values(4) + [""] * (
        sheet1.row_count - len(sheet1.col_values(4))
    )
    pokemon_info_list = []
    for idx, (type1, type2) in enumerate(zip(type_columns, type2_columns)):
        if pokemon_type[0] in (type1, type2) and (
            len(pokemon_type) == 1 or pokemon_type[1] in (type1, type2)
        ):
            num_pokemons -= 1
            if num_pokemons >= 0:
                pokemon_info_list.append(name_list[idx])
            else:
                break
    return pokemon_info_list


def all_true():
    pokemon_name_list = [sheet1.cell(y, 2).value for y in range(file_len)]
    return pokemon_name_list


@client.event
async def on_message(message):
    if message.content.startswith("!"):
        return
    question = str(message.content)
    if "news" in question.lower():
        await message.channel.send(pokemon_tweet(1))
        question = "type"
    infoList, b = input_function(question)[:2]
    infoList, d = input_breakdown(infoList)[:2]
    a, c = search_name(infoList)[:2]
    if c:
        return
    if infoList[8]:
        infoList[6] = file_len
    if infoList[4]:
        if infoList[2]:
            a = best_pokemon(True, infoList[6], infoList[5])
        elif infoList[3]:
            a = best_pokemon(False, infoList[6], infoList[5])
        elif infoList[1]:
            a = number_of_types(infoList[5])
        else:
            a = search_type(infoList[5], infoList[6])
    else:
        if infoList[0]:
            a = name_list[1 : infoList[6] + 1]
        elif infoList[1]:
            a = [len(name_list)]
        elif not any(infoList[2:4]) and not infoList[9]:
            a = name_list
        else:
            a = []
    outString = output(a, b, infoList, c, d)
    await message.channel.send(outString)


client.run("API_KEY")
