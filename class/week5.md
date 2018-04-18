
basis 越多 表示redundent -> overcomplete </br>
每一個representation是多個解</br>

### k-means clusterinng 與 sparse coding
k-means 注重在分群，僅關心與群中心的距離，不關心與其他類別的差異量。</br>
由於使用norm 0，無法得出與其他群的差異量，有點像one-hot encoding。</br>
it's called 'Hard assignment'</br>

sparse coding也透過norm 1使得coding output, vi 非常sparse，與k-means結果類似。</br>
但是由於多重解的關係，一定程度上的避免over-fitting，相對於k-means，相當於從附近幾個類似的群中心取linear combination。</br>
it's called 'Soft assignment'</br>

### norm, l1,l2,l0 

norm1 的最佳解通常在頂點上，形成spase 的解。</br>
而 l0更極端

