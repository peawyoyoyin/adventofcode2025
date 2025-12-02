def list_assert(l1, l2):
  assert len(l1) == len(l2), f'list has different lengths: {len(l1)} vs {len(l2)} \nfull lists:\n{l1}\nvs\n{l2}'
  
  for i, p in enumerate(zip(l1, l2)):
    a, b = p
    assert a == b, f'index {i} has different value: {a} vs {b}, \nfull lists:\n{l1}\nvs\n{l2}'