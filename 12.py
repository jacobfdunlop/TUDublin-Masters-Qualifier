pointlead = int(input("Please enter the point lead: "))
pointlead -= 3
posession = input("Does the winning team have possession? y/n ")

if posession == "y":
    pointlead = float(pointlead + 0.5)

else:
    pointlead = float(pointlead - 0.5)

if pointlead < 0:
    pointlead = 0

pointlead = round(int(pointlead ** 2))

time = int(input("How many seconds remain: "))

if pointlead > time:
    print("The Lead is safe")

else:
    print("The lead is not safe")
