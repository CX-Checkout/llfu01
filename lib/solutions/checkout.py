# noinspection PyUnusedLocal
letter_list = ["A","B","C","D", "E", "F"]
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
	e_price = 40
	e_price = 10

	five_a_price = (a_price * int(skus.count("A") / 5) * 5 - int(skus.count("A") / 5) * 50)
	left_a_count = skus.count("A") - int(skus.count("A") / 5) * 5
	three_a_price = (a_price * int(left_a_count / 3) * 3 - int(left_a_count / 3) * 20)
	double_left_a_count = left_a_count - int(left_a_count / 3) * 3
	total_price =  five_a_price + three_a_price + a_price * double_left_a_count

	b_count = 0
	b_count += skus.count("E") / 2
	real_b_count = 0
	if skus.count("B") > 0:
		if b_count > skus.count("B"):
			real_b_count = 0
		else:
			real_b_count = skus.count("B") - b_count
	else:
		real_b_count = 0

	total_price = total_price + b_price * real_b_count - 15 * int(real_b_count / 2)
	total_price = total_price + c_price * skus.count("C")
	total_price = total_price + d_price * skus.count("D")
	total_price = total_price + e_price * skus.count("E")

	return total_price

if __name__ == '__main__':
    print checkout("ABCDE")
