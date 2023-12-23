from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route("/integration")
def integration():
    def numIntegration(lower, upper, N):
        X = np.linspace(lower, upper, N, endpoint=False)
        dx = X[1] - X[0]
        integral_sum = np.sum(np.abs(np.sin(X)) * dx)

        return integral_sum

    interval_lower = 0.0
    interval_upper = np.pi
    N = [10, 100, 1000, 10000, 100000, 1000000]
    integrals = []
    string = ""
    

    for n in N:
        integral = numIntegration(interval_lower, interval_upper, n)
        integrals.append(integral)
        string += f"N = {n}: {integral} <br>" 
        print(f"N = {n}: {integral}")

    

    return f"<p>{string}</p>"

if __name__ == '__main__':
    app.run(debug=True)
