input = open("purchases.txt", "r")
output = open("01.txt", "w")

i=1
for line in input:
    datalist = line.strip().split("    ")
    date, time, store, item, cost, paymentType = datalist
    output.write(paymentType + "\t" + str(i) + "\n")

input.close()
output.close()
