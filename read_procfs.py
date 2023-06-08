try:
  with open('/proc/self/status') as f:
    print(f.read())
except Exception as e:
  print(f"An error occurred: {e}")
