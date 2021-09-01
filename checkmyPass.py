import requests
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f'Error fetching: {res.status_code}, check api and try again')
	return res

def pwned_api_check(password):
	# check password if it exists in api response
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	# print(sha1password.upper())
	first5_char, tail = sha1password[:5],sha1password[5:]
	print(first5_char, tail)
	response = request_api_data(first5_char)
	# print(response)
	return get_pwd_leaks_count(response, tail)

def get_pwd_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':')for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0


def main(args):
	for pas in args:
		count = pwned_api_check(pas)
		if count:
			print(f'{pas} was FOUND {count} time....you should probably chnge your password')
		else:
			print(f'{pas} was NOT FOUND, Carry On!!!!')
	return 'done!'

if __name__ == '__main__':
	main(sys.argv[1:])

	
