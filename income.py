import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file

app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    data_source = []
    with open("income.txt", "r") as f:
        header = f.readline().strip().split(",")
        next(f)
        for line in f:
            lines = line.strip().split(",")
            all_lines = []
            for element in lines:
                all_lines.append(int(element.replace(" ", "")))
                data_source.append(all_lines)
    df = pd.DataFrame(data_source)
    df.columns = [header[0], header[1], header[2], header[3]]
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)