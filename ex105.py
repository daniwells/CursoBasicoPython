def bol(*n, sit=False):
    """
    :param n: are the notes of student
    :param sit: (optional value)Is the situation of student
    :return: Return a dictionary with several notes, average and the situation of student
    """
    s = 0
    mai = 0
    men = 0
    for v in n:
        s = s + v

        if mai == 0:
            mai = v
        else:
            if v > mai:
                mai = v

        if men == 0:
            men = v
        else:
            if v < men:
                men = v

    med = s / len(n)

    if med >= 7:
        si = 'Passed'
    elif 5 <= med < 7:
        si = 'Retake'
    else:
        si = 'disapproved'


    bulletin = {'total':len(n), 'highest':mai, 'lower':men, 'average':med}

    if sit == True:
        bulletin['situation'] = si

    return bulletin


r = bol(4, 5, 4, 3, 7, 10, sit=True)

print(r)

help(bol)