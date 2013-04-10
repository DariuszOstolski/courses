import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    if n <= 0:
        raise ValueError, "n must be greater than or equal to 0"
    return int(math.ceil(n/50.0))


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    gains = 0
    losses = 0
    for price in price_changes:
      if price>0:
	gains += price
      else:
	losses += price
    return (gains, losses)
    
    

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    if k<0 or k>len(L):
      raise IndexError, "k must be greater than or equal to 0 and lower than %d"%(len(L))
    for i in range(k):
      j = len(L)-k+i
      L[i], L[j] = L[j], L[i]
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
