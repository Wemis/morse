import os
import sys
from rich import print

os.system("clear") 
os.system("bash Banner/bluat.sh") 

test={}
test["1"]=" .---- "
test["2"]=" ..--- "
test["3"]=" ...-- "
test["4"]=" ....- "
test["5"]=" ..... "
test["6"]=" -.... "
test["7"]=" --... "
test["8"]=" ---.. "
test["9"]=" ----. "
test["0"]=" ----- "
test["a"]=" .- "
test["b"]=" -... "
test["c"]=" -.-. "
test["d"]=" -.. "
test["e"]=" . "
test["f"]=" ..-. "
test["g"]=" --. "
test["h"]=" .... "
test["i"]=" .. "
test["j"]=" .--- "
test["k"]=" -.- "
test["l"]=" .-.. "
test["m"]=" -- "
test["n"]=" -. "
test["o"]=" --- "
test["p"]=" .--. "
test["q"]=" --.- "
test["r"]=" .-. "
test["s"]=" ... "
test["t"]=" - "
test["u"]=" ..- "
test["v"]=" ...- "
test["w"]=" .-- "
test["x"]=" -..-"
test["y"]=" -.-- "
test["z"]=" --.. "
test["."]=" .-.-.- "
print("[1] Text to morse") 
print("[2] Morse code") 
print("[3] About") 
print("[4] Subscribe Wemis on Github") 
print("[5] Exit") 
option=input("Choose option: ") 

if option == "1":
	t=input("input text some text... ") 
	print("characters:",len(t),''.join([test.get(i,i) for i in t]))
if option == "2":
	print(test) 

if option == "3":
	os.system("clear") 
	print("[bold orange] This is a morse translator tool. This tool created by Wemis. Subscribe please on GinHub https://github.com/Wemis ") 
	print("Good luck!") 

if option == "4":
	os.system("termux-open https://github.com/Wemis") 

if option == "5":
	sys.exit() 
if option == "69":
	os.system("termux-open https://pornhub.com") 

else:
	print("")
