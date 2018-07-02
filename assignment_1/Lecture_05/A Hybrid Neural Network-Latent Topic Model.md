## A Hybrid Neural Network-Latent Topic Model

### [topic model](https://github.com/k123321141/paper_notes/blob/master/class/topic_model.md)

### The hybrid model

這篇主要發想是利用結合了hierarchical topic model (HTM) 與 neural network (NN)。</br>
想要利用NN能夠好好處理feature extraction的能力，配合topic model做jointly的學習。</br>

## NN

主要功能是用做feature extration，根據不同應用可以有不同的架構</br>。
根據此篇的範例，使用簡單的2 layer NN，搭配sigmoid activation function做簡單的非線性轉換。</br>
而不同應用可以用不同的架構。</br>

注：這篇文有特別提到如何用Restricted Boltzmann machine (RBMs)做NN的pretrain，如果是不同應用，應該有不同適合的做法。</br>

### HTM

topic model假定透過NN轉換後的x，會符合由word組成的高斯分佈。</br>
而分別有topic分布及word分佈，graphical model如下圖：</br>
![Alt text][1]</br>
定好模型後，這篇文利用gradient decent訓練HTM，原始的輸入v會透過NN轉換成x，也就是f(v)</br>
Loss function如下：</br>
![Alt text][2]</br>

分別利用pretrain 來init參數{w0,π0,η0,φ0}</br>
利用下式更新：</br>
![Alt text][3]</br>


### Pre-training 

論文利用pre-training來做init，所以分別使用contrastive divergence (CD) algorithm配合RBMs做NN的pre training。</br>
而HTM部分則使用pre-train 結束的NN提供f(v)，利用Gibbs採樣訓練HTM。</br>

### joint optimization by gradient descent

當pretrain process都結束後，可以進入jointly training的步驟。</br>
不過HTM跟NN的training process依舊不同，透過擴展HTM的loss function:</br>
![Alt text][4]</br>
HTM的training algorithm如下：</br>
![Alt text][5]</br>

NN的部分需要透過定義一下幾種function，然後搭配微分連鎖率依然可以做gradient propagation。</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=A_{ji}&space;=&space;[p(f_w(v_j))\midy=i,\pi,\eta&space;,\phi&space;]_{ji}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A_{ji}&space;=&space;[p(f_w(v_j))\midy=i,\pi,\eta&space;,\phi&space;]_{ji}" title="A_{ji} = [p(f_w(v_j))\midy=i,\pi,\eta ,\phi ]_{ji}" /></a>

![Alt text][6]</br>
![Alt text][7]</br>



### 評論

現有許多model在各種領域都已經有很好的成果，而搭配NN做feature extraction end-to-end training是一種推進效能的辦法。</br>
而每種應用都有不同的解法，bag-of-words並不能符合所有應用的特性。</br>
搭配NN的做法是一種突破，以往嘗試許多不同feature extraction method然後搭配blending的效果也許有不錯的成果。</br>
但是end-to-end訓練是一種趨勢。</br>






[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/model.png
[2]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/HTM_loss.png
[3]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/HTM_update.png
[4]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/HTM_loss2.png
[5]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/HTM_algo.png
[6]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/NN_algo1.png
[7]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_05/NN_algo2.png



