Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input("Enter your name: ")
Enter your name: LaDonna Emeli
>>> print("Hello " + name + "!")
Hello LaDonna Emeli!
>>> findword = input("What word would you like to replace?")
What word would you like to replace? Emeli
>>> replaceword = input("What is the new word?")
What is the new word? Denise Emeli
>>> newname = name.replace(findword, replaceword)
>>> print(newname)
LaDonna Denise Emeli
>>> friends = input("How many friends do you have?")
How many friends do you have? 4
>>> carrots = input("How many carrots do you have?")
How many carrots do you have? 0
>>> money = input("How many dollars do you have?")
How many dollars do you have? 5
>>> print("There are" + friends + "so there are 10 icecream scoops")
There are 4so there are 10 icecream scoops
>>> print("Everyone gets" + carrots + "carrots because there are no carrots")
Everyone gets 0carrots because there are no carrots
>>> print("Everyone pays $1 because the bill was" + money + "dollars and there are 5 people")
Everyone pays $1 because the bill was 5dollars and there are 5 people
>>> name = input("Enter your name: ")
Enter your name: LaDonna Emeli
>>> age = input("Enter your age: ")
Enter your age: 19
>>> findword = input("What word would you like to replace?")
What word would you like to replace? 19
>>> replaceword = input("What is the new word?")
What is the new word? 20
>>> sentence = "LaDonna Emeli, you will be" replaceword + "next year"
SyntaxError: invalid syntax
>>> print("LaDonna Emeli, you will be" replaceword + "next year"
      
SyntaxError: invalid syntax
>>> LaDonna you will be 20 next year
SyntaxError: invalid syntax
>>> name = input("What is your name?")
What is your name? LaDonna
>>> age = input("What is your age?")
What is your age? 19
>>> if age >= 18
SyntaxError: invalid syntax
>>> if age >= 18:
	print("You are elgible to vote")
	else :
		
SyntaxError: invalid syntax
>>> if age >= 18:
	print("You are elgible to vote")
else :
	print("You are not elgible to vote")
age > 18:
	
SyntaxError: invalid syntax
>>> age = > 18
SyntaxError: invalid syntax
>>> 