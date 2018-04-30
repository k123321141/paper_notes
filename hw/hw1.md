

### sparse coding for face image retrival

使用上一篇must read paper提出的方法，J. Mairal, F. Bach, J. Ponce, and G. Sapiro, “Online dictionary learning
for sparse coding,” ICML, 2009.</br>
利用L1 regularizer學出sparse coding.</br>

須注意這邊並沒有涉入human attributes.</br>
這邊僅利用了reconstruct error</br>

### Attribute-enhanced sparse coding

為了將不同attribute的image經過sparse coding後，codeword不同。</br>
比較k-means與sparse coding的不同</br>
![Alt text][1]</br>
k-means 只讓一個image分配到一個類別(k個類別)，而sparse coding則讓一個image視為數個可能線性相依的dictionary colume的組成。</br>
兩個相似但是attibute不同的image在單純使用sparse coding的情況下，會產出類似的codeword，也就是使用相似的colume。</br>
ASC強迫不同attribute的image必須使用不同的column去組成原本的image來達成attibute的區別。</br>

而文中的比較圖<也揭示了可能的缺點，當detect attribute時發生了錯誤，則hard assignment會造成無法挽回的失敗。</br>
![Alt text][2]</br>

接下來討論如何設定選用的column</br>
假設現下只有一個attibute，利用這項attribute的正負號來表示一個image該選用的column。(二元區別)</br>
如果為正，則選用上半部的column</br>
如果為負，則選用下半部的column</br>
透過下列loss function，設立一個mask vector可以達成這樣的條件</br>
![Alt text][3]</br>
而多個attribute的形式則一樣，每一個attribute都會有兩組column。</br>
假設dictionary共有k個column，而有a組attributes，則共會分成k/2a組column，而每一組mask則寫成[1,1,..,∞,∞,1,1,...,∞,∞]^T的形式。</br>



[1]: https://github.com/k123321141/paper_notes/blob/master/class/img1.png
[2]: https://github.com/k123321141/paper_notes/blob/master/hw/fig4.png
[3]: https://github.com/k123321141/paper_notes/blob/master/hw/equ3.png

