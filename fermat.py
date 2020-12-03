# 对frame10的数据进行了分解
import gmpy2
from rsa_package import common
from Crypto.Util.number import inverse


def fermat_divide_number(n: int):
	a = gmpy2.iroot(n, 2)
	a_value = a[0] + 1
	while True:
		temp = a_value * a_value - n
		b = gmpy2.iroot(temp, 2)
		if b[1]:
			break
		a_value += 1
	return a_value - b[0], a_value + b[0]


if __name__ == '__main__':
	'''
	frame 10 
	'''
	number = int(
		'85A0AC7E685995D9F8012C3A0249491956697997BBB6E5DDC1B53DC6184A843C3E4EB9B2D97FEAFAD097AA0FF640846287953C88F5A0813FD81FF3EBBDD62D66F4403653DCEC64ACE99F9FAAED4FD35513214EF4B4B9AA910E5923CD87F9330E3599F2CF1AD90EFC6BDABBD249D1AC8CF83836FE18399379E712010FC25A3DA3',
		16)
	p, q = fermat_divide_number(number)
	e = int('10001', 16)
	d = inverse(e, (p - 1) * (q - 1))
	ciphertext = int(
		'704A43957AC6D55375FE290CEBA686277B617AE3A013BA998C7475F161A72C4C0820F3A6A2D9474DF3CE86D6B78B50814F6710DAF8338B9880A8ED05CC498098AE299905BDDDAF05423765070ADF71E8CC43103D8E813A9EA8E5027091360DE30D925369DF9085066392166961D70E5AF868B75FD78227F8E603E5790A89058C',
		16)
	plaintext = pow(ciphertext, d, p * q)
	common.output_rsa_parameter(number, e, p, ciphertext)

	'''解密结果为 'will get' '''
