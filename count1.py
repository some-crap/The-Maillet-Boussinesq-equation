import math
import datetime
from datetime import date
year = input("year: ")
data = open(year + ".csv", "r")
lines = -1
for line in data:
    lines += 1
print(lines)
data.close()
with open(year + ".csv") as file:
    data = [line.rstrip() for line in file]
print(data[0])
alpha = input("Alpha = ")
alpha = float(alpha)
mu = input("Mu = ")
mu = float(mu)
H_plus_all = 0.0
w_total = 0.0
results = "alpha = " + str(alpha) + "\n" + "Mu = " + str(mu) + "\n" + "\n___________________________\n"
for i in range(1, lines):
	temp = data[i]
	temp = temp.split(";")
	#print(temp)
	if len(temp[0]) == 0 or len(temp[1]) == 0 or len(temp[2]) == 0 or len(temp[3]) == 0:
		continue
	temp1 = data[i+1]
	#print(temp1)
	temp1 = temp1.split(";")
	if len(temp1[0]) == 0 or len(temp1[1]) == 0 or len(temp1[2]) == 0 or len(temp1[3]) == 0:
		continue
	H_dr = temp[1]
	H0 = temp[3]
	H_dr = H_dr.split(",")
	H_dr = float(H_dr[0] + "." + H_dr[1])
	H0 = H0.split(",")
	H0 = float(H0[0] + "." + H0[1])
	H_dr1 = temp1[1]
	H_01 = temp1[3]
	H_dr1 = H_dr1.split(",")
	H_dr1 = float(H_dr1[0] + "." + H_dr1[1])
	#print("test = "+str(len(H_01))+"\n")
	H_01 = H_01.split(",")
	H_01 = float(H_01[0] + "." + H_01[1])
	Ht_real = H_01
	if Ht_real < H0:
		continue
	Dren = (H_dr + H_dr1)/2.0
	delta = 1
	t = 1
	Z = (H0-Dren) * (1 - math.exp(t * (-1)*alpha))
	Delta_H_see = Ht_real - H0
	w = (Z + Delta_H_see)*mu/t
	print("_________________\n")
	print("H0 = "+str(H0)+"\n"+"H1 = "+str(Ht_real)+"\n")
	print("W "+str(i)+": " + str(w))
	w_total += w
	print("Delta Z = " + str(Z))
	print("Delta H_see = " + str(Delta_H_see))
	print("H+ = " + str(Z + Delta_H_see))
	print("GW Supply = " + str(w))
	results = results + "\n_________________\n" + "Delta Z = " + str(Z) + "\nDelta H_see = " + str(Delta_H_see) + "\nH+ = " + str(Z + Delta_H_see) + "\nGW Supply = " + str(w) + "\n" + data[0] + "\n" + data[i] + "\n" + data[i+1] + "\n"
	H_plus_all += Z + Delta_H_see
f = open("results"+year+".txt", "w")
results = "H+ total: " + str(H_plus_all) + "\n" + "GW total supply: " + str(w_total) + "\n\n" + results
f.write(results)
f.close()
print("\n\n\nH+ total: " + str(H_plus_all) + "")
print("W total: " + str(w_total))
print("Resuts were saved to " + "results"+year+".txt")
input()
