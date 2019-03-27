import sys
d = {
        "start" : "starting",
        "stop"  : "stopping",
        "restart" : "stopping\nstarting"
    }
if len(sys.argv) > 1: 
    ans = sys.argv[1]
else:
    ans = raw_input("What do you want to do? ")

print d.get(ans, "You must enter start stop or restart")
# OR
if ans in d:
    print d[ans]
else:
    print "You must enter start stop or restart"


