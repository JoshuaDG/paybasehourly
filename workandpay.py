# Joshua D. Gonzalez
# Calculates a person's pay based on hours 
# worked and pay rate.

'''
copy from other file
into this program to
print out what is the 
fastest running time
'''
print("welcome to run mate ")


def print_separator(width):
    print("-" * width)
    


print_separator(10)
print("Time   latitude   longitude   Distance   Pace " )
print("(hh:mm:ss)   (deg)   (deg)    (miles)   (mine/mile)")
print_separator(10)

filename = input("Enter the name of the file: ")

fileline = open(filename,"r")

for line in fileline:
    line = line.strip()
    if line != "":
        parts = line.split(" ")
        print(parts)
'''
fname = input("Enter the name of the file: ")
fvar = open(fname,"r")
for line in fvar:
    try:
        line = line.strip()
        if line != "":
            parts = line.split(" ")
            hours = float(parts[3])
            rate = float(parts[4])
            gross_pay = hours * rate
            if gross_pay < 0:
                print("You must have entered in garbage.")
            else:
                tax_rate = get_tax_rate(gross_pay)
                taxes = gross_pay * tax_rate
                net_pay = gross_pay - taxes
                print_paycheck(gross_pay, net_pay, taxes, tax_rate)
    except:
        print("You are a squirrely one. You hurt me. I don't like it.")
'''
