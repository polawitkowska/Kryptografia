"""Autorem tego zadania jest Pola Witkowska"""
import os
import sys
import math
import secrets

def read_input_file(path):
	with open(path, "r", encoding="utf-8") as f:
		lines = [line.strip() for line in f if line.strip()]
	if not lines:
		raise ValueError("Plik wejściowy jest pusty")
	nums = [int(x) for x in lines]
	return nums

def write_output_file(path, content):
	with open(path, "w", encoding="utf-8") as f:
		f.write(str(content).strip() + "\n")

def decompose_power_of_two(m):
	s = 0
	d = m
	while d % 2 == 0 and d > 0:
		d //= 2
		s += 1
	return d, s

def try_mr_round_with_factor(n, a, d, s):
	x = pow(a, d, n)
	if x == 1 or x == n - 1:
		return False, None

	for _ in range(s):
		prev = x
		x = (x * x) % n
		if x == 1:
			g = math.gcd(prev - 1, n)
			if 1 < g < n:
				return True, g
			else:
				return True, None
		if x == n - 1:
			return False, None

	return True, None

def miller_rabin_with_optional_exponent(n, rounds=20, provided_exponent=None, find_factor=True):
	if n < 2:
		return True, None
	if n in (2, 3):
		return False, None
	if n % 2 == 0:
		return True, 2

	if provided_exponent is None:
		d, s = decompose_power_of_two(n - 1)
	else:
		if provided_exponent <= 0:
			d, s = decompose_power_of_two(n - 1)
		else:
			d, s = decompose_power_of_two(provided_exponent)

	tried = set()
	small_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]

	for a in small_bases:
		if a >= n:
			continue
		if math.gcd(a, n) != 1:
			return True, math.gcd(a, n)
		comp, factor = try_mr_round_with_factor(n, a, d, s) if find_factor else try_mr_round_with_factor(n, a, d, s)
		tried.add(a)
		if comp:
			return True, factor

	needed = max(0, rounds - len(tried))
	for _ in range(needed):
		if n - 3 <= 0:
			a = 2
		else:
			a = 2 + secrets.randbelow(n - 3)
		if a in tried:
			continue
		if math.gcd(a, n) != 1:
			return True, math.gcd(a, n)
		comp, factor = try_mr_round_with_factor(n, a, d, s) if find_factor else try_mr_round_with_factor(n, a, d, s)
		tried.add(a)
		if comp:
			return True, factor

	return False, None

def fermat_test(n, rounds=20):
	if n < 2:
		return False
	if n in (2, 3):
		return True
	if n % 2 == 0:
		return False
	for _ in range(rounds):
		if n - 3 <= 0:
			a = 2
		else:
			a = 2 + secrets.randbelow(n - 3)
		if math.gcd(a, n) != 1:
			return False
		if pow(a, n - 1, n) != 1:
			return False
	return True


def main():
	script_dir = os.path.dirname(os.path.abspath(__file__))
	in_path = os.path.join(script_dir, "wejscie.txt")
	out_path = os.path.join(script_dir, "wyjscie.txt")

	args = sys.argv[1:]
	fermat_only = (len(args) >= 1 and args[0] == "-f")

	nums = read_input_file(in_path)
	n = nums[0]

	if fermat_only:
		is_probably_prime = fermat_test(n, rounds=20)
		if is_probably_prime:
			write_output_file(out_path, "prawdopodobnie pierwsza")
		else:
			write_output_file(out_path, "na pewno złożona")
		return

	provided_exponent = None
	if len(nums) == 2:
		provided_exponent = nums[1]
	elif len(nums) >= 3:
		provided_exponent = nums[1] * nums[2] - 1

	if n % 2 == 0:
		write_output_file(out_path, 2)
		return

	if provided_exponent is not None and provided_exponent > 0:
		comp, factor = miller_rabin_with_optional_exponent(
			n, rounds=25, provided_exponent=provided_exponent, find_factor=True
		)
		if factor is not None and 1 < factor < n:
			write_output_file(out_path, factor)
			return
		if comp:
			write_output_file(out_path, "na pewno złożona")
			return

	comp, factor = miller_rabin_with_optional_exponent(n, rounds=20, provided_exponent=None, find_factor=True)
	if factor is not None and 1 < factor < n:
		write_output_file(out_path, factor)
		return
	if comp:
		write_output_file(out_path, "na pewno złożona")
	else:
		write_output_file(out_path, "prawdopodobnie pierwsza")


if __name__ == "__main__":
	main()