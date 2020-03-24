#!/usr/bin/python3

from gotlougit import main as m

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

log1 = m.removeTimeStamp(log1)
log2 = m.removeTimeStamp(log2)

log1 = log1.split('\n')
log2 = log2.split('\n')

common = m.compareLog(log1, log2)

for i in range(len(common)):
    common[i] += '\n'

with open(LOG_FILE_COMMON, "w") as f:
    f.writelines(common)
print("Done.")


