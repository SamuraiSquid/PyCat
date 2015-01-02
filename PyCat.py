import urllib2 #For getting fact from cat fact site
import json #For decoding JSON response
import time #For timing between sending facts
from googlevoice import Voice #For sending facts via Google Voice

print('        PyCat')
print('Written by SamuraiSquid')
print('------------------------')

timex = input('Time Between Facts(Seconds): ') #Ask for time between fact sending

print('Registering with Google SMS Gateway')
voice = Voice() #Initialize Google Voice
voice.login('Google_Voice_Email_Address_Here', 'Google_Voice_Password_Here') #Login to Google Voice
print('Registration Successful!')
print('---------------------------')
print('Loading Member Library')
f = open('numbers.list')#Open list of numbers to send the facts to
numbers = f.readlines()#Read the numbers into a list
f.close()
numofnums = len(numbers)#Get the number of numbers that will recieve CatFacts

print('Member Library Loaded - ' + str(numofnums) + ' Users Total')#Print the number of numbers that will revieve CatFacts

print('---------------------------')

def sendfact(number, fact):#This function will do the actual sending of the text message
    voice.send_sms(number, fact)#Send the fact(fact) to the recipient(number)

print('PyCat is Now Active!')
while True:
    time.sleep(timex)#Wait between sending messages
    userid = 0 #Reset list position
    while True:#Loop through list of recipient numbers until the last number is sent it's fact
        number = numbers[userid]#set number to the recipient's number
        userid = userid + 1 #Move up on the list of numbers
        f = urllib2.urlopen('http://catfacts-api.appspot.com/api/facts')#Fetch the JSON response from the CatFacts API
        json_string = f.read()#Read the fact from the API
        parsed_json = json.loads(json_string)#Parse the JSON response
        fact = parsed_json["facts"][0]#Extract the fact from the JSON response
        sendfact(number, fact)#Call the function sendfact to send the fact
        print('---------------------------')
        print('Sent: ' + number + ' - ' + fact)#Print the number and the fact sent to that number in the console
        print('---------------------------')
        if userid == numofnums:#Once the last number in the list is reached break the sending loop
            break
