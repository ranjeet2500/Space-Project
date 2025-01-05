 #This is the program to calulate the distance between planets
import streamlit as st

dis=[36,67,92,141,483,890,1784,2793,3700]
min_tm=[-290,820,-128,-225,-260,-280,-370,-360,-387]
max_tm=[800,900,134,70,-150,-170,-320,-328,-369]

def planet_lookup(planet_name):
    if planet_name=="mercury":
        distance=dis[0]
    elif planet_name=="venus":
        distance=dis[1]
    elif planet_name=="earth":
        distance=dis[2]
    elif planet_name=="mars":
        distance=dis[3]
    elif planet_name=="jupiter":
        distance=dis[4]
    elif planet_name=="saturn":
        distance=dis[5]
    elif planet_name=="uranus":
        distance=dis[6]
    elif planet_name=="neptune":
        distance=dis[7]
    elif planet_name=="pluto":
        distance=dis[8]
    else:
        print ("Please enter the 1st planet correctly or check the spelling!")
        exit()
    return distance

def temp_lookup(planet_name):
    if planet_name=="mercury":
        min_temp=min_tm[0]
        max_temp=max_tm[0]
    elif planet_name=="venus":
        min_temp=min_tm[1]
        max_temp=max_tm[1]
    elif planet_name=="earth":
         min_temp=min_tm[2]
         max_temp=max_tm[2]
    elif planet_name=="mars":
         min_temp=min_tm[3]
         max_temp=max_tm[3]
    elif planet_name=="jupiter":
         min_temp=min_tm[4]
         max_temp=max_tm[4]
    elif planet_name=="saturn":
         min_temp=min_tm[5]
         max_temp=max_tm[5]
    elif planet_name=="uranus":
         min_temp=min_tm[6]
         max_temp=max_tm[6]
    elif planet_name=="neptune":
         min_temp=min_tm[7]
         max_temp=max_tm[7]
    elif planet_name=="pluto":
         min_temp=min_tm[8]
         max_temp=max_tm[8]
    else:
        print ("Please enter the 1st planet correctly or check the spelling!")
        exit()
    return min_temp , max_temp

#planet_name1=input("Input the name of the first planet [all lowercase]")
planet_name1=st.text_input("Input the name of the first planet [all lowercase]")

distance_p1=planet_lookup(planet_name1)
planet1_min_temp,planet1_max_temp=temp_lookup(planet_name1) 
planet1_avg_temp=float((planet1_min_temp+planet1_max_temp)/2)

#planet_name2=input("Input the name of the second planet [all lowercase]")
planet_name2=st.text_input("Input the name of the second planet [all lowercase]")

distance_p2=planet_lookup(planet_name2)
planet2_min_temp,planet2_max_temp=temp_lookup(planet_name2)
planet2_avg_temp=float((planet2_min_temp+planet2_max_temp)/2)


#print("the distance of "+planet_name1+" from sun is "+str(distance_p1)+" million miles")
#print("the mininum temperature of "+planet_name1+" is "+str(planet1_min_temp)+" degrees fahrenheit, while the maxinum temperature of "+planet_name1+" is "+str(planet1_max_temp)+" degrees fahrenheit")
#print("the average temperature of " +planet_name1+" is "+str(planet1_avg_temp)+" degrees fahrenheit.")

#print("the distance of "+planet_name2+" from sun is "+str(distance_p2)+" million miles")
#print("the mininum temperature of "+planet_name2+" is "+str(planet2_min_temp)+" degrees fahrenheit, while the maxinum temperature of "+planet_name2+" is "+str(planet2_max_temp)+" degrees fahrenheit")
#print("the average temperature of " +planet_name2+" is "+str(planet2_avg_temp)+" degrees fahrenheit.")

st.write("1. The distance of "+planet_name1+" from sun is "+str(distance_p1)+" million miles")
#st.write("the mininum temperature of "+planet_name1+" is "+str(planet1_min_temp)+" degrees fahrenheit, while the maxinum temperature of "+planet_name1+" is "+str(planet1_max_temp)+" degrees fahrenheit")
#st.write("the average temperature of " +planet_name1+" is "+str(planet1_avg_temp)+" degrees fahrenheit.")
st.write("2. The distance of "+planet_name2+" from sun is "+str(distance_p2)+" million miles")
#st.write("the mininum temperature of "+planet_name2+" is "+str(planet2_min_temp)+" degrees fahrenheit, while the maxinum temperature of "+planet_name2+" is "+str(planet2_max_temp)+" degrees fahrenheit")
#st.write("the average temperature of " +planet_name2+" is "+str(planet2_avg_temp)+" degrees fahrenheit.")

dis_bet=abs(distance_p1-distance_p2)
st.write("3. The distance between " +planet_name1+ " and "+planet_name2+ " is "+str(dis_bet)+" million miles")