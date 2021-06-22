def main():
    print(r'''
       Bill divider!
    
     // ""--.._
     ||  (_)  _ "-._
     ||    _ (_)    '-.
     ||   (_)   __..-'
      \\__..--""
    
''')
    total_price = float(input('Total price: '))
    total_people = int(input('How many people?: '))
    payment = total_price / total_people
    print('Each one has to pay', '$' + str(payment))
    quit()

main()




