def checker():
    l = [
        0,
        0.07,
        0.16,
        0.27,
        0.37,
        0.48,
        0.59,
        0.7,
        0.81,
        0.91,
        1.02,
        1.13,
        1.23,
        1.34,
        1.45,
        1.55]

    for i in l:
        print (str(round(i-0.0001, 5)).replace(".",","))
        print (str(round(i, 5)).replace(".",","))
    for k in range (0,15):
        print (k)
        print (k)
start = 0
while start < 2.50:
    start += 0.1
    print(str(round(start, 2)))

while start > 0:
    start -= 0.1
    print(str(round(start, 2)))

if __name__ == '__main__':
    checker()
