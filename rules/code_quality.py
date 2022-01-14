# ruleid:overusing-args
def function(args):
  args.updates = 1
  return args

# ok: overusing-args
def func(*args, **kwargs):
  acceptable = 1
  return acceptable

# ok: overusing-args
def func(*args):
  return 1
