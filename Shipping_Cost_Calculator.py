#Shipping cost calculator 

## Input package weight and shipping rate
weight=float(input("enter the pakage in kilograms:"))
rate = float(input("enter the shipping rate per kilogram:"))

## Calculate shipping cost 
shipping_cost = weight *rate 

##Display the result 
print (f"Shipping Cost:{shipping_cost} USD")
