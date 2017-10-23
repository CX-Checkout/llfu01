# noinspection PyUnusedLocal
letter_list = ["A","B","C","D"]
def illegal_input(item_list):
	for it in letter_list:
		item_list = item_list.replace(it, "")

	if len(item_list) != 0:
		return True
	else:
		return False

def checkout(skus):
    if illegal_input(skus) == True:
    	return -1

    total_price = 0
    sku_list = list(skus)
    a_price = 50
    b_price = 30
    c_price = 20
    d_price = 15

    
if __name__ == '__main__':
    checkout("A")
    checkout("A")
    checkout("A")
