# noinspection PyUnusedLocal
def hello(friend_name):
	if isinstance(friend_name[0], str) == False:
		print friend_name
		return

	print "Hello, World!"