## End-to-End Learning for Point Cloud Based 3D Object Detection

### 目的

利用3D的資料，配合deep learning做3D的物體偵測。</br>
3D物體偵測是許多應用領域核心問題，如自駕車、VR等等。</br>


### 資料LiDAR

[LiDAR](https://en.wikipedia.org/wiki/Lidar)是一種3D data的表示方式，屬於sparsed表示法，所以並不能直接使用3D convolution處理。</br>
而儲存3D data的表示法有很多種，而如何使這種sparsed data配合Region Purposal Network結合，使之處理3D object detection，仍在出現許多不同做法的階段。</br>
這篇論文想利用Raw Point Cloud資料，經過網路做3D Bounding Box Prediction。</br>
![Alt text][1]</br>

### 3 stage model

![Alt text][2]</br>
先看一下RPN與CNN都不是新東西了，那麼第一層的Feature Learning Network到底是什麼東西？</br>
這裡將sparsed point cloud 轉成dense表示法，好讓後面的CNN可以處理。</br>
先將3D空間劃分為固定大小的立方體，voxel。</br>
利用random sample降低資料處理的複雜度，使用FCN投射到高維空間就有point-wise feature。</br>
然後利用VFE保留局部特徵，Aggregated Feature與高維空間結合。</br>
![Alt text][3]</br>

處理到這裡就可以丟給3D CNN做處理了，然後配合RPN做到3D Bounding Box Prediction

### result

![Alt text][4]</br>
![Alt text][5]</br>

[1]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_10/figure1.png
[2]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_10/model1.png
[3]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_10/VFE.png
[4]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_10/result1.png
[5]: https://github.com/k123321141/paper_notes/blob/master/assignment_1/Lecture_10/result2.png



