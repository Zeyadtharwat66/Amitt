import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
y=np.array([2,2.8,3.6,4.5])
theta_0=0 #w
theta_1=0 #b
alpha=0.01
num_iteration=100
sse_values=[] #store sum square error values for plotting
#Gradient descient
for i in range(num_iteration):
    #compute predictions
    y_pred=theta_0+theta_1*x
    #compute gradients
    d_theta_0=-2*np.sum(y-y_pred)
    d_theta_1=-2*np.sum((y-y_pred)*x)
    #update parameters
    theta_0 -=alpha*d_theta_0
    theta_1 -=alpha*d_theta_1
    sse=np.sum((y-y_pred)**2)
    sse_values.append(sse)
print(f"Iteration {3},SSE:{sse_values[2]}")
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(range(num_iteration), sse_values,label="SSE")
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
print(f"predict x = 6  ---->  {theta_0*(6)+theta_1}")