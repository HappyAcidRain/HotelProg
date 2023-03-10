import matplotlib.pyplot as plt

# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# Setting Y-axis limits
gnt.set_ylim(0, 80)

# Setting X-axis limits
gnt.set_xlim(0, 62)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('Даты')
gnt.set_ylabel('Номера')

#yt hf,jnftn
# changing diamentionshe
#gnt.set_figwidth(52)
#gnt.set_figheight(20)


# Setting ticks on x-axis
gnt.set_xticks([2, 4, 6, 8, 10, 12, 14, 16,
                18, 20, 22, 24, 26, 28, 30,
                32, 34, 36, 38, 40, 42, 44,
                46, 48, 50, 52, 54, 56, 58,
                60, 62])

# Labelling tickes of x-axis
gnt.set_xticklabels(["2", "", "", "", "", "", "", "16",
                     "", "", "", "", "", "28", "", "1",
                     "", "", "", "", "", "15", "", "",
                     "", "", "", "", "", "31", ""])

# Setting ticks on y-axis
gnt.set_yticks([5, 15, 25, 35, 45, 55, 65, 75])

# Labelling tickes of y-axis
gnt.set_yticklabels(['1', '2 ', '3', '4', '5', '6', '7', '8'])

# Setting graph attribute
gnt.grid(True)


def rum_calc(x):
    if x == 1:
        return 0

    elif x == 2:
        return 10

    elif x == 3:
        return 20

    elif x == 4:
        return 30

    elif x == 5:
        return 40

    elif x == 6:
        return 50

    elif x == 7:
        return 60

    elif x == 8:
        return 70

    else:
        return "Error, this room doesn't exist"


def ins_cust(start_time, end_time, room, color):

    duration = int(end_time) - int(start_time)
    row = rum_calc(room)

    # добавление в график данных
    gnt.broken_barh([(start_time, duration)], (row, 10), facecolors=f'tab:{color}')


ins_cust(10, 31, 4, 'blue')

ins_cust(25, 34, 6, 'orange')

ins_cust(12, 41, 5, 'red')

plt.savefig("gant.png")
