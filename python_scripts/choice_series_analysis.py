import sqlite3 as lite
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

import statsmodels.api as sm
import statsmodels.tsa.arima_process as arima

con = lite.connect("everscape.db")
with con:
    cur = con.cursor()
    cur.execute("\
        SELECT * FROM Time_choice3\
        ORDER BY session_id ASC, mmss ASC;\
    ")
    rows = cur.fetchall()

data = {}

for row in rows:
    if not row[0] in data:
        data[row[0]] = [[], []]
    data[row[0]][0].append(row[2])
    data[row[0]][1].append(row[3])

def plot_series():
    for session_id in range(12):
        choice_series = np.array(data[session_id][1])
        order =  np.array(range(len(choice_series)))

        choice_time_series = pd.Series(choice_series, index=order)

        choice_time_series.plot()

        plt.show()

def fit_arma():
    #cannot predict a binary series
    session_id = 5
    choice_series = np.array(data[session_id][1])
    dates = sm.tsa.datetools.dates_from_range('1980m1',\
        length = len(choice_series))

    choice_time_series = pd.Series(choice_series, index=dates)
    arma_mod = sm.tsa.ARMA(choice_time_series, order=(2, 0))
    arma_res = arma_mod.fit(trend='nc', disp=-1)
    print(arma_res)

def one_step_reg():
    equal = 0
    diff = 0
    for session_id in range(12):
        choice_series = data[session_id][1]
        memory = choice_series[0]
        token = 0
        for choice in choice_series:
            if token == 0:
                token = 1
                continue
            if choice == memory:
                equal += 1
            else:
                diff += 1
            memory = choice

    print(str(float(equal)/float(equal + diff)))

def one_step_reg_naive(session_id):
    equal = 0
    diff = 0
    choice_series = data[session_id][1]
    memory = choice_series[0]
    token = 0
    for choice in choice_series:
        if token == 0:
            token = 1
            continue
        if choice == memory:
            equal += 1
        else:
            diff += 1
        memory = choice
    return (float(equal)/float(equal + diff))

def one_step_reg(session_id, lag):
    equal = 0
    diff = 0
    choice_series = data[session_id][1]
    dates = data[session_id][0]
    for i in range(len(dates)):
        s = str(dates[i])
        sec = int(s[:-4])*60 + int(s[-4:-2])
        dates[i] = sec
    time_series = dates
    memory = choice_series[0]
    time_memory = time_series[0]
    token = 0
    i = 0
    for choice in choice_series:
        if token == 0:
            token = 1
            i += 1
            continue

        if  time_series[i] > (time_memory + lag):
            print( str(time_series[i]) + " > " +\
            str(time_memory + lag))
            time_memory = time_series[i]
            i += 1
            memory = choice
            continue
        if choice == memory:
            equal += 1
        else:
            diff += 1
        memory = choice
        i += 1
    return (float(equal)/float(equal + diff))

def time_base_reg(session_id, span):
    print("in function")
    equal = 0
    diff = 0
    counter = 0
    dates = data[session_id][0]
    for i in range(len(dates)):
        s = str(dates[i])
        sec = int(s[:-4])*60 + int(s[-4:-2])
        print(str(dates[i]) + " becomes " + str(sec))
        dates[i] = sec

    choice_series = zip(data[session_id][0], data[session_id][1])
    nb_choice = len(data[session_id][0])
    memory = []
    for choice in choice_series:
        print("iterating over series")
        time_now = choice[0]
        if len(memory) == 0:
            memory.append(choice)
            continue
        cursor = memory[0]
        while memory and cursor[0] < time_now - span:
            memory.pop(0)
            if memory:
                cursor = memory[0]
        print(str(len(memory)))
        if len(memory) != 0:
            counter += 1
            score = 0.0
            for mem_choice in memory:
                if mem_choice[1] == choice[1]:
                    score += 1.0
                else:
                    score -= 1.0
            if score >= 0:
                equal += 1
            else:
                diff += 1
        memory.append(choice)
    print(" %f rendered" % (float(counter) / float(nb_choice)))
    return (float(equal)/float(equal + diff))

sessions = range(12)
stat = []
for session_id in range(12):
    stat.append(one_step_reg(session_id, 60))

print(sessions)
plt.plot(sessions, stat)
plt.show()

