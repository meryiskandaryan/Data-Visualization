import sqlite3
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

connection = sqlite3.connect('data_db.db')
c = connection.cursor()

c.execute("DROP TABLE IF EXISTS two_values")

c.execute("CREATE TABLE two_values (id int,value1 int, value2 int, value3 int, value4 int, value5 int, value6 int, value7 int, avg float)")

i = 0
a = 0


while True:
	i += 1
	a = np.random.randint(low=1,high=7, size=7)
	c.execute("INSERT INTO two_values values ({},{},{},{},{},{},{},{},{})".format(*np.append(np.append(i,a),a.mean())))
	connection.commit()

	time.sleep(0.5)

