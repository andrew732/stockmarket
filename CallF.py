import subprocess as sub
import threading
import time

class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        #self.p = sub.Popen(self.cmd)
	mytime=time.strftime("%Y-%m-%d")
	with open("/home/www/tweepy/Andrew/"+ mytime + ".txt", "w+") as output:
        	self.p = sub.Popen(self.cmd,stdout=output)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()      #use self.p.kill() if process needs a kill -9
            self.join()

RunCmd(["python", "/home/www/tweepy/Andrew/twitter_streaming.py"], 3600).Run()
