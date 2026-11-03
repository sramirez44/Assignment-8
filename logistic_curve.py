
#  create the plot
st.title('Logisitic Curve')

st.latex(r"f(x) = \frac{e^{\beta_0 + \beta_1 x}}{1 + e^{\beta_0 + \beta_1 x}}")

beta0_st = st.slider('Beta 0', min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
beta1_st = st.slider('Beta 1', min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# generate data
x = np.linspace(-10, 10, 400)
numerator = np.exp(beta0_st + beta1_st * x)
y = numerator / (1 + numerator)

# plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color="red", linewidth=2)
ax.set_ylim(-0.05, 1.05)
ax.set_xlim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("Probability f(x)")
ax.grid(True, linestyle="--", alpha=0.6)

st.pyplot(fig)
