odeEuler <- function(f, y0, rho, alpha, tm) {
  y <- rep(0, length(tm))
  y[1] = y0
  for (n in 1:(length(tm)-1)) {
    y[n+1] = y[n] + f(y[n], rho, alpha)*(tm[n+1]-tm[n])
  }

  return(y)
}

sir <- function(I, rho, alpha) {
  dI <- rho*I*(1-I)-alpha*I
  return(dI)
}

sir <- function(tm, state, parameters) {
  with(as.list(c(state, parameters)), {
         dI <- rho*I*(1-I)-alpha*I
         return(list(c(dI)))
  })
}

init <- c(I=1e-6)
parameters <- c(rho=1.5, alpha=0.9)
times <- seq(0, 50, by=1)

library(deSolve)
out <- ode(y=init, times=times, func=sir, parms=parameters)
plot(out[, "time"], out[, "I"], type="l")

rho = 1.5
alpha = 1.9
tm = seq(0, 50, by=1)

I0=0.001
out <- odeEuler(sir, I0, rho, alpha, tm)
plot(out, type="l")
abline(h=1-alpha/rho, col="red")
