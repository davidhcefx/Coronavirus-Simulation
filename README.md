# Coronavirus-Simulation
Simulate the spread of Coronavirus and perhaps predict the trend.

# Assumptions

- Each person picks `E` random people every day to interact with. However, real-world people are clustered. But there are [claims](https://www.youtube.com/watch?v=Kas0tIxDvrg) that in the clustered case, the underlying growth is still logistic.

- Infected people can not be infected again.

- Infected people have 10 days to interact with others before been discovered and quarantined.

# Future work

- Fit the curve with real-world data. For instance, from [coronavirus_dashboard](https://github.com/RamiKrispin/coronavirus_dashboard).

# Plots
- 0.15

  <img src="/Plots/Plot_015.png" width="500"/>

- 0.145

  <img src="/Plots/Plot_0145.png" width="500"/>

- 0.14

  <img src="/Plots/Plot_014.png" width="500"/>

- 0.135

  <img src="/Plots/Plot_0135.png" width="500"/>
 
- 0.13

  <img src="/Plots/Plot_013.png" width="500"/>

- 0.125

  <img src="/Plots/Plot_0125_1.png" width="500"/>
  <img src="/Plots/Plot_0125_2.png" width="500"/>

- 0.12

  <img src="/Plots/Plot_012.png" width="500"/>
  <img src="/Plots/Plot_012_2.png" width="500"/>
  <img src="/Plots/Plot_012_3.png" width="500"/>
  
Note that when `E*P` is close to 0.1, the curse tends to be more unstable. Also note that when `E*P` is less than 0.1, then the expectation of the number each person infects other will be less than 1.
