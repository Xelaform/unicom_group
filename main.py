# put your python code here
s = "abch12345h"
print(s[: s.find("h")] + s[s.rfind("h"): s.find("h"): -1] + s[s.rfind("h"):])
