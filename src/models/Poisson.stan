//Poisson Model
data {
    int N; 
    int<lower=0> y[N]; 
}
parameters{
    real<lower=0> lambda; 
}
model {
    //Gamma prior on lambda shape and scale 
    //Recall in Green beta is given as rate
    lambda ~ gamma(25.0, 10.0); 
    y ~ poisson(lambda); 
}
generated quantities {   
	real logModel; 	
	logModel = poisson_lpmf(y | lambda) + gamma_lpdf(lambda|25.0, 10.0); 
}