## NEURAL ARCHITECTURE SEARCH WITH REINFORCEMENT LEARNING

### 前述

Deep Learning已經被廣泛地使用在各個領域中，但是如何設計網路的架構仍舊需要靠人類的經驗。</br>
而網路的架構深深地影響效能，這篇論文使用RNN去構造一個神經網路，並且使用reinforcement learning最大化對validation set的accuracy。</br>
在CIFAR-10的testing set上，達到了比人類設計的網路還強的效能。</br>
在Penn Treebank dataset還產生了一種RNN cell表現得比常見的LSTM cell更好。</br>

![Alt text][1]</br>
controller 持續產生 child network，然後利用RL再產生出下一代child network。</br>

### RNN controller on hyperparameters

![Alt text][2]</br>
描述controller如何建造出一個只含convolution layer的NN。</br>
controller是一個RNN network，調整hyperparameters of convolution layer。</br>
hyperparameters: nunmber of filter, filter size, stride size, etc</br>
controller可以決定每個conv layer的參數，使用softmax classifier產生每個timestep的hyperparameter，seq2seq學習。</br>
使用RNN架構可以處理variable-lenth input。</br>

每次產生出hyperparameters，就訓練直到收斂後，記錄固定validation set的accuracy。</br>
利用policy gradient 訓練這個RNN controller。</br>
pg是RL很基本的方法，這篇還有提到一些實驗的設定也是常見的做法，像設定baseline。

### skip connections

利用attention mechanism讓controller決定讓哪些layer可以使用這種進階結構，配合sigmoid function讓每一層都決定是否需要連結。</br>
如此一來除了layer的參數，網路的架構也可以被產生。</br>

### RNN cell

除了網路的部分，作者額外將RNN cell的一些操作加入action space。標準的RNN cell如下：</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=h_t&space;=&space;\tanh\left&space;(&space;W_1\ast&space;x_t&space;&plus;&space;W_2\ast&space;h_{t-1}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h_t&space;=&space;\tanh\left&space;(&space;W_1\ast&space;x_t&space;&plus;&space;W_2\ast&space;h_{t-1}&space;\right&space;)" title="h_t = \tanh\left ( W_1\ast x_t + W_2\ast h_{t-1} \right )" /></a></br>
W1 W2各是要被學習的參數，作者讓controller可以決定</br>
1. activation function，對應上面的tanh。</br>
2. combination method，對應上面的elementwise addition。</br>

下圖是決定RNN cell的流程：</br>
![Alt text][3]</br>


### 心得

實驗結果就不秀了，我感興趣的是產生出child model的架構</br>
![Alt text][4]</br>
這個神奇的CNN居然還嘗試長方形的filter。</br>
而RNN cell就更畸形了，由於加入了很多activation function進去action space，可以期待controller產生新奇的架構。</br>
![Alt text][5]</br>
即便加入了sin function，機器也沒有選擇使用sin，這種奇怪的嘗試讓機器做真是符合機器學習的精神。</br>
還記得當初學LSTM的時候，每個操作都是有一種數學含義，然後用淺顯易懂的文字描述成「記憶」單元。</br>
像c的變化會比h小，則能夠類比成保留long term memory，而h則是short term momery。</br>
就像AlphaGO找出了許多沒看過的盤面，也許會有人想做controller的分析，找出合理的描述方式，這樣也許能從機器中學習如何設計機器(供殺小)</br>

不過就自己訓練RL的時候，首先是RL的訓練過程實在不是很stable，在面對probabilistic action的時候更難訓練，我想每次train網路使用不同的亂數也能算是一種probabilistic action。</br>
還有RL很耗時，加上policy gradient算是on-policy的方法，對於訓練的要求實在很高，沒有那麼多機器可以玩家分散式的訓練那麼多network。</br>
玩不起啊，這種實驗真適合google brain。</br>










[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_13/controller_model.png
[2]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_13/controller.png
[3]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_13/rnn.png
[4]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_13/result1.png
[5]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_13/result2.png



