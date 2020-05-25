import datetime
import colorama

class Logger:
    def __init__(self, logfile="logfile.txt"):
        self.SUCCESS = 1
        self.FAIL = 2
        self.WARNING = 3
        self.logfile = logfile

    def message(self, message, success):
        msg = ""
        time = datetime.datetime.now()
        timestamp = "[%s%s%s:%s%s%s]" % (time.year, time.month, time.day,
                                            time.hour,time.minute,time.second)

        if(success == self.SUCCESS):
            msg = "SUCCESS : %s\n" % message
        elif(success == self.WARNING):
            msg = "WARNING : %s\n" % message
        else:
            msg = "FAIL : %s\n" % message

        logmsg = "%s %s" % (timestamp, msg)

        with open(self.logfile, "w+") as f:
            f.write(logmsg)

        print(logmsg)