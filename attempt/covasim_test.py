import covasim as cv
cv.options(jupyter=True, verbose=0)

sim = cv.Sim()
msim = cv.MultiSim(sim)
msim.run(n_runs=5)
msim.plot(dpi=1000)
