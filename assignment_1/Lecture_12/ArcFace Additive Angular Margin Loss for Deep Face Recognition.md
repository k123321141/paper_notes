## Visualizing Data using t-SNE; The Journal of Machine Learning Research

### 要解決的問題

高維的轉換對於模型的能力有很大的幫助，但是人類並不適合解讀高維度的資料。</br>
如果想要做高維資料的視覺化處理，勢必要降維到人類熟悉的2D或是3D維度，而這部分有很多方式可以選擇，PCA LDA t-SNE等等</br>

### [PCA](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/PCA.md)

### SNE

降維的精神是，高維資料的特性在轉換過後的低維空間仍保持的某些特性，不同方法關注的性質不一樣。</br>
SNE利用Euclidean distance以及normal distribution去描述每兩兩個點之間的相似性，用kernel density描述點的相似性。</br>
換句話說，越相近的點，越有可能將彼此視為「鄰居」，而投影過後的資料可以看出，哪些資料點是「鄰居關係」，而看出群集關係。</br>
注意：這種描述法不適合做分群，k-means會是比較好的方式</br>

<a href="https://www.codecogs.com/eqnedit.php?latex=p_{\left&space;(&space;j&space;\mid&space;i&space;\right&space;)&space;}&space;=&space;\frac{\exp\left&space;(&space;-\left&space;\|&space;x_i-x_j&space;\right&space;\|^2&space;/&space;2\sigma&space;^2_i&space;\right&space;)}{\sum&space;_{k\neq&space;i}\exp&space;\left&space;(&space;-\left&space;\|&space;x_i-x_k&space;\right&space;\|^2&space;/&space;2\sigma&space;^2_i&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{\left&space;(&space;j&space;\mid&space;i&space;\right&space;)&space;}&space;=&space;\frac{\exp\left&space;(&space;-\left&space;\|&space;x_i-x_j&space;\right&space;\|^2&space;/&space;2\sigma&space;^2_i&space;\right&space;)}{\sum&space;_{k\neq&space;i}\exp&space;\left&space;(&space;-\left&space;\|&space;x_i-x_k&space;\right&space;\|^2&space;/&space;2\sigma&space;^2_i&space;\right&space;)}" title="p_{\left ( j \mid i \right ) } = \frac{\exp\left ( -\left \| x_i-x_j \right \|^2 / 2\sigma ^2_i \right )}{\sum _{k\neq i}\exp \left ( -\left \| x_i-x_k \right \|^2 / 2\sigma ^2_i \right )}" /></a></br>
上式的意思是，選定一個data point xi，根據Euclidean distance以及normal distribution，較近距離的xj有比較大的機率被挑到。</br>
其中normal distribution的標準差是根據每一個xi有不同的值，後述會討論如何設定。</br>

而降為過後的X -> Y，每一對data point應該要保持相似的關係，在低維空間中的Y直接統一將標準差設為1/√2，保持一致的分佈。</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=q_{\left&space;(&space;j&space;\mid&space;i&space;\right&space;)&space;}&space;=&space;\frac{\exp\left&space;(&space;-\left&space;\|&space;y_i-y_j&space;\right&space;\|^2&space;\right&space;)}{\sum&space;_{k\neq&space;i}\exp&space;\left&space;(&space;-\left&space;\|&space;y_i-y_k&space;\right&space;\|^2&space;\right&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?q_{\left&space;(&space;j&space;\mid&space;i&space;\right&space;)&space;}&space;=&space;\frac{\exp\left&space;(&space;-\left&space;\|&space;y_i-y_j&space;\right&space;\|^2&space;\right&space;)}{\sum&space;_{k\neq&space;i}\exp&space;\left&space;(&space;-\left&space;\|&space;y_i-y_k&space;\right&space;\|^2&space;\right&space;)}" title="q_{\left ( j \mid i \right ) } = \frac{\exp\left ( -\left \| y_i-y_j \right \|^2 \right )}{\sum _{k\neq i}\exp \left ( -\left \| y_i-y_k \right \|^2 \right )}" /></a></br>

假設共有N筆資料，每ㄧ個data point xi都有一個PDF去描述N筆資料，如何比較在X空間的N筆PDF與Y空間的N筆PDF之間的相似性？</br>
論文中選用Kullback-Leibler divergence。 注：不知道能不能用ISE
<a href="https://www.codecogs.com/eqnedit.php?latex=C=\sum&space;_iKL\left&space;(&space;P_i\parallel&space;Q_i&space;\right&space;)&space;=&space;\sum&space;_i\sum&space;_jp_{j\mid&space;i}\log&space;\frac{p_{j\mid&space;i}}{q_{j&space;\mid&space;i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C=\sum&space;_iKL\left&space;(&space;P_i\parallel&space;Q_i&space;\right&space;)&space;=&space;\sum&space;_i\sum&space;_jp_{j\mid&space;i}\log&space;\frac{p_{j\mid&space;i}}{q_{j&space;\mid&space;i}}" title="C=\sum _iKL\left ( P_i\parallel Q_i \right ) = \sum _i\sum _jp_{j\mid i}\log \frac{p_{j\mid i}}{q_{j \mid i}}" /></a></br>
由於KL-divergence不對稱: <br>
<a href="https://www.codecogs.com/eqnedit.php?latex=KL\left&space;(p_{i&space;\mid&space;j}&space;,&space;q_{j&space;\mid&space;i}&space;\right)&space;\neq&space;KL\left&space;(q_{i&space;\mid&space;j}&space;,p_{j&space;\mid&space;i}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?KL\left&space;(p_{i&space;\mid&space;j}&space;,&space;q_{j&space;\mid&space;i}&space;\right)&space;\neq&space;KL\left&space;(q_{i&space;\mid&space;j}&space;,p_{j&space;\mid&space;i}&space;\right)" title="KL\left (p_{i \mid j} , q_{j \mid i} \right) \neq KL\left (q_{i \mid j} ,p_{j \mid i} \right)" /></a></br>

當xi與xj很相近pij應該很大，p=0.8, 而投影的q錯誤了，q=0.2，cost=1.11</br>
另一種情況p=0.2，q=0.8，cost=-0.277</br>
也就是說當X空間很相近時，一定要找出來這種「鄰居」關係，而如果很遠可是錯認成「鄰居」的話沒關係。</br>
可以認爲會保留局部區域的關係。</br>

### 如何調整X空間的標準差？

標準差可以用來描述使用怎樣的normal distribution，這邊為每一個data point xi挑選適合的標準差。(這裡比較像variable KDE)</br>
在比較密集的X空間應該選用比較尖的高斯分佈，也就是比較小的標準差，文中利用perplexity去描述這個hyperparameter。</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=Perp(P_i)&space;=&space;2^{H(P_i)}&space;\\&space;H(P_i)&space;=&space;-\sum_j&space;p_{j&space;\mid&space;i}&space;\log_2&space;p_{j&space;\mid&space;i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Perp(P_i)&space;=&space;2^{H(P_i)}&space;\\&space;H(P_i)&space;=&space;-\sum_j&space;p_{j&space;\mid&space;i}&space;\log_2&space;p_{j&space;\mid&space;i}" title="Perp(P_i) = 2^{H(P_i)} \\ H(P_i) = -\sum_j p_{j \mid i} \log_2 p_{j \mid i}" /></a></br>
當給定了perplexity，在比較密集的區域就必須得出比較小的標準差。</br>

### 如何求解

有了cost function以後，推導一下利用SGD就可以解出，而文中有推導出最終的梯度表示法。</br>
其中還加入了optimizer的想法，透過加入momentum避免陷入local minima。</br>

那麼還需要如何改進？

### t-SNE
1. 首先SNE不足的地方在於asymmetric KL-divergence不好求解，所以替換成了symmetric loss</br>
2. crowding problem，當降維的低維空間時，不同群的資料卻擠在同一區域當中。</br>
當一個m維空間中，以xi為中心m維球的uniform分佈，當m增加時，其他點與xi的距離變化。(圖片來源自[1])</br>
![Alt text][1]</br>
隨著維度增加，大部分資料都聚集在m維球表面附近，如果將這種距離關係保持到低維空間就會造成crowding problem。</br>



### 





### 資料參考

http://www.datakit.cn/blog/2017/02/05/t_sne_full.html



[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_07/sne_crowding.png



