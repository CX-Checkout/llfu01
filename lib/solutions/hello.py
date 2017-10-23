# noinspection PyUnusedLocal
def hello(friend_name):
	print isinstance(friend_name, str)
	if isinstance(friend_name, str) == False:
		print friend_name
		return

	print "Hello, World!"
