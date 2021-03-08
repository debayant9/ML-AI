## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- y
- absolutely
- for sure
- yes yes yes
- definitely
- yes, it did.
- yes sure
- yeah sure
- did it help
- y\nexport

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- n
- N
- No Please
- No,Please
- Not
- don't
- don't like this
- do not
- try again
- try searching again
- please search again

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- Bye
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- good night
- have a nice day
- i'm off
- see you later
- we'll speak soon
- we will meet again
- end
- finish

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- good afternoon
- dear sir
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi Mr.
- hi pal!
- hi friend
- hi pal
- hi baby
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- who are you?
- what are you?
- what's up
- how do you do?
- How you doing?
- How are you doing?
- hi

## intent:other_topics
- what is the weather in bangalore
- what are you doing?
- do you not get it?
- do you not understand?

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [Lucknow](location)
- i am looking for an [South Indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- Oh, sorry, in [Delhi](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican](cuisine)
- [Lucknow](location) [Italian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find me restaurant in [delhi](location)
- can you find me restaurant in [delhi](location)
- [South Indian](cuisine)
- I'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- i'm looking for a place in the [Lucknow](location) of town
- show me [chinese](cuisine) restaurants
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [North Indian](cuisine) spot
- search for restaurants
- anywhere in the [Chennai](location)
- I am looking for [Thai](cuisine) food
- I am hungry
- Can you tell me a place to eat?
- I need food
- Food near [delhi](location)
- Food near me
- what are some good restraunts in [Delhi](location)
- suggest me some good [chinese](cuisine) place
- suggest me a good place to eat
- where can i get best [Italian](cuisine)
- where can I find best [Chinese](cuisine) in [Pune](location)?
- best [North Indian](cuisine) in [Bangalore](location)?
- i want to eat [South Indian](cuisine)
- best [Mexican](cuisine) in [delhi](location)
- what are the best [Italian](cuisine) in [delhi](location)
- i feel like having [Chinese](cuisine)
- i would like to have some [North Indian](cuisine)
- best [North Indian](cuisine) near me
- i am feeling hungry
- tell me the nearest [Chinese](cuisine) place
- i want a [Chinese](cuisine)
- where can i get [Chinese](cuisine) in [chennai](location)
- can you recommend some good [continental](cuisine) place in [mysore](location)
- Actually, I want to eat [pasta](cuisine) in [chennai](location)
- can you suggest good [Chinese](cuisine) place in [chennai](location)?
- [South Indian](cuisine) in [gurugram](location)
- [South Indian](cuisine) in [gurgaon](location)
- restaurant
- [delhi](location)
- [chinese](cuisine)
- [lesser than 300](Lesser than Rs 300)
- [Lesser than Rs 300](Lesser than Rs 300)
- [kolkata](location)
- [Chinese](cuisine:chinese)
- [More than Rs 700](budget)
- [Behrampur](location)
- find me a restaurant

## intent:tells_emailid
- [debayant9@gmail.com](mail)
- My email id is [debayant9@gmail.com](mail)
- yes. Please send it to [xyz@sth.edu](mail)
- yes. Please send it to [ahbcdj@dkj.com](mail)
- [debayant9@gmail.com](mail)
- [kirtirajchaudhary@gmail.com](mail)
- [kirtirajchaudhary@gmail.com](mail)
- [kirtirajchaudhary@gmail.com](mail)

## synonym: Cheap
- Lesser than 300

## synonym: High
- more than 700

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:Gurgaon
- gurugram

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:kolkata
- Calcutta

## synonym:mid
- moderate

## synonym:moderate
- 300 to 700

## synonym:mysore
- Mysuru

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:greet
- hello[^\s]*
- hey[^\s]*
- hi[^\s]*

## regex:pincode
- [0-9]{6}

## regex:tells_emailid
- @{1}
