import sys
import pandas as pd
import numpy as np

def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        df = pd.read_csv(input_file)
    except:
        print("Error: File not found")
        sys.exit(1)

    if df.shape[1] < 3:
        print("Error: File must contain at least 3 columns")
        sys.exit(1)

    data = df.iloc[:, 1:]

    try:
        data = data.astype(float)
    except:
        print("Error: Criteria must be numeric")
        sys.exit(1)

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        print("Error: Number of weights and impacts must match criteria")
        sys.exit(1)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    s_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = s_minus / (s_plus + s_minus)

    df['Topsis Score'] = score
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)

    print("TOPSIS calculation completed successfully")

if __name__ == "__main__":
    main()
