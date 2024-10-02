#TIP CALCULATOR AND SPLITING BILL
print ("welcome to the tip caluculator!" )
bill =float(input("what is your bill ? $" +""))
print (f"your total bill is ? {bill}")
tip= int(input("whats the peercentage of bill you woulde liem to give 10 12 15" +""))
people= int( input("how many people had lunch"+ ""))
bill_with_tip= tip /100 *bill + bill
print (bill_with_tip)
bill_per_person= bill_with_tip /people
final_bill =round (bill_per_person, 2)
print(f"each person need to pay: ${final_bill}")