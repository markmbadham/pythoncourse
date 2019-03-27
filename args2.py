
#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    arg = input("enter stop|start|restart: ")
else:
    arg = sys.argv[1]
out = {
    "start" : "starting",
    "stop" : "stopping",
    "restart" : "stopping\nstarting"
}
print out.get(arg,"usage: stops|start|restart")
