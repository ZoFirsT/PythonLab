areyouStd = input("Are you a student? [Y/N]")
if areyouStd.lower() == "y":
    pad = input("What you sex. [M/F]")
    if pad.lower() == "m":
        print("you discount is 10%")
    elif pad.lower() == "f":
        print("you discount is 15%")
else:
    print("you discount is 0%")