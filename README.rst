**Project created on SocialWifi hackathon**


========================
Install on vitual env
========================
python setup.py install


========================
Description
========================
Alfa version contain email guessing by name in emial.
In future I plan to add next modules that guess bu surname and nickname.

========================
Example of use
========================
import email_guesser.name_guesser as name_guesser

a = name_guesser.NameGuesser("olgamalkowska@gmail.com")
a.guess()

========================
How to run test
========================
In test folder run:
python -m unittest
