
## Iterative Quantization: A Procrustean Approach to Learning Binary Codes
## Yunchao Gong and Svetlana Lazebnik

相關先備筆記 [PCA](https://github.com/k123321141/paper_notes/blob/master/week_1/PCA.md)

### Abstract

這篇論文主要想解決的問題在圖片的降維編碼
以應付資料儲存以及快速搜尋的應用

其中有幾點要求：

1.
編碼的長度必須夠短以節省空間。

2.
降維後的二維編碼能夠快速進行相似度運算。二維碼的Hamming distance需要在圖片相似度上有負相關

3.
比現有的large-scale indexing方法，更為簡單的演算法及資料結構。編碼一個新的圖片需要有效率。


### ITQ
論文提出的方法，將降維過後的資料，並不限於PCA(unsupervised)或是CCA(supervised embeddings)等方法，
以最小化quantization error轉換到binary hypercube的頂點上

使用論文中的notation 
<a href="https://www.codecogs.com/eqnedit.php?latex=\left&space;\{&space;x_1,&space;x_2,...,x_n&space;\right&space;\}&space;,&space;x&space;\in&space;\mathbb{R}^d&space;,&space;X\in&space;\mathbb{R}^{n\times&space;d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left&space;\{&space;x_1,&space;x_2,...,x_n&space;\right&space;\}&space;,&space;x&space;\in&space;\mathbb{R}^d&space;,&space;X\in&space;\mathbb{R}^{n\times&space;d}" title="\left \{ x_1, x_2,...,x_n \right \} , x \in \mathbb{R}^d , X\in \mathbb{R}^{n\times d}" /></a>
與assumption 
<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{i=1}^{n}x_i&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{i=1}^{n}x_i&space;=&space;0" title="\sum_{i=1}^{n}x_i = 0" /></a>
透過PCA降維得到<a href="https://www.codecogs.com/eqnedit.php?latex=V&space;=&space;XW&space;,W&space;\in&space;\mathbb{R}^{d&space;\times&space;c}&space;,&space;V&space;\in&space;\mathbb{R}^{n\times&space;c}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V&space;=&space;XW&space;,W&space;\in&space;\mathbb{R}^{d&space;\times&space;c}&space;,&space;V&space;\in&space;\mathbb{R}^{n\times&space;c}" title="V = XW ,W \in \mathbb{R}^{d \times c} , V \in \mathbb{R}^{n\times c}" /></a>

做完降維之後，encode的每一個x輸出長這樣<a href="https://www.codecogs.com/eqnedit.php?latex=v&space;\in&space;\mathbb{R}^c&space;,&space;sgn(v)&space;\in&space;\left&space;\{&space;{-1,1}&space;\right&space;\}^c" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v&space;\in&space;\mathbb{R}^c&space;,&space;sgn(v)&space;\in&space;\left&space;\{&space;{-1,1}&space;\right&space;\}^c" title="v \in \mathbb{R}^c , sgn(v) \in \left \{ {-1,1} \right \}^c" /></a>
接下來要最小化quantization error，也就是到hypercube的Euclidean distance

<a href="https://www.codecogs.com/eqnedit.php?latex=\left&space;\|&space;sgn(v)&space;-&space;v&space;\right&space;\|^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left&space;\|&space;sgn(v)&space;-&space;v&space;\right&space;\|^2" title="\left \| sgn(v) - v \right \|^2" /></a>


PCA降維的資料在各維度上的variance不平衡的問題
透過正交轉換不影響PCA的objective function
找出適當的正交矩陣*R*可以降低quantization error

最佳化編碼的問題變成最小化問題
<a href="https://www.codecogs.com/eqnedit.php?latex=Q&space;(B,R)&space;=&space;\left&space;\|&space;B&space;-&space;VR&space;\right&space;\|^2_F" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q&space;(B,R)&space;=&space;\left&space;\|&space;B&space;-&space;VR&space;\right&space;\|^2_F" title="Q (B,R) = \left \| B - VR \right \|^2_F" /></a>

接下來遞迴地執行ITQ降低quantization error，分別使用fix *R* 求 *B*，以及 fix *B* 求 *R*


### Fix R and update B
最大化問題
<a href="https://www.codecogs.com/eqnedit.php?latex=tr(BR^TV^T)&space;=&space;\sum^n_{i=1}\sum^c_{j=1}B_{ij}\tilde{V}_{ij}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?tr(BR^TV^T)&space;=&space;\sum^n_{i=1}\sum^c_{j=1}B_{ij}\tilde{V}_{ij}" title="tr(BR^TV^T) = \sum^n_{i=1}\sum^c_{j=1}B_{ij}\tilde{V}_{ij}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=B_{ij}&space;=&space;1,&space;\textrm{if&space;}&space;\tilde{V}_{ij}&space;\geq&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B_{ij}&space;=&space;1,&space;\textrm{if&space;}&space;\tilde{V}_{ij}&space;\geq&space;0" title="B_{ij} = 1, \textrm{if } \tilde{V}_{ij} \geq 0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=B_{ij}&space;=&space;-1,&space;\textrm{otherwise}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B_{ij}&space;=&space;-1,&space;\textrm{otherwise}" title="B_{ij} = -1, \textrm{otherwise}" /></a>

### Fix B and update R
對<a href="https://www.codecogs.com/eqnedit.php?latex=B^TV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B^TV" title="B^TV" /></a>做SVD分解
求得<a href="https://www.codecogs.com/eqnedit.php?latex=S\Omega&space;\tilde{S}^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S\Omega&space;\tilde{S}^T" title="S\Omega \tilde{S}^T" /></a>以後
更新<a href="https://www.codecogs.com/eqnedit.php?latex=R&space;=&space;\tilde{S}S^T" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R&space;=&space;\tilde{S}S^T" title="R = \tilde{S}S^T" /></a>

