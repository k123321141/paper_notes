## ArcFace Additive Angular Margin Loss for Deep Face Recognition

### 前述

在圖像已經被CNN所主宰的情況下，人臉相關的應用也都充斥著許多CNN的影子。</br>
而這篇討論的主題也在人臉應用，更深入的探討有關lost function所帶來的影響。</br>
從最naive的softmax，到這篇提出的ArcFace，討論不同loss帶來的影響。</br>


### Euclidean margin based loss

softmax在分類器是很常見的做法，經過網路的feature extraction，softmax將不同類別的hidden vector分開。</br>
但是softmax並沒有進一步的使同類別的樣本有較小的差距，之後相繼提出了許多擴大margin的改進。</br>

Center Loss: 為每個類別提出了一個中心，使用softmax增加不同類別的差距的同時，最小化同類別的差距。</br>
<a href="https://www.codecogs.com/eqnedit.php?latex=L_c&space;=&space;\frac&space;12&space;\sum^m_{i=1}||x_i&space;-&space;C_{y_i}&space;||^2_2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L_c&space;=&space;\frac&space;12&space;\sum^m_{i=1}||x_i&space;-&space;C_{y_i}&space;||^2_2" title="L_c = \frac 12 \sum^m_{i=1}||x_i - C_{y_i} ||^2_2" /></a></br>
<a href="https://www.codecogs.com/eqnedit.php?latex=L=L_s&plus;\lambda&space;L_c" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L=L_s&plus;\lambda&space;L_c" title="L=L_s+\lambda L_c" /></a></br>
這是mnist搭配center loss的結果圖，資料參考原論文：</br>
![Alt text][1]</br>



除此之外，像Center loss, Range loss, and Marginal loss加強了對同類別的差異容許(intra-variance or inter-distance)</br>

而另一種做法使用pair training strategy,The contrastive loss and the Triplet loss. </br>
The contrastive loss透過positive pair與negative pair使得每次更新gradient時，拉近了positive pair，也推遠了negative pair。</br>
Triplet loss則選定了一個anchor，透過sampling，拉近positive sample而推遠negative sample。</br>
但是這種作法在sampling以及挑選pair時，仰賴經驗，是比較困難的部分。</br>

### Angular and cosine margin based loss

出現了large margin Softmax (L- Softmax)，除了Euclidean distance上的差異，引入了angular margin。</br>
SphereFace透過normalize weights and zero biases，相當於映射到同一個高維球面，然後加入angular margin。</br>
![Alt text][2]</br>

透過改進SphereFace，增加了一個使cosine(mθ) monotonic的function，將原本SphereFace的mθ轉換到cosine空間中</br>
由於角度距離，比cosine space距離對角度影像更加直接，最終修改成Additive Angular Margin。</br>

SphereFace Loss</br>
![Alt text][3]</br>

Additive Cosine Margin</br>
![Alt text][4]</br>

Additive Angular Margin</br>
![Alt text][5]</br>

下圖是各個改進的決策邊界。</br>
![Alt text][6]</br>


### 心得

當然最後就要跟其他baseline比較一番，但是從資料到模型的架構，這一番細節比較建議直接看論文的詳述。</br>
處理像人臉這種manifold的問題，比起feature extraction，遇到在應用上差距，以及testing data分佈差距(資料庫內樣本與資料庫外樣本)，考慮intra-invarience常常是被忽略的。</br>
透過loss function的改變，可以看出不同loss所代表的意義，以及試圖想解決的問題，是我在處理問題上不會先想到的方向。</br>
這是很好的一種理解方向。</br>









[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/center_loss.png
[2]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/SphereFace.png
[3]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/SphereFace_loss.png
[4]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/cosine_margin.png
[5]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/ArcFace_loss.png
[6]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_12/decision_boundary.png



