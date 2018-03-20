
##  Learning Deep Object Detectors from 3D Models


### 論文簡述

CNN在電腦視覺上取得廣大的成果，現下的瓶頸在於訓練資料的取得。</br>
鑑於現在3D模型的資源逐年產出，如何利用大量的3D廉價資源去取代昂貴的真實2D照片。</br>
許多應用需要人為標出bounding box，但是這類型的資料相對的昂貴。</br>
而3D模型缺乏真實性，缺失了許多low-level資訊 : realistic object texture, pose, or background.</br>

這篇論文討論哪些細節是DCNN需要的，根據不同的任務，察覺到有部分的細節是不重要的。</br>
意指部分細節的影響力對DCNN的能力相當小，例如HOG-based classifier對於顏色是灰階或是彩色的影響相當小，被認為是重要的是物件的「輪廓」。</br>
此時，對於HOG-based classifier，顏色變成為了文中提到的「cue invariance」</br>

那麼，找出哪些low-level資訊屬於「invariance」，就可以利用3D模型來增加資料不足的窘境。</br>

### 作法-如何利用3D模型訓練一個object detecotr

#### 模疑資料

利用3D模型模擬需要注意很多low-level資訊，文中模擬了較少的性質。</br>
object texture, color, 3D pose and 3D shape, as well as background scene texture and color.</br>
如果應用中存在某些資訊屬於「invariance」，例如色彩，那麼模擬時只需要使用灰階就行了。</br>
1.  選出5-25種飛機的模型。</br>
2.  選出3-4種視角。</br>
3.  加入表面材質及背景。</br>
4.  加入一些雜訊。(random rotation)</br>
5.  加入真實圖片。(optional)</br>

#### 分析invariance

invariance的意思在於，如果該cue屬於invariance，對於缺失的low-level資訊，DCNN中的High-level層中的neuron被激發的分布仍然相同。</br>
也就是說DCNN並沒有將該cue視為特徵。</br>
繞一大圈講完，論文中的做法就是，模擬時分別使用包含該cue與否的兩個資料集，最後用兩個網路的效能去判定該cue是否重要。</br>
並且認為在不同的任務，存在不同的cue invariance，像是識別花豹的任務，花紋就變得很重要。</br>

### 實驗結果

#### 找出適合的模擬資料量

文中使用mean Average Precision (mAP)來衡量一個網路的效能。</br>
這是不同的模擬資料量對於mAP的影響。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img4.png)</br>

#### 找出invariance

要找出重要的low-level資訊，就需要不同的模擬資料，同樣使用mAP衡量，下圖表示不同設定的效能。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img5.png)</br>






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

![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img2_.png "Figure3. Overviewofourapproachtotrainanimageclassifierfromaverylargesetoftrainingsampleswithnoisylabels(orange)anda small set of samples which additionally have human verification (green). The model contains a label cleaning network that learns to map noisy labels to clean labels, conditioned on visual features from an Inception V3 ConvNet. The label cleaning network is supervised by the human verified labels and follows a residual architecture so that it only needs to learn the difference between the noisy and clean labels. The image classifier shares the same visual features and learns to directly predict clean labels supervised by either (a) the output of the label cleaning network or (b) the human rated labels, if available.")

### cleaning network

1.  首先將noisy label跟feature maps利用FCN(Fully-Connected Network)投影到低維度，將兩向量接起來再過一層FCN輸出multi-label。</br>
2.  加入residual network的概念，加入一個nosiy label space的residual block。</br>用意是讓cleaning network不用學習整個label space裡的關係，讓cleaning network專注在noisy label與cleaned label的差異。</br>
3.  Loss function的定義，cleaning network線性輸出會被clip([0, 1])，文中採用absolute distance;嘗試更平滑的輸出可以採用mse。

### classifier network

訓練最終classifier的Loss function採用multi-label cross-entropy。
target label是cleaned label如果輸入存在cleaned label；否則為cleaning network的輸出。

### experience details

1.  為了平衡loss weight, loss = 0.1\*cleaning loss + classify loss。</br>
2.  sample的比率，9:1 for noisy and cleaned label.</br>

### 與其他baseline的比較

![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img3_.png "")

### 補充

可以嘗試透過這種做法來實作gan，含有大量hash tag的資料很容易搜集，與這篇work的情境很類似。</br>

