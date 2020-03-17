# Coronavirus-Simulation
Simulate the spread of Coronavirus and perhaps predict the trend.

# Assumptions

- Each person picks `E` random people every day to interact with. However, real-world people are clustered. But there are [claims](https://www.youtube.com/watch?v=Kas0tIxDvrg) that in the clustered case, the underlying growth is still logistic.

  * Therefore, new cases `Δ N(t)` is roughly `E * P * N(t-1)`.
  
  * `E` is the number of others each person interactive with each day, and `P` is the probability of infection while interacting with someone.

- Infected people can not be infected again.

- Infected people have 10 days to interact with others before been discovered and quarantined.

- The virus infectivity in relate to the temparature (eg. Summer) has not been considered.

# Future work

- Fit the curve with real-world data. For instance, from [Coronavirus cases](https://www.worldometers.info/coronavirus/coronavirus-cases/) or from [RamiKrispin/Coronavirus Dashborad](https://github.com/RamiKrispin/coronavirus_dashboard).

# Plots
- 0.15

  <img src="/Plots/Plot_0.15.png" width="500"/>

- 0.145

  <img src="/Plots/Plot_0.145.png" width="500"/>

- 0.14

  <img src="/Plots/Plot_0.14.png" width="500"/>

- 0.135

  <img src="/Plots/Plot_0.135.png" width="500"/>
 
- 0.13

  <img src="/Plots/Plot_0.13.png" width="500"/>

- 0.125

  <img src="/Plots/Plot_0.125.png" width="500"/>
  
- 0.12

  <img src="/Plots/Plot_0.12.png" width="500"/>

- Newly infected + Total infected

  <img src="/Plots/Plot_0.14_with_total.png" width="500"/>
  

Note that when `E*P` is close to 0.1, the curse tends to be more unstable. Also note that when `E*P` is less than 0.1, then the expectation of the number each person infects other will be less than 1.
