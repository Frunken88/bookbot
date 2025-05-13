def words_in_book(bok_split):
    sum = 0
    bok_delad = bok_split.split()
    for b in bok_delad:
        sum += 1
    return sum

def chars_in_book(bok_split):
    kand = {}
    sma = ""
    for boks in bok_split:
        sma = boks.lower()
        if sma in kand:
            kand[sma] += 1
        else:
            kand[sma] = 1
    return kand

def sort_on(dict):
    return dict["num"]

def present_book(kand):
    pres_dict = [{"char": key, "num": value} for key, value in kand.items()]
    pres_dict.sort(reverse=True, key=sort_on)
    return pres_dict
