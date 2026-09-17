
guest_list = ['Isaac Snr.', 'Uduak', 'Henry']

message1 = f" Hello {guest_list[0]}, I would like to invite you to dinner with the rest of the family!"

message2 = f" Hello {guest_list[1]}, I would like to invite you to dinner with the rest of the family!"

message3 = f" Hello {guest_list[2]}, I would like to invite you to dinner with the rest of the family!"


print(message1)
print(message2)
print(message3)


print( f"Hello everyone!, {guest_list[2] } will not be able to make it to dinner.")

guest_list.pop(2)

new_guest = 'Emmanuel'

guest_list.append(new_guest)


message1 = f" Hello {guest_list[0]}, I would like to invite you to dinner with the rest of the family!"

message2 = f" Hello {guest_list[1]}, I would like to invite you to dinner with the rest of the family!"

message3 = f" Hello {guest_list[2]}, I would like to invite you to dinner with the rest of the family!"


print(message1)
print(message2)
print(message3)

print( f"Hello everyone! I have found a bigger table for dinner, so i will be inviting more guests to dinner.")

guest_list.insert(0 , 'Aniebet')

guest_list.insert(2 , 'Israela')

guest_list.append('Amaifiok')

message1 = f" Hello {guest_list[0]}, I would like to invite you to dinner with the rest of the family!"

message2 = f" Hello {guest_list[1]}, I would like to invite you to dinner with the rest of the family!"

message3 = f" Hello {guest_list[2]}, I would like to invite you to dinner with the rest of the family!"

message4 = f" Hello {guest_list[3]}, I would like to invite you to dinner with the rest of the family!"

message5 = f" Hello {guest_list[4]}, I would like to invite you to dinner with the rest of the family!"

message6 = f" Hello {guest_list[5]}, I would like to invite you to dinner with the rest of the family!"

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)

print( f" Hello everyone!, I regret to inform you all that the bigger table will not arrive in time for dinner, and as a result, I can only invite 2 guests!")


print(f" Hello {guest_list[5]}, sorry I will not be able to host you for dinner anymore.")
guest_list.pop()

print(f" Hello {guest_list[4]}, sorry I will not be able to host you for dinner anymore.")
guest_list.pop()

print(f" Hello {guest_list[3]}, sorry I will not be able to host you anymore for dinner.")
guest_list.pop()

print(f"Hello {guest_list[2]}, sorry I will not be able to host you for dinner anymore.")
guest_list.pop()
print(f"Hello {guest_list[1]}, you are still invited to tonight's dinner.")
print(f"Hello {guest_list[0]}, you are still invited to tonight's dinner.")


# exercise 3-9

lenofg = len(guest_list)

message = f"I will only be inviting {lenofg} guests to tonight's dinner."

print(message)



del guest_list[1]
del guest_list[0]

print(guest_list)
