# Write your greet function definition below:
def greet(name):
  return 'Hello, ' +name+'!'

  

# Any code inside the if statement will be ignored by the automarker.
# Put your test code in here, since it will be run by clicking Run or Terminal.
if __name__ == '__main__':
  print(greet('World'))	
  print(greet('Grok'))
  print(greet('123'))		

def test():
  return print('test')

def call():
	print('call')

call()