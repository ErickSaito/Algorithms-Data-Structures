def floyd(x0: int, f) -> (int, int):
  turtle, hare = f(x0), f(f(x0))
  while (turtle != hare):
    turtle, hare = f(turtle), f(f(hare))
  
  mu, hare = 0, x0
  while (turtle != hare):
    turtle, hare = f(turtle), f(hare)
    mu += 1
  
    l, hare = 1, f(turtle)
    while (turtle != hare):
      hare = f(hare)
      l += 1
    
    return mu, l


# Tests
def f(x):
  return (3*x + 1) % 4

assert floyd(7, f) == (1, 2)