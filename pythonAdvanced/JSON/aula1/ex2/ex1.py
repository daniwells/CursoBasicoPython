import json

cars_dic = {"mark":"honda","model":"HVR","color":"red"}

cars_list = ['honda', 'volkswagem', 'ford', 'fiat', 'chevrolet']

cars_tupla = ('honda', 'volkswagem', 'ford', 'fiat', 'chevrolet')

cars_j1 = json.dumps(cars_dic, indent=4, separators=(":","="),sort_keys=True)
cars_j2 = json.dumps(cars_list)
cars_j3 = json.dumps(cars_tupla)

print(cars_j1)
print(cars_j2)
print(cars_j3)

#############################################################
"""
player = {
    "name":"Daniel",
    "team":"drivers",
    "alive":True,
    "energy":85,
    "backpack":["knife","sniper","rope"],
    "cars":[
        {"type":"transport", "ability":65},
        {"type":"atack", "ability":70},
        {"type":"race", "ability":100}
    ]
}

player_j= json.dumps(player, indent=4)

print(player_j)"""

#############################################################

"""player_jso = '{"name":"Daniel","team":"drivers","alive":"True","energy":"85","backpack":["knife","sniper","rope"], "cars":[ {"type":"transport", "ability":"65"},{"type":"atack", "ability":"70"},{"type":"race", "ability":"100"}]}'

player_p = json.loads(player_jso)


'for k, e in player_p['cars'][0].items():
    print(f'{k} = {e}')'

print(player_p["name"])
"""








