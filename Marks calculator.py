print("ENTER 0 IF YOU HAVE NOT RECEIVED ANY OF THESE MARKS")
midMarks=int(input("ENTER YOUR MID TERM MARKS IN THE SUBJECT(out of 50)- "))
intMarks=int(input("ENTER YOUR INTERNAL MARKS IN THE SUBJECT(out of 40)- "))
endMarks=int(input("ENTER YOUR END SEM MARKS IN THE SUBJECT(out of 100)- "))

mid_grand_Marks=((midMarks*2)/100)*30
end_grand_Marks=(endMarks/100)*30

if endMarks==0:
    target=int(input("ENTER TARGET MARKS(CHOOSE BETWEEN 70,80 OR 90)- "))
    if target==70:
        Req1=((70-(mid_grand_Marks+intMarks))/30)*100
        print("Marks required to get to 70 are- ",Req1, "out of 100")
    elif target==80:
        Req2=((80-(mid_grand_Marks+intMarks))/30)*100
        print("Marks required to get to 80 are- ",Req2,"out of 100")
    elif target==90:
        Req3=((90-(mid_grand_Marks+intMarks))/30)*100
        print("Marks required are- ",Req3,"out of 100")
    elif target==60:
        Req4=((60-(mid_grand_Marks+intMarks))/30)*100
        print("Marks required are- ",Req4,"out of 100")
elif endMarks!=0:
    print("Grand total is", mid_grand_Marks+end_grand_Marks+intMarks)

