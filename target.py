# execute the targrt exectable and get execution time
# the function `exec` and `time` should be customizedd
# based on your target program

import subprocess
import re
import os

def get_opts():
    # read optimization flag from text file
    f = open("target/opt.txt")
    lines = f.read()
    f.close()
    if os.path.exists("target/record.csv"):
        os.remove("target/record.csv")

    # return [line.replace(" \n", "") for line in lines if line != ""]
    return re.findall("(-\S*)", lines)

def compile(flags):
    # gcc $flag -fopt-info -fsanitize=address MD.c control.c util.c -o MD -lm >> result.txt 2>&1
    # ./MD > test.txt
    # grep timesteps test.txt >> result.txt
    subprocess.run("gcc-11 " + flags + \
        " MD.c control.c util.c -o MD -lm", shell=True, cwd="target")

# execute target executable
def exec():
    subprocess.run("./MD > result.txt", shell=True, cwd="target")

# retrive execution time
def time():
    f = open("target/result.txt")
    results = f.read()
    f.close()

    time = re.findall("timesteps took (\d+\.?\d*) seconds", results)
    f = open("target/record.csv", "a+")
    f.write(time[len(time) - 1]+"\n")
    f.close()
    return float(time[len(time) - 1])