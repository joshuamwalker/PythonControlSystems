from filterdesign_tf_coeffs import filterdesign_tf_coeffs

data = [1+2j, 2*np.exp(1j)]

# extract real and imaginary parts
x = [ele.real for ele in data]
y = [ele.imag for ele in data]

# plot the complex numbers
fig = plt.figure(figsize=(6, 6))

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# plt.scatter(x, y)
# plt.ylabel('Imaginary')
# plt.xlabel('Real')
# plt.show()
# plt.xlim([-1, 1])
# plt.ylim([-1, 1])
axlim = 3

ax1.set_title('Plot Window')
ax1.scatter(x, y, color='blue', marker='x')
ax1.set_xlim(-axlim, axlim)
ax1.set_ylim(-axlim, axlim)

ax2.set_title('Truncated view')
ax2.scatter(x, y, color='red')
ax2.set_xlim(-axlim, axlim)
ax2.set_ylim(-axlim, axlim)

# ax2.set_xlim([25, 50])

plt.show()
