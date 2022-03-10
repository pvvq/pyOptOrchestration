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
    subprocess.run("./MD > output.txt", shell=True, cwd="target")

# retrive execution time
def time():
    f = open("target/output.txt")
    results = f.read()
    f.close()

    time = re.findall("timesteps took (\d+\.?\d*) seconds", results)
    return float(time[len(time) - 1])

# wrapper, compile, run, and get time
def measure(list_of_flags):
    separator = ' '
    flags = separator.join(list_of_flags)
    compile(flags)
    exec()
    return time()


first_touch = True
def record(name, value):
    global first_touch
    if first_touch:
        if os.path.exists("target/record.csv"):
            os.remove("target/record.csv")
        first_touch = False
    f = open("target/record.csv", "a+")
    f.write(name+','+str(value)+"\n")
    f.close()