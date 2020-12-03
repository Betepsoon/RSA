from Crypto.Util.number import inverse


def output_rsa_parameter(n, e, p, c):
	'''

	:param n: 模数
	:param e: 公钥
	:param p: n的一个因数
	:param c: 密文
	:return: null
	'''
	q = n // p
	# 计算私钥
	fai_n = (p-1)*(q - 1)
	d = inverse(e,fai_n)
	# 解密
	plaintext = pow(c,d,n)
	print(f'p = {hex(p)}\nq = {hex(q)}\nn = {hex(n)} \ne = {hex(e)} \nd = {hex(d)}\nm ={hex(plaintext)}')

def rsa_verify(m,e,n,c):
	if pow(m,e,n) == c:
		print('本密文确实由消息m加密得到')
	else:
		print('Wrong!')