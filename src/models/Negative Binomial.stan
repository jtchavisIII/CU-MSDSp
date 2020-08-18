//Negative Binomial Model
data {
    int N; 
    int<lower=0> y[N]; 
}
parameters{
    real<lower=0> lambda;
    real<lower=0> kappa;  
}
model {
    //Gamma prior on lambda shape and scale 
    //Recall in Green beta is given as rate
    lambda ~ gamma(25, 10); 
    kappa ~ gamma(1,10); 
    y ~ neg_binomial_2(lambda, 1/kappa); 
}
generated quantities {   
    real logModel; 
    logModel = neg_binomial_2_lpmf(y | lambda, 1/kappa) + gamma_lpdf(lambda|25.0, 10.0) + gamma_lpdf(kappa|1.0,10.0); 
}