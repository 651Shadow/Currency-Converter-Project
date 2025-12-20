import pytemperature as pt

ss = ["C", "F", "K"]


def Temperature_convert(value: float, base: str, to: str):
    if base.lower() == ss[0].lower():
        if to.lower() == ss[1].lower():
            return pt.c2f(value)
        elif to.lower() == ss[2].lower():
            return pt.c2k(value)

    elif base.lower() == ss[1].lower():
        if to.lower() == ss[0].lower():
            return pt.f2c(value)
        elif to.lower() == ss[2].lower():
            return pt.f2k(value)

    elif base.lower() == ss[2].lower():
        if to.lower() == ss[0].lower():
            return pt.k2c(value)
        elif to.lower() == ss[1].lower():
            return pt.k2f(value)


if __name__ == "__main__":
    print("asd")
