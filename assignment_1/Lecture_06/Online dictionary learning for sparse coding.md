## Online dictionary learning for sparse coding

### 要解決的問題

### sparse vs dense

首先根據http://www.scholarpedia.org/article/Sparse_coding</br>
哺乳類動物的大腦由許多神經組成，定義一下density，假定大腦訊號由N組binary神經組成(which can be either active or inactive)</br>
平均active neuron的比例就是density，觀察發現density大於1/2的訊號幾乎都可以無損轉換成density小於1/2的訊號，如果沒有損失訊息量，代表有一組更有效的基底(set of binary neurons)，可以表示原本的訊號。</br>
另一個例子是，靈長類動物的低級視覺區有5000萬個神經元，而視網膜和外側膝狀體的神經細胞只有約100萬個，這表示原本的訊號由100萬的基底組成。</br>

>接下來是我自己臆測的部分
在深度學習中，auto en-decoder裡面的bottle neck相當於輸出有效的dense code，與sparse coding很相似，都是用一組基底去近似原本的訊號，希望能夠無損轉換，提供另一組更有效率的表示法。</br>
但是在神經系統當中，每個神經元的輸出是binary的，所以輸出訊號必須為{0,1}^N，但是深度學習中的dense code精神像是近似於找出線性相依的部分並剔除，一方面與原本訊號中的有效基底有關(rank)，所以模型的能力幾乎被資料所主宰，也就是overfitting的隱憂。</br>
而spase coding在於模仿神經系統中，激發訊號區佔總神經元的低比例，透過限制dense code的能力，使其近似於神經訊號行為，雖然不是最有效的基底表示，但是可以做許多用途，像是可以期待generalize的能力，以及比較容易理解的相似度運算(vector dot)。</br>


