# noinspection PyUnusedLocal
letter_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
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
	f_price = 10
	g_price = 20
	h_price = 10
	i_price = 35
	j_price = 60
	k_price = 70
	l_price = 90
	m_price = 15
	n_price = 40
	o_price = 10
	p_price = 50
	q_price = 30
	r_price = 50
	s_price = 20
	t_price = 20
	u_price = 40
	v_price = 50
	w_price = 20
	x_price = 17
	y_price = 20
	z_price = 21

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
	
	total_price = total_price + (f_price * int(skus.count("F") / 3) * 2) + (f_price * (skus.count("F") % 3))
	total_price = total_price + g_price * skus.count("G")	

	five_h_price = (h_price * int(skus.count("H") / 10) * 10 - int(skus.count("H") / 10) * 20)
	left_h_count = skus.count("H") - int(skus.count("H") / 10) * 10
	three_h_price = (h_price * int(left_h_count / 5) * 5 - int(left_h_count / 5) * 5)
	double_left_h_count = left_h_count - int(left_h_count / 5) * 5
	total_price = total_price + five_h_price + three_h_price + h_price * double_left_h_count

	total_price = total_price + i_price * skus.count("I")	
	total_price = total_price + j_price * skus.count("J")	
	total_price = total_price + 120 * int(skus.count("K") / 2) + k_price * (skus.count("K") % 2)
	total_price = total_price + l_price * skus.count("L")	
	
	m_count = 0
	m_count += skus.count("N") / 3
	real_m_count = 0
	if skus.count("M") > 0:
		if m_count > skus.count("M"):
			real_m_count = 0
		else:
			real_m_count = skus.count("M") - m_count
	else:
		real_m_count = 0

	total_price = total_price + m_price * real_m_count
	total_price = total_price + n_price * skus.count("N")
	total_price = total_price + o_price * skus.count("O")

	total_price = total_price + 200 * int(skus.count("P") / 5) + p_price * (skus.count("P") % 5)

	q_count = 0
	q_count += skus.count("R") / 3
	real_q_count = 0
	if skus.count("Q") > 0:
		if q_count > skus.count("Q"):
			real_q_count = 0
		else:
			real_q_count = skus.count("Q") - q_count
	else:
		real_q_count = 0


	total_price = total_price + q_price * real_q_count - 10 * int(real_q_count / 3)

	total_price = total_price + r_price * skus.count("R")
	
	total_price = total_price + (u_price * int(skus.count("U") / 4) * 3) + (u_price * (skus.count("U") % 4))

	five_v_price = (v_price * int(skus.count("V") / 3) * 3 - int(skus.count("V") / 3) * 20)
	left_v_count = skus.count("V") - int(skus.count("V") / 3) * 3
	three_v_price = (v_price * int(left_v_count / 2) * 2 - int(left_v_count / 2) * 10)
	double_left_v_count = left_v_count - int(left_v_count / 2) * 2
	total_price =  total_price + five_v_price + three_v_price + v_price * double_left_v_count

	total_price = total_price + w_price * skus.count("W")
	
	total_price = total_price + s_price * skus.count("S")
	total_price = total_price + t_price * skus.count("T")
	total_price = total_price + x_price * skus.count("X")
	total_price = total_price + y_price * skus.count("Y")
	total_price = total_price + z_price * skus.count("Z")

	list_str = list["STXYZ"]
	for it in letter_list:
		if it not in list_str:
			skus = skus.replace(it, "")

	extra_count = int(len(sku) / 3)
	last_index = len(sku) - extra_count * 3
	sku = sku[-last_index:]
	return total_price

if __name__ == '__main__':
    print checkout("ABCDE")
