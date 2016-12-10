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
	vector [T] y[N];
}

parameters{
  	cov_matrix[M] A[K];
	//  	cov_matrix[M] C[K];
	vector [K] C;
	vector [M] R[K];
	vector [M] b[K];
	vector [K] r;
	vector [M] x[N];
	matrix [M,M] q;
	real d[K];
	real s;//matrix [M,M] s;
}


model{
  matrix[M,M] scale;
  vector [K] z;
  scale<-diag_matrix(rep_vector(1.0,M)); 
  for(j in 1:M){
    A[j]~inv_wishart(M,scale);
    //    C[j]~inv_wishart(M,scale);
  }

  for(t in 1:T){
  for(i in 2:N){
      for(k in 1:K){
	lp__<-lp__+log(z[k])+multi_normal_log(x[i],A[k]*x[i-1]+b[k],q) ;
	lp__<-lp__+log(z[k])+normal_log(y[i,t],C[k]*x[i]+d[k]  ,s) ;
      }

      z[1]<-sigmoid(dot_product(R[1],x[i])+r[1]);
      for(k in 2:K){
	z[k]<-sigmoid(dot_product(R[k],x[i])+r[k]);
	for(kp in k:K){
	  z[k]<-z[k]+sigmoid(-(dot_product(R[k],x[i])+r[k]));
	}
      }
      lp__<-lp__+log_sum_exp(log(z));
  }	
  }
}

