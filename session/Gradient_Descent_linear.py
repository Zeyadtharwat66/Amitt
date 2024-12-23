import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([2,2.8,3.6,4.5])
theta_0 = 0
theta_1 = 0
alpha = 0.01
num_iterations = 100
sse_values=[] # some square errors
for i in range(num_iterations):
    y_pred=theta_0 + theta_1 * x
    d_theta_0=-2 * np.sum(y-y_pred)
    d_theta_1=-2 * np.sum((y-y_pred)*x)
    #update parameters
    theta_0 -= alpha*d_theta_0
    theta_1 -= alpha*d_theta_1
    #compute SSE and store it
    sse=np.sum((y-y_pred)**2)
    sse_values.append(sse)
    if (i+1) %100 ==0:
        print(f"Iterations {i+1},SSE: {sse}")


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(range(num_iterations), sse_values,label="SSE")
plt.xlabel('Iteration')
plt.ylabel('SSE')
plt.title('SEE over Iterations')
plt.legend()
plt.subplot(1,2,2)
plt.scatter(x,y,color='blue',label='Data points')
plt.plot(x,theta_0+theta_1 *x,color='red',label='Regression line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.tight_layout()
plt.show()