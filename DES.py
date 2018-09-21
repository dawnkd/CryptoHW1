import numpy as np

box0 = np.array([
[1,0,3,2],
[3,2,1,0],
[0,2,1,3],
[3,1,3,2]
])
box1 = np.array([
[0,1,2,3],
[2,0,1,3],
[3,0,1,0],
[2,1,0,3]
])
key_test = np.array([1,0,1,0,1,0,1,0,1,0])

def gen_keys(key):
	p10 = key[[2,4,1,6,3,9,0,8,7,5]]
	first_half = np.roll(p10[:5],-1)
	second_half = np.roll(p10[5:],-1)
	k1 = np.concatenate((first_half,second_half))[[5,2,6,3,7,4,9,8]]
	first_half_2 = np.roll(first_half,-1)
	second_half_2 = np.roll(second_half,-1)
	k2 = np.concatenate((first_half_2,second_half_2))[[5,2,6,3,7,4,9,8]]
	return (k1,k2)

def s_box(input_bits, box):
	col = 2 * input_bits[1] + input_bits[2]
	row = 2* input_bits[0] + input_bits[3]
	return [box[row,col] //2, box[row,col]%2]
	

def f_func(input_bits, key):
	expanded = input_bits[[3,0,1,2,1,2,3,0]]
	xor = expanded ^ key
	s0 = s_box(xor[:4],box0) 
	s1 = s_box(xor[4:],box1)
	return np.concatenate((s0,s1))[[1,3,2,0]]

def apply(input_bits, key, encrypt):
	k1,k2 = gen_keys(key);
	permuted = input_bits[[1,5,2,0,3,7,4,6]]
	first_half = permuted[:4]
	second_half = permuted[4:]
	#print(first_half.dtype)
	#print(f_func(second_half,k1).dtype)
	first_xor = first_half ^ f_func(second_half,  k1 if encrypt else k2)
	second_xor = second_half ^ f_func(first_xor, k2 if encrypt else k1)
	combined = np.concatenate((second_xor,first_xor))
	return combined[[3,0,2,4,6,1,7,5]]
