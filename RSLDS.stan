functions {
  real sigmoid(real a){
    return inv_logit(-a);
  }
}

data{
	int T;
	int N;
	int M;
	int K;
	int Nu;
	vector [T] y[N];
}

parameters{
  	matrix[M,M] A[K];
	//  	matrix[M] C[K];
	vector [K] C;
	vector [M] R[K];
	vector [M] b[K];
	vector [K] r;
	vector [M] x[N];
	real d[K];
	real <lower=0> s;//matrix [M,M] s;
	cholesky_factor_corr[M] corr_ch;	
	vector<lower=0> [M] sv;
}
transformed parameters{
  cholesky_factor_cov[M] cov_ch;			
  cov_ch<-diag_pre_multiply(sv,corr_ch);	
}

model{
  vector [K] z;

  for(j in 1:K){
    sv[j]~student_t(4,0,200);
  }
  s~student_t(4,0,200);	
  corr_ch~lkj_corr_cholesky(Nu);
  for(t in 1:T){
  for(i in 2:N){
      for(k in 1:K){
	target+=log(z[k])+multi_normal_cholesky_lpdf(x[i]|A[k]*x[i-1]+b[k],cov_ch) ;
	target+=log(z[k])+normal_lpdf(y[i,t]|C[k]*x[i]+d[k],s) ;
      }

      z[1]=sigmoid(dot_product(R[1],x[i])+r[1]);
      for(k in 2:K){
	z[k]=sigmoid(dot_product(R[k],x[i])+r[k]);
	for(kp in k:K){
	  z[k]=z[k]+sigmoid(-(dot_product(R[kp],x[i])+r[kp]));
	}
      }
      target+=log_sum_exp(log(z));	
  }	
  }
}

