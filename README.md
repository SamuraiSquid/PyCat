PyCat
=====

A Python prgram for sending cat facts to people via SMS

PyCat uses Google Voice to send facts about everybody's favorite feline to anyone with a text message capable device.
The facts are pulled from the Cat Facts API (http://catfacts-api.appspot.com/)

To use this program simply add the phone numbers of those you want to recieve the facts to the numbers.list, and put each
number on a seperate line; the phone numbers must be 10 digits only (XXX-XXX-XXXX). This program uses Google Voice so you
will have to sign up for Google Voice at voice.google.com (using just a normal google account).

In the PyCat.py file on line 14 make sure to add your Google account information so that the program can actually
send the messages, the email must be a full email address (whatever@gmail.com).

You must have the following modules installed; GoogleVoice (https://code.google.com/p/pygooglevoice/), urllib2, json, and 
time.

This program is built for Python 2.7.9

I am not responsible for what you do with this program, please make sure to abide by all applicable laws, and TOS 
aggreements.
