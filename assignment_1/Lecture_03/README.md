
## Learning From Noisy Large-Scale Datasets With Minimal Supervision 


### 論文簡述

CNN在電腦視覺上取得廣大的成果，現下的瓶頸在於訓練資料的取得。
缺乏大量且正確的semantic annotations訓練資料。
於是這篇論文探討，如何用少量的昂貴正確資料，解決上述窘境。

### 作法

既然大部分的資料是屬於noisy label，那麼訓練一個網路負責處理noisy label，藉其加強最終分類的效果。

![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img3.png "Figure 2. High-level overview of our approach. Noisy input la- bels are cleaned and then used as targets for the final classifier. The label cleaning network and the multi-label classifier are jointly trained and share visual features from a deep convnet. The clean- ing network is supervised by the small set of clean annotations (not shown) while the final classifier utilizes both the clean data and the much larger noisy data.")

通過label cleaning network後的cleaned label，可以幫助multi-label classifier。


