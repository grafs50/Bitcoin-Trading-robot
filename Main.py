import csv

reader= csv.reader(open("per_day_all_time_history(1).csv"))
prices = []

for column in reader:
    prices.append(column[3])
print(len(prices))
x=0
y=100

pricedifference= []
while x<len(prices)-2:
   price1=prices[y]
   price2=prices[y+1]

   pricedifference.append(((float(price2)-float(price1))/float(price1)))
   x+=1
   y+=1
   """Program crashes at this point due to an out of range index error"""

ln10change = []
n10change = []
n75change = []
n50change = []
n25change = []
p0change = []
p25change = []
p50change = []
p75change = []
plus10change = []
screwup = []

for x in pricedifference:
    if x<=(-.1)*(10^5):
        ln10change.append(x)

    elif x>-.1*(10^5) and x<=-.075*(10^5):
        n10change.append(x)

    elif x>-.075*(10^5) and x<=-.05*(10^5):
        n75change.append(x)

    elif x>-.05*(10^5) and x<=-.025*(10^5):
        n50change.append(x)

    elif x>-0.025*(10^5) and x<=0*(10^5):
        n25change.append(x)

    elif x>.0*(10^5) and x<=.025*(10^5):
        p0change.append(x)

    elif x>.025*(10^5) and x<=.05*(10^5):
        p25change.append(x)

    elif x>.05*(10^5) and x<=.075*(10^5):
        p50change.append(x)

    elif x>.075*(10^5) and x<=.1*(10^5):
        p75change.append(x)

    elif x>.1*(10^5):
        plus10change.append(x)

    else:
        screwup.append(x)


amount = len(ln10change)+len(n10change)+len(n75change)+len(n50change)+len(n25change)+len(p0change)+len(p25change)+len(p50change)+len(p75change)+len(plus10change)

print(pricedifference)
print("The probability that the values are more the -10% apart is " + str(len(ln10change)/amount))
print("The probability that the values are less the -10% apart and more than -7.5% is " + str(len(n10change)/amount))
print("The probability that the values are less than -7.5% apart and more than -5% apart is " + str(len(n75change)/amount))
print("The probability that the values are less than -5% apart and more than -2.5% apart is " + str(len(n50change)/amount))
print("The probability that the values are less than -2.5% apart and more than 0% apart is " + str(len(p0change)/amount))
print("The probability that the values are less than 2.5% apart and more than 0& apart is " + str(len(p25change)/amount))
print("The probability that the values are less than 7.5% apart and more than 5% apart is " + str(len(p50change)/amount))
print("The probability that the values are less than 10% apart and more than 7.5% apart is " + str(len(p75change)/amount))
print("THe probability that the values are more than 10% apart is " + str(len(plus10change)/amount))


