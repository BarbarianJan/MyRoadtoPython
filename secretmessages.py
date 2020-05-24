alphabet = 'abcdefghijklmnopqrstuvwyxz'
key = int(input('Please enter an cipher key: '))
newmessage = ''

message = input('Please enter a message: ')


for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newposition = (position + key) %26
    newcharacter = alphabet[newposition]
    #print('Your ciphered letter is: '+ newcharacter)
    newmessage += newcharacter
  else:
    newmessage += character
  
print('Your new message is: ', newmessage)
  

