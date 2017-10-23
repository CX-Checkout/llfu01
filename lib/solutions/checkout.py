# noinspection PyUnusedLocal
letter_list = ["A","B","C","D", "E"]
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

    total_price = total_price + a_price * skus.count("A")
    total_price = total_price + b_price * skus.count("B")
    total_price = total_price + c_price * skus.count("C")
    total_price = total_price + d_price * skus.count("D")

    if skus.count("A") >= 3:
    	total_price -= 20 * int(skus.count("A") / 3)

    if skus.count("B") >= 2:
    	total_price -= 15 * int(skus.count("B") / 2)

    return total_price
