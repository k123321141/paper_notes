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
I move it to '/usr/lib/python2.7/dist-packages/'</br>
hint: use sys.path to get dirs which python include. 

5. cp svm.py  svmutil.py to python path, make it callable to python shell.</br>
I choose '/Library/Python/2.7/site-packages/libsvm/'</br>
