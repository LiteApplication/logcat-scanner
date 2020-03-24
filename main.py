#!/usr/bin/python3

from gotlougit import main

###########################
version = 0.2
LOG_FILE_1 = "logcat_1.log.txt"
LOG_FILE_2 = "logcat_2.log.txt"
LOG_FILE_COMMON = "logcat_c.log.txt"
###########################

print(f"Welcome to Logcat-Scanner v{version}\n by Gotlou and LiteApplication")
log1_file = open(LOG_FILE_1, 'r')
log1 = log1_file.read()
log1_file.close()

log2_file = open(LOG_FILE_2, 'r')
log2 = log2_file.read()
log2_file.close()

log1 = main.removeTimeStamp(log1)
log2 = main.removeTimeStamp(log2)

common = main.compareLog(log1, log2)
with open(LOG_FILE_COMMON, "w") as f:
    f.writelines(common)
print("Done.")


