import requests
import hashlib
import sys


def request_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Oh, snap!. There was an {res.status_code} error')
  return res

def get_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, leaks in hashes:
    if h == hash_to_check:
      return leaks
  return 0


def pwned_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first_five_char, tail = sha1password[:5], sha1password[5:]
  response = request_data(first_five_char)

  return get_leaks_count(response, tail)


def main(args):
  for password in args:
    leaks = pwned_check(password)
    if leaks:
      print(f"The password: {password} was found {leaks} times... It's time to change it!")
    else:
      print(f"Sleep tight, your password '{password}' was NOT found. Still, this does not mean that your password is secure")
  return '...done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))