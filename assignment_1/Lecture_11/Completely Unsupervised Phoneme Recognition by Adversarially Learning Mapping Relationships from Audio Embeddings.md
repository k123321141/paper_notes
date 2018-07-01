## Completely Unsupervised Phoneme Recognition by Adversarially Learning Mapping Relationships from Audio Embeddings 

### 目的

讓一段聲音訊號轉成phoneme sequences.

### 前言

機器學習需要大量的資料，而labeled data一直是各種機器學習會遇到的問題，而phoneme-labeled audio data除了稀少之外，label的難度也很高。</br>
label data也可能遇到mis-annotaion的問題。</br>
如果能利用unlabeled data，可以用的資料就變得很多，這篇論文提出使用unsupervied learning處理phoneme recognition問題。</br>

### 3 stage model

![Alt text][1]</br>


這篇我理解的思路如下</br>

### seq2seq

利用seq2seq model配合supervised learning，可以嘗試做audio sequence -> phoneme sequence的轉換，但是labeled-data的取得困難，造就unsupervising learning的需求。</br>

### GAN

利用seq2seq配上reconstruction error可以對audio做一種embedding，訓練GAN則希望得到embedding vector -> phoneme的轉換。</br>
GAN的generator負責吃embedding vector，輸出phoneme label，而discriminator則負責辨別phoneme sequence是否假造。</br>
fake seq的部分由generator產生，true seq則由text依照音素表(像是kk音標)轉成phoneme seq，而text與video不需要是相關的。</br>

### K-means clustering

我猜想是seq2seq的reconstruction error會保留許多intra-invariance，而最終目標，label phoneme seq，並不在意是否能夠reconstruct original video，所以為了減少這種intra-invairance加入了clustering，也讓GAN fitting變得容易。</br>
我的想法是經過clustering，也許每個人的口音，都會消失，而留下基本的聲音輪廓，像是google小姐的機器聲，雖然無法reconstruct，但是最終只是要label phoneme seq，所以GAN的訓練會變得容易些。</br>


### result


![Alt text][2]</br>
這張圖是我感興趣的地方，是對比於supervised learning的效能，supervised learning當然能期待比較好的效能，但是那個0.001常常就是資料的門檻。</br>

### 心得

其實GAN的訓練部分是我覺得比較tricky的地方，難道不會train完，generator只固定產生某一組phoneme seq?</br>
而這個問題也讓我想到另一個很有名的unsupervised learning GAN，CycleGAN。</br>
不曉得cycleGAN在這領域是否能夠做得好？有聽過CNN主宰了電腦視覺，而RNN則強在自然語言處理，在這種聲音訊號上，也許是還沒出現適合deep learning的模型，也許做不好。</br>

這裡還有提到Gumbel softmax的選用，與[ArcFace](https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/ArcFace%20Additive%20Angular%20Margin%20Loss%20for%20Deep%20Face%20Recognition.md)有相似之處，討論使用不同loss的場合。</br>


[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_11/model.png
[2]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_11/result.png



