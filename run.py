import os
if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("Hannan").Main_()._no_vpn()
   except Exception as e:
       exit(str(e))
