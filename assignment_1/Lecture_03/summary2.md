
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
2000是個較好的選擇。</br>

#### 找出invariance

要找出重要的low-level資訊，就需要不同的模擬資料，同樣使用mAP衡量，下圖表示不同設定的效能。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img5.png "Table 1. Detection results on the PASCAL VOC2007 test dataset. Each row is trained on different background and texture configuration of virtual data shown in the top table. In the middle table, the DCNN is trained on ImageNet ILSVRC 1K classification data and finetuned on the PASCAL training data; in the bottom table, the network is not fine-tuned on PASCAL.")</br>
上圖指出，在PASC-FT表格(trained on ImageNet, fine-tune on PASCAL)，RG-RR與W-RR表現甚至好一些，那麼可能表示background color屬於cue invarince</br>
相對而言，花紋就是比較重要的資訊。</br>

另外要觀察的是網路對於哪些輸入會有最高的「反應」，找出網路認為最符合某類別的輸入，也是找出invariance的指標。</br>
![alt text](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_03/img6.png "Figure 4. Top 10 regions with strongest activations for 2 pool5 units using the method of [5]. Overlay of the unit’s receptive field is drawn in white and normalized activation value is shown in the upper-left corner. For each unit we show results on (top to bottom): real PASCAL images, RR-RR, W-RR, W-UG. See text for further explanation.")</br>
左邊電視機的範例，從真實物件-真實背景到模擬物件-無背景，網路activate的對象大部分都是對的。</br>
右邊綿羊的範例，W-UG，白背景-全灰階物件時，網路明顯無法判斷出正確的綿羊圖片，花紋是相對重要的資訊。</br>


## 結論

DCNN經過fine-tune以後，存在更多invariance，使得模擬資料包不包含這些cue，對於網路的效能影響不大。</br>
基於這項假設，根據不同的應用，利用模擬的資料，可以解決訓練資料不足。</br>
像是新的類別需要被辨識時，使用pre-train network，由於是新類別，基於fine-tune會出現更多cue invariance。</br>
這時候就相當適合使用模擬資料做訓練。</br>

