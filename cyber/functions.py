import socket
import constants 
import sympy
from random import choice

def list_nums(message):
    tmp_msg = message[1:-1]
    ret_me = tmp_msg.split(constants.SEPARATOR)
    return ret_me


def get_ip():
    host = socket.gethostname()
    ret_me = socket.gethostbyname(host)
    return ret_me



def parse_string_data(message):
    nums = list_nums(message)
    readable_data = []
    for num in nums:
        readable_data.append(int(num))
    return readable_data

def turn_to_hex(message):
    new_message = ""
    for number in message.split("	"):
        new_message += "0x"
        new_message += number
        new_message += ",	"
    print(new_message)
    return new_message

def find_prime(bit_range):
    rang = 2 ** bit_range
    prime_list = []
    for i in range(2**(bit_range-1), rang):
        if sympy.isprime(i):
            prime_list.append(i)
    return choice(prime_list)

if __name__ == "__main__":
    print(get_ip())
    turn_to_hex('''52	09	6a	d5	30	36	a5	38	bf	40	a3	9e	81	f3	d7	fb
                10	7c	e3	39	82	9b	2f	ff	87	34	8e	43	44	c4	de	e9	cb
                20	54	7b	94	32	a6	c2	23	3d	ee	4c	95	0b	42	fa	c3	4e
                30	08	2e	a1	66	28	d9	24	b2	76	5b	a2	49	6d	8b	d1	25
                40	72	f8	f6	64	86	68	98	16	d4	a4	5c	cc	5d	65	b6	92
                50	6c	70	48	50	fd	ed	b9	da	5e	15	46	57	a7	8d	9d	84
                60	90	d8	ab	00	8c	bc	d3	0a	f7	e4	58	05	b8	b3	45	06
                70	d0	2c	1e	8f	ca	3f	0f	02	c1	af	bd	03	01	13	8a	6b
                80	3a	91	11	41	4f	67	dc	ea	97	f2	cf	ce	f0	b4	e6	73
                90	96	ac	74	22	e7	ad	35	85	e2	f9	37	e8	1c	75	df	6e
                a0	47	f1	1a	71	1d	29	c5	89	6f	b7	62	0e	aa	18	be	1b
                b0	fc	56	3e	4b	c6	d2	79	20	9a	db	c0	fe	78	cd	5a	f4
                c0	1f	dd	a8	33	88	07	c7	31	b1	12	10	59	27	80	ec	5f
                d0	60	51	7f	a9	19	b5	4a	0d	2d	e5	7a	9f	93	c9	9c	ef
                e0	a0	e0	3b	4d	ae	2a	f5	b0	c8	eb	bb	3c	83	53	99	61
                f0	17	2b	04	7e	ba	77	d6	26	e1	69	14	63	55	21	0c	7d''')

