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

首先處理PCA降維的資料在各維度上的variance不平衡的問題
透過適當的正交轉換[1]

再來遞迴得使用ITQ降低quantization error


[1]: H. Je ́gou, M. Douze, C. Schmid, and P. Perez. Aggregating local descriptors into a compact image representation. CVPR, 2010.

