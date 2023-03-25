import pandas as pd

df = pd.read_csv("Prematch Data.csv", index_col="Team")

matchn = int(input("Input Match #: "))
#matches = {}
teams = [input("Enter Team 1's (In order of 3 red, 3 blue) #: "), input("Enter Team 2's #: "), input("Enter Team 3's #: "),
         input("Enter Team 4's #: "), input("Enter Team 5's #: "), input("Enter Team 6's #: ")]

print("*Match Number:* " + str(matchn))
#teams = matches[matchn]

for num, tn in enumerate(teams):
    if num <= 2:
        print(":red_circle:*" + tn + "*:red_circle:")
    else:
        print(":large_blue_circle:*" + tn + "*:large_blue_circle:")

    x = df.loc[int(tn)]
    print("Center of Gravity: " + str(x["Center of Gravity"]))

    # Auto
    print("Auto: ", end="")
    als = ["Low", "Mid", "High"]
    c = 3
    try:
        for i in als:
            if int(x[f"Normal # of Pieces {i} Auto"]) != 0:
                print(str(x[f"Normal # of Pieces {i} Auto"]) + f" {i}", end="")
                c -= 1
        if c == 3:
            print("No pieces in Auto", end="")
    except ValueError:
        print("NaN, ", end="")

    try:
        if float(x["AUTO % Engage"].replace("%", "")) > 50:
            print(" and Engage", end="")
        if float(x["AUTO % Mobility"].replace("%", "")) > 50:
            print(" and Mobility ", end="")
    except ValueError:
        print(", NaN", end="")

    # what node, make sure to fix code later b/c hella convoluted and inefficient rn
    # try:
    dict = {
        "Low": float(str(x["% Low Score"]).replace("%", "")),
        "Mid": float(str(x["% Mid Score"]).replace("%", "")),
        "High": float(str(x["% High Score"]).replace("%", ""))
    }
    y = max(float(str(x["% Low Score"]).replace("%", "")), float(str(x["% Mid Score"]).replace("%", "")), float(str(x["% High Score"]).replace("%", "")))
    for i in dict.values():
        if str(i) != "0.0" and (str(i) == "50.0" or str(i) == "33.3"):
            print("\nNode(s): " + ", ".join([k for k, v in dict.items() if v == i]))
            break
        else:
            print("\nNode(s): " + list(dict.keys())[list(dict.values()).index(float(y))] + " Node")
            break
    # except ValueError:
    #     print("\nNode: NaN Error")

    # total teleop pieces (obviously)
    try:
        print("Total Teleop Pieces: " + str(sum([int(x["Normal # of Pieces Low Teleop"]), int(
            x["Normal # of Pieces Mid Teleop"]), int(x["Normal # of Pieces High Teleop"])])))
    except ValueError:
        print("Total Teleop Pieces: NaN Error")

    # feeder
    print("Feeder Type(s): ", end="")
    try:
        dict2 = {
            "Ground": float(str(x["% Field Pickup"]).replace("%", "")),
            "Single": float(str(x["% Slide Pickup"]).replace("%", "")),
            "Double": float(str(x["% High Pickup"]).replace("%", ""))
        }

        feederls = list(dict2.values())
        feederls.sort(reverse=True)
        for i in feederls:
            if str(i) != "0.0" and str(i) == "50.0" or str(i) == "33.3":
                print(" ".join([k for k, v in dict2.items() if v == i]), end="")
                break
            elif str(i) != "0.0":
                print(list(dict2.keys())[list(dict2.values()).index(i)], end=" ")
                break
    except ValueError:
        print("NaN Error", end="")

    # cones/cubes
    if x["% Both"] != "0.0%" or (x["% Cone"] != "0.0%" and x["% Cube"] != "0.0%"):
        print("\nGP: Both cubes and cones")
    elif x["% Cone"] != "0.0%":
        print("\nGP: Cones")
    elif x["% Cube"] != "0.0%":
        print("\nGP: Cubes")
    else:
        print("\nNo Data")

    # end engage percent
    print("Percent of Engages in Endgame: " + x["END % Engage"])

    # defense?
    try:
        print("Defense: Yes") if float(x["Defense Preformance"]) > 5.0 else print("Defense: No")
    except ValueError:
        print("Defense: NaN Error")

    # newline  /\_/\
    #         ( o.o )
    #          > ^ <

    print("\n")
