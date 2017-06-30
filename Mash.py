
from random import *
from timeit import default_timer as timer

start = timer()
input("Hit enter to Mash!")
# ...
end = timer()
elapse_time = int(end - start)


#Create the list of words you want to choose from.
Dogname_list = ["Buddy", "Chubby", "Candy", "Oscar", "Harley", "Lola", "Rocky","Apollo", "Romeo", "Deisel", "Otis", "Peanut", "Butter", "Skittle", "Twix", "Hershey", "Bruno", "Pineapple", "Kanye","Ramen", "Pablo"]
Location_list = ["Canada", "Seatle","Iowa", "Hawaii","Germany", "Trinidad", "New York", "Italy", "Dubai", "Paris"]
Age_list = ["20", "21", "23", "24","25","32","25","54","35","31","75","52","60","47","46","54"]
Mash = ["Manison", "Apartment", "Shack","House"]
Job = ["Computer Programmer", "Veteranarian", "Grocery Bagger", "CEO", "Tarantula Handler", "Movie Producer","Actres","Model","Fashion Designer","Assasin", "Ninja","Garbage Woman"]
Kids = range(0,15)
Transportation = ["Jeep", "Razor Scooter","Elephant","Mini Van","Vespa","Bart","Limo"]
Sallary = ["5k","10k","100k","1million", "10million","1 billion"]
Pet = ["Tarantula" , "Cat","Lion","Tiger","Turtle","Fish","Ferret"]
Pet_num = range(0,10)

#Generates a random integer.
d = elapse_time % len(Dogname_list)
l = elapse_time % len(Location_list)
a = elapse_time % len(Age_list)
m = elapse_time % len(Mash)
j = elapse_time % len(Job)
k = elapse_time % len(Kids)
t = elapse_time % len(Transportation)
s = elapse_time % len(Sallary)
p = elapse_time % len(Pet)
pn = elapse_time % len(Pet_num)
#l = #randint(0, len(Location_list)-1)
#a = #randint(0, len(Age_list)-1)
#m = #randint(0, len(Mash)-1)
#j = #randint(0, len(Job)-1)
#k = #randint(0, len(Kids)-1)
#t = #randint(0, len(Transportation)-1)
#s = #randint(0, len(Sallary)-1)
#p = #randint(0, len(Pet)-1)
#pn = #randint(0, len(Pet_num)-1)

#print (d , l , a)
print ("When you are", Age_list[a] ,"years old you will live in " ,Location_list[l],". You will live in a" ,Mash[m]  ,". You will work as a", Job[j] ,"and make", Sallary[s] ,"a year. You will get to your job by" ,Transportation[t] ,". You will have", str(Kids[k]) ,"kid/kids and", str(Pet_num[pn]), Pet[p],"s, and a dog named", Dogname_list[d] ,".")
