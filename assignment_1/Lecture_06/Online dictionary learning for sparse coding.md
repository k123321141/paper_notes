## Online dictionary learning for sparse coding

### 要解決的問題

sparse coding在許多領域有很好的效果，諸如訊號重建、訊號處理等等。</br>
這篇論文提出的方法為stochastic，online learning，可以處理large scale以及不輸於batch learning的方式。</br>
適合用於現行large scale的圖片線上應用，像是大量無標註圖片資料(flickr, facebook)，就需要online learning。</br>


### why sparse ? sparse vs dense

首先根據http://www.scholarpedia.org/article/Sparse_coding</br>
哺乳類動物的大腦由許多神經組成，定義一下density，假定大腦訊號由N組binary神經組成(which can be either active or inactive)</br>
平均active neuron的比例就是density，觀察發現density大於1/2的訊號幾乎都可以無損轉換成density小於1/2的訊號，如果沒有損失訊息量，代表有一組更有效的基底(set of binary neurons)，可以表示原本的訊號。</br>
另一個例子是，靈長類動物的低級視覺區有5000萬個神經元，而視網膜和外側膝狀體的神經細胞只有約100萬個，這表示原本的訊號由100萬的基底組成。</br>

>接下來是我自己臆測的部分
在深度學習中，auto en-decoder裡面的bottle neck相當於輸出有效的dense code，與sparse coding很相似，都是用一組基底去近似原本的訊號，希望能夠無損轉換，提供另一組更有效率的表示法。</br>
但是在神經系統當中，每個神經元的輸出是binary的，所以輸出訊號必須為{0,1}^N，但是深度學習中的dense code精神像是近似於找出線性相依的部分並剔除，一方面與原本訊號中的有效基底有關(rank)，所以模型的能力幾乎被資料所主宰，也就是overfitting的隱憂。</br>
而spase coding在於模仿神經系統中，激發訊號區佔總神經元的低比例，透過限制dense code的能力，使其近似於神經訊號行為，雖然不是最有效的基底表示，但是可以做許多用途，像是可以期待generalize的能力，以及比較容易理解的相似度運算(vector dot)。</br>

### objective function

首先希望encode過後的a是spase的，又要與原本的訊號差最小。</br>
訊號差使用norm2的平方，而sparse部分則用lagrange multiplier跟norm1處理，得出下列式子。</br>
![Alt text][1]</br>
除了a的部分，也希望D的每一項不能夠太powerful，不然D的基底值會太大。</br>
限制了D的條件後，將上式寫成batch loss的形式。</br>
![Alt text][2]</br>
這個式子不是convex，無法透過gradient計算。</br>
如果分別給定D或是a，則變成convex式子，所以透過iterative分別求出D跟a。</br>
![Alt text][3]![Alt text][4]</br>








[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_06/equ2.png
[2]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_06/equ3.png
[3]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_06/algo1.png
[4]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_06/algo2.png



