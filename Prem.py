import platform, os
 
def __main__():
  try:
    __import__('ig').__file__()
  except Exception as e:
    exit(f"\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m {e}")
if __name__=='__main__':
  if '32bit' in str(platform.architecture()):
    __main__()
  else:
    exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Use 32bit Device")
 
