### OSX

1. clone libsvm from https://github.com/cjlin1/libsvm

2. make in libsvm dir, to generate binary executable file.(svm-predict, svm-train, svm-scale.)

3. make in python dir under libsvm, to generate library file libsvm.so.2, under libsvm dir.

4. mv libsvm.so.2 to system path.</br>
I move it to '/Library/Python/2.7/Library/Python/2.7/'

5. cp svm.py  svmutil.py to python path, make it callable to python shell.</br>
I choose '/Library/Python/2.7/site-packages/'</br>

### ubuntu

1. clone libsvm from https://github.com/cjlin1/libsvm

2. make in libsvm dir, to generate binary executable file.(svm-predict, svm-train, svm-scale.)

3. make in python dir under libsvm, to generate library file libsvm.so.2, under libsvm dir.

4. mv libsvm.so.2 to python path.</br>
I move it to '/usr/lib/python2.7/'</br>

5. cp svm.py  svmutil.py to python path, make it callable to python shell.</br>
I choose '/Library/Python/2.7/site-packages/'</br>


### Manual

#### Hard margin

If problem in X space is linear separable, in dual Lagrange form.</br>
hard margin : <a href="https://www.codecogs.com/eqnedit.php?latex=\max_{&space;0&space;\leq&space;\alpha&space;_n\leq&space;C,\beta_n=C-\alpha_n}&space;\&space;\&space;\max_{b,w}&space;\&space;\&space;\&space;w^Tw&space;&plus;&space;\sum^N_{n=1}\alpha_n(1-y_n(w^Tx_n&plus;b))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\max_{&space;0&space;\leq&space;\alpha&space;_n\leq&space;C,\beta_n=C-\alpha_n}&space;\&space;\&space;\max_{b,w}&space;\&space;\&space;\&space;w^Tw&space;&plus;&space;\sum^N_{n=1}\alpha_n(1-y_n(w^Tx_n&plus;b))" title="\max_{ 0 \leq \alpha _n\leq C,\beta_n=C-\alpha_n} \ \ \max_{b,w} \ \ \ w^Tw + \sum^N_{n=1}\alpha_n(1-y_n(w^Tx_n+b))" /></a>


