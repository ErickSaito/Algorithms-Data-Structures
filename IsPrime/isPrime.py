def is_prime(n:int) -> bool:
  if (n > 1):
    for i in range(2, int(n ** (1/2)) + 1):
      if (n % i == 0):
        return False

    return True

  return False