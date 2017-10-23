# noinspection PyUnusedLocal
def hello(friend_name):
	print type(friend_name[0])
	
	if type(friend_name[0]) != 'str':
		return friend_name

	return "Hello, World!"

if __name__ == '__main__':
    hello("ttt")
