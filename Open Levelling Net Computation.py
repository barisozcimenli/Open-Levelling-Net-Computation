#Barış Özçimenli - ID: 010210616
#Geo108E Term Project - Open Levelling Net Computation


import math
print(">>>")
print("This program calculates the elevations in open levelling net")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")


#Input part

ID_Point = [input("Enter the point ID of known point: ")]
elevation= []
Elevation_of_point = float(input(f"Enter the elevation of point {ID_Point[0]} (m): "))
elevation.append(Elevation_of_point)
Number_of_unknown_points = int(input("Enter the number of unknown points: "))
i = 0
while i < Number_of_unknown_points:
    ID_Point.append(input(f"Enter the point ID of unknown point {i + 1} : "))
    i += 1
i = 0
BS = []
FS = []
while i < Number_of_unknown_points:
    BS += [float(input(f"Enter the BS reading of point {ID_Point[i]} (m) : "))]
    FS += [float(input(f"Enter the FS reading of point {ID_Point[i + 1]} (m) : "))]
    i += 1

#Calculations

Deltah_list = []
for x in range(0,Number_of_unknown_points):
    delta_h = (BS[x] - FS[x])
    deltaf_h = format(delta_h, ".3f")
    Deltah_list.append(deltaf_h)


for y in range(len(ID_Point)-1):
    Elevation_of_point+= float(Deltah_list[y])
    Elevation_of_pointf = format(Elevation_of_point, ".3f")
    elevation.append(Elevation_of_pointf)


#Output adjustments

print(">>>")
print(format("Point ID", "<10s"), format("Point ID", "<10s"), format("Delta H", "<10s"))
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
b = 0
for b in range (len(ID_Point)-1):
    b_1 = format(str(ID_Point[b]), "<10s")
    b_2 = format(str(ID_Point[b+1]), "<10s")
    b_3 = format(str(Deltah_list[b]), "<10s",)
    print(b_1,b_2,b_3, sep="")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

print(format("Point ID", "<10s"),format("Elevation","<10s"), sep="")
print("−−−−−−−−−−−−−−−−−−−")

for e in range(1,len(ID_Point)):
    b_4 = format(str(ID_Point[e]), "<10s")
    b_5 = format(str(elevation[e]), "<10s")
    print(b_4,b_5,sep="")
print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")




















