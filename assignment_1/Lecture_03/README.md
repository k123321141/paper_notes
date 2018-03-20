
## Learning From Noisy Large-Scale Datasets With Minimal Supervision 


### 論文簡述

CNN在電腦視覺上取得廣大的成果，現下的瓶頸在於訓練資料的取得。</br>
缺乏大量且正確的semantic annotations訓練資料。</br>
於是這篇論文探討，如何用少量的昂貴正確資料，解決上述窘境。

### 作法

既然大部分的資料是屬於noisy label，那麼訓練一個網路負責處理noisy label，藉其加強最終分類的效果。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img1.png "Figure 2. High-level overview of our approach. Noisy input la- bels are cleaned and then used as targets for the final classifier. The label cleaning network and the multi-label classifier are jointly trained and share visual features from a deep convnet. The clean- ing network is supervised by the small set of clean annotations (not shown) while the final classifier utilizes both the clean data and the much larger noisy data.")</br>
通過label cleaning network後的cleaned label，可以幫助multi-label classifier。

## 以往作法

常見的做法是，利用大量包含noisy label進行pre-train，後續使用clean label data來fine-tune。

此篇論文認為，clean label可以提供更多信息，可以做到將noisy label對應到clean label。</br>
cleaning network不僅學習了noisy的樣式，也學習到label空間中的隱藏信息。

* 臆測補充：如果clean label只用來作fine-tune太浪費了，直覺上noisy label跟clean label有某種程度上的關聯，像是子集關係或是相似的描述。
不如學一個網路特別作為「降噪」的功能。</br>
就訓練資料上的性質來說，並沒有得到一批真正乾淨的label，另外訓練的這個網路比較像是下面描述的直覺。</br>
我希望這個網路可以告訴我這張圖片是小籠包，而不是「餃子皮」「食物」「中式料理」或甚至錯誤的label等等。</br>
直覺上，透過noisy標籤的描述有點像猜謎遊戲，那麼強迫網路去學習如何猜謎，可以讓網路更著重在我們認為重要的部分，</br>也就是模擬人先得到了概念性的描述，最後再輸出「小籠包」。</br>
概念上跟CNN的shared weights很像，透過shared weights，讓網路學習空間關係。</br>
這裡透過cleaning network，讓網路學習label空間中的關係。

文中基於兩項假設，設計這樣的模型結構。</br>
1.  multi-label之間的關係並不是相互獨立的 -> 可以從學習noisy label中學習對應關係。</br>
2.  semantic label需要考慮到圖片本身隱含的資訊 -> 透過CNN擷取的feature map配合cleaning network可以產出更佳的sematic label。</br>

## key details

![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img2.png "Figure3. Overviewofourapproachtotrainanimageclassifierfromaverylargesetoftrainingsampleswithnoisylabels(orange)anda small set of samples which additionally have human verification (green). The model contains a label cleaning network that learns to map noisy labels to clean labels, conditioned on visual features from an Inception V3 ConvNet. The label cleaning network is supervised by the human verified labels and follows a residual architecture so that it only needs to learn the difference between the noisy and clean labels. The image classifier shares the same visual features and learns to directly predict clean labels supervised by either (a) the output of the label cleaning network or (b) the human rated labels, if available.")

### cleaning network

1.  </br>首先將noisy label跟feature maps利用FCN(Fully-Connected Network)投影到低維度，將兩向量接起來再過一層FCN輸出multi-label。
2.  </br>加入residual network的概念，加入一個nosiy label space的residual block。</br>用意是讓cleaning network不用學習整個label space裡的關係，讓cleaning network專注在noisy label與cleaned label的差異。


可以嘗試透過這種做法來實作gan
