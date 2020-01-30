packageurl <- 'https://cran.r-project.org/src/contrib/Archive/SPAtest/SPAtest_3.0.0.tar.gz'
install.packages(packageurl, repos=NULL, type="source")
packages <- c("Rcpp", "RcppArmadillo", "RcppParallel", "data.table", "RcppEigen", "Matrix", "optparse", "BH", "SKAT", "MetaSKAT")
install.packages(packages, repos="http://cran.us.r-project.org")
