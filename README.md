# gcn_run
runnable version of gcn

the output of the first version：

D:\Unity\python\python.exe D:/Unity/pycharm/gcn_run/train.py
support-- [(array([[   0,    0],
       [ 633,    0],
       [1862,    0],
       ..., 
       [1473, 2707],
       [2706, 2707],
       [2707, 2707]], dtype=int32), array([ 0.25     ,  0.25     ,  0.2236068, ...,  0.2      ,  0.2      ,
        0.2      ]), (2708, 2708))] 
 num_supports-- 1 
 model_func-- <class 'models.GCN'>
placeholders--in class GCN in models.py--- {'labels': <tf.Tensor 'Placeholder_5:0' shape=(?, 7) dtype=float32>, 'dropout': <tf.Tensor 'PlaceholderWithDefault:0' shape=() dtype=float32>, 'features': <tensorflow.python.framework.sparse_tensor.SparseTensor object at 0x000001CAFFE4B860>, 'support': [<tensorflow.python.framework.sparse_tensor.SparseTensor object at 0x000001CAFFE4B4A8>], 'labels_mask': <tf.Tensor 'Placeholder_6:0' shape=<unknown> dtype=int32>, 'num_features_nonzero': <tf.Tensor 'Placeholder_7:0' shape=<unknown> dtype=int32>}
GraphConvo in models.py
layers--in def build in models.py--- [<layers.GraphConvolution object at 0x000001CA811E72E8>, <layers.GraphConvolution object at 0x000001CA811E7080>]
x=inputs--in graphConvo in layers.py-- SparseTensor(indices=Tensor("Placeholder_4:0", shape=(?, 2), dtype=int64), values=Tensor("Placeholder_3:0", shape=(?,), dtype=float32), dense_shape=Tensor("Const:0", shape=(2,), dtype=int64))
layers--in def build in models.py--- [<layers.GraphConvolution object at 0x000001CA811E72E8>, <layers.GraphConvolution object at 0x000001CA811E7080>]
x=inputs--in graphConvo in layers.py-- Tensor("graphconvolution_1/Relu:0", shape=(?, 16), dtype=float32)
self.outputs---def accuracy in models.py- Tensor("graphconvolution_2/SparseTensorDenseMatMul/SparseTensorDenseMatMul:0", shape=(?, 7), dtype=float32) 
self.placeholders['labels']-- Tensor("Placeholder_5:0", shape=(?, 7), dtype=float32)
2018-03-10 12:46:38.230432: I C:\tf_jenkins\home\workspace\rel-win\M\windows\PY\35\tensorflow\core\platform\cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
Epoch: 0001 train_loss= 1.95399 train_acc= 0.07143 val_loss= 1.95070 val_acc= 0.20600 time= 0.12831
Epoch: 0002 train_loss= 1.94801 train_acc= 0.29286 val_loss= 1.94716 val_acc= 0.37000 time= 0.09207
Epoch: 0003 train_loss= 1.94218 train_acc= 0.48571 val_loss= 1.94333 val_acc= 0.47000 time= 0.09107
Epoch: 0004 train_loss= 1.93654 train_acc= 0.56429 val_loss= 1.93922 val_acc= 0.50400 time= 0.09329
Epoch: 0005 train_loss= 1.92665 train_acc= 0.66429 val_loss= 1.93517 val_acc= 0.50400 time= 0.09307
Epoch: 0006 train_loss= 1.92017 train_acc= 0.70000 val_loss= 1.93110 val_acc= 0.51400 time= 0.08906
Epoch: 0007 train_loss= 1.91050 train_acc= 0.71429 val_loss= 1.92704 val_acc= 0.52000 time= 0.09644
Epoch: 0008 train_loss= 1.89941 train_acc= 0.71429 val_loss= 1.92310 val_acc= 0.51600 time= 0.09120
Epoch: 0009 train_loss= 1.89015 train_acc= 0.75714 val_loss= 1.91920 val_acc= 0.52000 time= 0.09317
Epoch: 0010 train_loss= 1.88369 train_acc= 0.67143 val_loss= 1.91527 val_acc= 0.52000 time= 0.09556
Epoch: 0011 train_loss= 1.87589 train_acc= 0.72143 val_loss= 1.91122 val_acc= 0.52000 time= 0.09307
Epoch: 0012 train_loss= 1.86910 train_acc= 0.68571 val_loss= 1.90708 val_acc= 0.53200 time= 0.09320
Epoch: 0013 train_loss= 1.85591 train_acc= 0.70714 val_loss= 1.90297 val_acc= 0.53400 time= 0.09238
Epoch: 0014 train_loss= 1.84738 train_acc= 0.71429 val_loss= 1.89877 val_acc= 0.55200 time= 0.09207
Epoch: 0015 train_loss= 1.83186 train_acc= 0.72857 val_loss= 1.89443 val_acc= 0.56000 time= 0.09206
Epoch: 0016 train_loss= 1.81894 train_acc= 0.77857 val_loss= 1.89003 val_acc= 0.57200 time= 0.09307
Epoch: 0017 train_loss= 1.81409 train_acc= 0.73571 val_loss= 1.88559 val_acc= 0.58600 time= 0.09234
Epoch: 0018 train_loss= 1.79738 train_acc= 0.76429 val_loss= 1.88102 val_acc= 0.59200 time= 0.09533
Epoch: 0019 train_loss= 1.79215 train_acc= 0.75000 val_loss= 1.87632 val_acc= 0.58800 time= 0.10307
Epoch: 0020 train_loss= 1.77766 train_acc= 0.75000 val_loss= 1.87153 val_acc= 0.59400 time= 0.09632
Epoch: 0021 train_loss= 1.76760 train_acc= 0.77857 val_loss= 1.86662 val_acc= 0.59200 time= 0.09707
Epoch: 0022 train_loss= 1.74438 train_acc= 0.81429 val_loss= 1.86159 val_acc= 0.58800 time= 0.09713
Epoch: 0023 train_loss= 1.74515 train_acc= 0.78571 val_loss= 1.85646 val_acc= 0.59000 time= 0.09106
Epoch: 0024 train_loss= 1.73049 train_acc= 0.80000 val_loss= 1.85116 val_acc= 0.59200 time= 0.08906
Epoch: 0025 train_loss= 1.71461 train_acc= 0.77857 val_loss= 1.84557 val_acc= 0.59600 time= 0.09006
Epoch: 0026 train_loss= 1.68822 train_acc= 0.80714 val_loss= 1.83967 val_acc= 0.60200 time= 0.09036
Epoch: 0027 train_loss= 1.68093 train_acc= 0.78571 val_loss= 1.83355 val_acc= 0.60600 time= 0.09107
Epoch: 0028 train_loss= 1.68646 train_acc= 0.76429 val_loss= 1.82723 val_acc= 0.62200 time= 0.09213
Epoch: 0029 train_loss= 1.66409 train_acc= 0.79286 val_loss= 1.82073 val_acc= 0.62800 time= 0.08955
Epoch: 0030 train_loss= 1.64123 train_acc= 0.77143 val_loss= 1.81413 val_acc= 0.63800 time= 0.08995
Epoch: 0031 train_loss= 1.62944 train_acc= 0.80000 val_loss= 1.80741 val_acc= 0.64400 time= 0.09106
Epoch: 0032 train_loss= 1.62115 train_acc= 0.79286 val_loss= 1.80045 val_acc= 0.65200 time= 0.09325
Epoch: 0033 train_loss= 1.60770 train_acc= 0.82857 val_loss= 1.79344 val_acc= 0.65400 time= 0.09006
Epoch: 0034 train_loss= 1.60463 train_acc= 0.81429 val_loss= 1.78648 val_acc= 0.66000 time= 0.09807
Epoch: 0035 train_loss= 1.56832 train_acc= 0.85714 val_loss= 1.77930 val_acc= 0.66400 time= 0.12209
Epoch: 0036 train_loss= 1.55106 train_acc= 0.87143 val_loss= 1.77186 val_acc= 0.67000 time= 0.11408
Epoch: 0037 train_loss= 1.53871 train_acc= 0.87857 val_loss= 1.76430 val_acc= 0.67400 time= 0.12221
Epoch: 0038 train_loss= 1.51639 train_acc= 0.84286 val_loss= 1.75637 val_acc= 0.68200 time= 0.12009
Epoch: 0039 train_loss= 1.52742 train_acc= 0.87143 val_loss= 1.74819 val_acc= 0.69000 time= 0.11724
Epoch: 0040 train_loss= 1.49984 train_acc= 0.87143 val_loss= 1.74004 val_acc= 0.68800 time= 0.09407
Epoch: 0041 train_loss= 1.49882 train_acc= 0.85000 val_loss= 1.73166 val_acc= 0.69200 time= 0.09207
Epoch: 0042 train_loss= 1.45390 train_acc= 0.85714 val_loss= 1.72328 val_acc= 0.69600 time= 0.09707
Epoch: 0043 train_loss= 1.47726 train_acc= 0.83571 val_loss= 1.71492 val_acc= 0.69600 time= 0.10107
Epoch: 0044 train_loss= 1.43801 train_acc= 0.82857 val_loss= 1.70627 val_acc= 0.70800 time= 0.09107
Epoch: 0045 train_loss= 1.42582 train_acc= 0.84286 val_loss= 1.69771 val_acc= 0.71200 time= 0.09006
Epoch: 0046 train_loss= 1.37447 train_acc= 0.87857 val_loss= 1.68892 val_acc= 0.72000 time= 0.09935
Epoch: 0047 train_loss= 1.37587 train_acc= 0.82857 val_loss= 1.67985 val_acc= 0.72400 time= 0.09607
Epoch: 0048 train_loss= 1.37041 train_acc= 0.91429 val_loss= 1.67064 val_acc= 0.73000 time= 0.09106
Epoch: 0049 train_loss= 1.37453 train_acc= 0.84286 val_loss= 1.66152 val_acc= 0.73400 time= 0.09707
Epoch: 0050 train_loss= 1.32568 train_acc= 0.85714 val_loss= 1.65225 val_acc= 0.73200 time= 0.09918
Epoch: 0051 train_loss= 1.38851 train_acc= 0.85714 val_loss= 1.64305 val_acc= 0.73600 time= 0.09017
Epoch: 0052 train_loss= 1.32950 train_acc= 0.89286 val_loss= 1.63386 val_acc= 0.73600 time= 0.09707
Epoch: 0053 train_loss= 1.32623 train_acc= 0.89286 val_loss= 1.62455 val_acc= 0.73600 time= 0.11030
Epoch: 0054 train_loss= 1.30045 train_acc= 0.87143 val_loss= 1.61519 val_acc= 0.74200 time= 0.09115
Epoch: 0055 train_loss= 1.28332 train_acc= 0.89286 val_loss= 1.60586 val_acc= 0.74200 time= 0.09522
Epoch: 0056 train_loss= 1.23221 train_acc= 0.90714 val_loss= 1.59672 val_acc= 0.74400 time= 0.09931
Epoch: 0057 train_loss= 1.26357 train_acc= 0.90714 val_loss= 1.58782 val_acc= 0.74600 time= 0.09106
Epoch: 0058 train_loss= 1.22354 train_acc= 0.90000 val_loss= 1.57871 val_acc= 0.74800 time= 0.09407
Epoch: 0059 train_loss= 1.23061 train_acc= 0.91429 val_loss= 1.56945 val_acc= 0.75200 time= 0.09907
Epoch: 0060 train_loss= 1.25688 train_acc= 0.90000 val_loss= 1.56006 val_acc= 0.75600 time= 0.09320
Epoch: 0061 train_loss= 1.18911 train_acc= 0.89286 val_loss= 1.55086 val_acc= 0.75600 time= 0.09132
Epoch: 0062 train_loss= 1.20369 train_acc= 0.90000 val_loss= 1.54161 val_acc= 0.75800 time= 0.10307
Epoch: 0063 train_loss= 1.13703 train_acc= 0.89286 val_loss= 1.53249 val_acc= 0.76200 time= 0.09707
Epoch: 0064 train_loss= 1.18960 train_acc= 0.86429 val_loss= 1.52341 val_acc= 0.76200 time= 0.09407
Epoch: 0065 train_loss= 1.17308 train_acc= 0.92857 val_loss= 1.51439 val_acc= 0.76400 time= 0.09013
Epoch: 0066 train_loss= 1.12569 train_acc= 0.92857 val_loss= 1.50526 val_acc= 0.77000 time= 0.09106
Epoch: 0067 train_loss= 1.12061 train_acc= 0.88571 val_loss= 1.49642 val_acc= 0.77400 time= 0.09213
Epoch: 0068 train_loss= 1.11809 train_acc= 0.93571 val_loss= 1.48789 val_acc= 0.77200 time= 0.09307
Epoch: 0069 train_loss= 1.12220 train_acc= 0.91429 val_loss= 1.47969 val_acc= 0.77200 time= 0.09427
Epoch: 0070 train_loss= 1.09568 train_acc= 0.92143 val_loss= 1.47169 val_acc= 0.77000 time= 0.09219
Epoch: 0071 train_loss= 1.09616 train_acc= 0.88571 val_loss= 1.46357 val_acc= 0.77400 time= 0.09111
Epoch: 0072 train_loss= 1.07255 train_acc= 0.93571 val_loss= 1.45562 val_acc= 0.77600 time= 0.09024
Epoch: 0073 train_loss= 1.06721 train_acc= 0.96429 val_loss= 1.44818 val_acc= 0.77400 time= 0.09307
Epoch: 0074 train_loss= 1.10403 train_acc= 0.89286 val_loss= 1.44058 val_acc= 0.77400 time= 0.09527
Epoch: 0075 train_loss= 1.01538 train_acc= 0.92143 val_loss= 1.43314 val_acc= 0.77600 time= 0.09006
Epoch: 0076 train_loss= 1.00960 train_acc= 0.94286 val_loss= 1.42541 val_acc= 0.77600 time= 0.09307
Epoch: 0077 train_loss= 0.95229 train_acc= 0.95000 val_loss= 1.41774 val_acc= 0.77600 time= 0.09106
Epoch: 0078 train_loss= 1.04013 train_acc= 0.91429 val_loss= 1.41061 val_acc= 0.77600 time= 0.09106
Epoch: 0079 train_loss= 1.00806 train_acc= 0.92857 val_loss= 1.40379 val_acc= 0.77600 time= 0.09515
Epoch: 0080 train_loss= 1.00069 train_acc= 0.95000 val_loss= 1.39687 val_acc= 0.77600 time= 0.09529
Epoch: 0081 train_loss= 0.97463 train_acc= 0.91429 val_loss= 1.39013 val_acc= 0.77600 time= 0.09006
Epoch: 0082 train_loss= 0.96301 train_acc= 0.95714 val_loss= 1.38356 val_acc= 0.77600 time= 0.09514
Epoch: 0083 train_loss= 0.95958 train_acc= 0.95000 val_loss= 1.37702 val_acc= 0.77600 time= 0.09116
Epoch: 0084 train_loss= 0.97093 train_acc= 0.93571 val_loss= 1.37043 val_acc= 0.77600 time= 0.09217
Epoch: 0085 train_loss= 0.94742 train_acc= 0.96429 val_loss= 1.36384 val_acc= 0.77600 time= 0.09907
Epoch: 0086 train_loss= 0.94996 train_acc= 0.93571 val_loss= 1.35739 val_acc= 0.77800 time= 0.09207
Epoch: 0087 train_loss= 0.97249 train_acc= 0.92857 val_loss= 1.35100 val_acc= 0.78000 time= 0.09021
Epoch: 0088 train_loss= 0.94913 train_acc= 0.93571 val_loss= 1.34459 val_acc= 0.78000 time= 0.09307
Epoch: 0089 train_loss= 0.97455 train_acc= 0.91429 val_loss= 1.33826 val_acc= 0.78000 time= 0.09207
Epoch: 0090 train_loss= 0.97957 train_acc= 0.91429 val_loss= 1.33204 val_acc= 0.78000 time= 0.09407
Epoch: 0091 train_loss= 0.92480 train_acc= 0.95000 val_loss= 1.32596 val_acc= 0.78000 time= 0.09210
Epoch: 0092 train_loss= 0.95817 train_acc= 0.92143 val_loss= 1.32011 val_acc= 0.78000 time= 0.09137
Epoch: 0093 train_loss= 0.89500 train_acc= 0.95000 val_loss= 1.31456 val_acc= 0.77800 time= 0.10206
Epoch: 0094 train_loss= 0.86474 train_acc= 0.92857 val_loss= 1.30937 val_acc= 0.77800 time= 0.11116
Epoch: 0095 train_loss= 0.90715 train_acc= 0.96429 val_loss= 1.30445 val_acc= 0.78000 time= 0.10650
Epoch: 0096 train_loss= 0.89772 train_acc= 0.93571 val_loss= 1.29963 val_acc= 0.78000 time= 0.11370
Epoch: 0097 train_loss= 0.88455 train_acc= 0.93571 val_loss= 1.29490 val_acc= 0.78000 time= 0.09012
Epoch: 0098 train_loss= 0.93267 train_acc= 0.91429 val_loss= 1.29068 val_acc= 0.78000 time= 0.09006
Epoch: 0099 train_loss= 0.88896 train_acc= 0.94286 val_loss= 1.28639 val_acc= 0.78400 time= 0.09314
Epoch: 0100 train_loss= 0.90960 train_acc= 0.91429 val_loss= 1.28227 val_acc= 0.78400 time= 0.09006
Epoch: 0101 train_loss= 0.86087 train_acc= 0.95714 val_loss= 1.27814 val_acc= 0.78400 time= 0.09024
Epoch: 0102 train_loss= 0.86598 train_acc= 0.93571 val_loss= 1.27432 val_acc= 0.78400 time= 0.09316
Epoch: 0103 train_loss= 0.83829 train_acc= 0.93571 val_loss= 1.27057 val_acc= 0.78400 time= 0.09011
Epoch: 0104 train_loss= 0.84580 train_acc= 0.95000 val_loss= 1.26665 val_acc= 0.78400 time= 0.08823
Epoch: 0105 train_loss= 0.82976 train_acc= 0.95714 val_loss= 1.26240 val_acc= 0.78000 time= 0.09206
Epoch: 0106 train_loss= 0.86847 train_acc= 0.92857 val_loss= 1.25843 val_acc= 0.78000 time= 0.09027
Epoch: 0107 train_loss= 0.86326 train_acc= 0.93571 val_loss= 1.25464 val_acc= 0.77800 time= 0.09206
Epoch: 0108 train_loss= 0.83011 train_acc= 0.94286 val_loss= 1.25113 val_acc= 0.77800 time= 0.09006
Epoch: 0109 train_loss= 0.84336 train_acc= 0.95000 val_loss= 1.24781 val_acc= 0.77800 time= 0.08826
Epoch: 0110 train_loss= 0.78123 train_acc= 0.95000 val_loss= 1.24383 val_acc= 0.77800 time= 0.09115
Epoch: 0111 train_loss= 0.83708 train_acc= 0.95000 val_loss= 1.24008 val_acc= 0.77800 time= 0.09307
Epoch: 0112 train_loss= 0.85494 train_acc= 0.92857 val_loss= 1.23682 val_acc= 0.77800 time= 0.09006
Epoch: 0113 train_loss= 0.79999 train_acc= 0.92857 val_loss= 1.23371 val_acc= 0.78000 time= 0.09006
Epoch: 0114 train_loss= 0.79866 train_acc= 0.92857 val_loss= 1.23075 val_acc= 0.78000 time= 0.09115
Epoch: 0115 train_loss= 0.80150 train_acc= 0.94286 val_loss= 1.22764 val_acc= 0.78000 time= 0.08806
Epoch: 0116 train_loss= 0.81792 train_acc= 0.97143 val_loss= 1.22439 val_acc= 0.78000 time= 0.08923
Epoch: 0117 train_loss= 0.78448 train_acc= 0.95000 val_loss= 1.22124 val_acc= 0.78400 time= 0.09307
Epoch: 0118 train_loss= 0.79777 train_acc= 0.95000 val_loss= 1.21824 val_acc= 0.78000 time= 0.09217
Epoch: 0119 train_loss= 0.77666 train_acc= 0.95714 val_loss= 1.21523 val_acc= 0.78200 time= 0.08906
Epoch: 0120 train_loss= 0.77692 train_acc= 0.97143 val_loss= 1.21201 val_acc= 0.78200 time= 0.09240
Epoch: 0121 train_loss= 0.77942 train_acc= 0.95000 val_loss= 1.20875 val_acc= 0.78400 time= 0.08906
Epoch: 0122 train_loss= 0.78487 train_acc= 0.94286 val_loss= 1.20480 val_acc= 0.78200 time= 0.09008
Epoch: 0123 train_loss= 0.76759 train_acc= 0.95000 val_loss= 1.20085 val_acc= 0.78200 time= 0.09205
Epoch: 0124 train_loss= 0.74731 train_acc= 0.95000 val_loss= 1.19699 val_acc= 0.78000 time= 0.09106
Epoch: 0125 train_loss= 0.75950 train_acc= 0.95000 val_loss= 1.19287 val_acc= 0.78000 time= 0.09011
Epoch: 0126 train_loss= 0.75599 train_acc= 0.95714 val_loss= 1.18858 val_acc= 0.78000 time= 0.09225
Epoch: 0127 train_loss= 0.74233 train_acc= 0.95000 val_loss= 1.18441 val_acc= 0.78000 time= 0.08906
Epoch: 0128 train_loss= 0.75403 train_acc= 0.95714 val_loss= 1.18006 val_acc= 0.78000 time= 0.09007
Epoch: 0129 train_loss= 0.76155 train_acc= 0.94286 val_loss= 1.17581 val_acc= 0.78000 time= 0.09384
Epoch: 0130 train_loss= 0.74934 train_acc= 0.93571 val_loss= 1.17175 val_acc= 0.78000 time= 0.08714
Epoch: 0131 train_loss= 0.76718 train_acc= 0.94286 val_loss= 1.16783 val_acc= 0.78200 time= 0.08804
Epoch: 0132 train_loss= 0.74461 train_acc= 0.95000 val_loss= 1.16445 val_acc= 0.78200 time= 0.09208
Epoch: 0133 train_loss= 0.72737 train_acc= 0.95000 val_loss= 1.16198 val_acc= 0.78200 time= 0.08806
Epoch: 0134 train_loss= 0.72769 train_acc= 0.95000 val_loss= 1.16005 val_acc= 0.78200 time= 0.09005
Epoch: 0135 train_loss= 0.73893 train_acc= 0.94286 val_loss= 1.15833 val_acc= 0.78200 time= 0.09307
Epoch: 0136 train_loss= 0.70035 train_acc= 0.95714 val_loss= 1.15682 val_acc= 0.78000 time= 0.08826
Epoch: 0137 train_loss= 0.79603 train_acc= 0.93571 val_loss= 1.15521 val_acc= 0.78200 time= 0.08806
Epoch: 0138 train_loss= 0.71783 train_acc= 0.97143 val_loss= 1.15365 val_acc= 0.78200 time= 0.09208
Epoch: 0139 train_loss= 0.72414 train_acc= 0.93571 val_loss= 1.15218 val_acc= 0.78200 time= 0.09004
Epoch: 0140 train_loss= 0.76024 train_acc= 0.92857 val_loss= 1.15087 val_acc= 0.78000 time= 0.11088
Epoch: 0141 train_loss= 0.71716 train_acc= 0.94286 val_loss= 1.15020 val_acc= 0.78400 time= 0.11208
Epoch: 0142 train_loss= 0.65483 train_acc= 0.95000 val_loss= 1.14929 val_acc= 0.78600 time= 0.11355
Epoch: 0143 train_loss= 0.70601 train_acc= 0.97857 val_loss= 1.14833 val_acc= 0.78600 time= 0.09307
Epoch: 0144 train_loss= 0.75722 train_acc= 0.96429 val_loss= 1.14718 val_acc= 0.78600 time= 0.10007
Epoch: 0145 train_loss= 0.70279 train_acc= 0.95714 val_loss= 1.14563 val_acc= 0.78600 time= 0.08833
Epoch: 0146 train_loss= 0.68137 train_acc= 0.95714 val_loss= 1.14390 val_acc= 0.78600 time= 0.09818
Epoch: 0147 train_loss= 0.70446 train_acc= 0.92143 val_loss= 1.14202 val_acc= 0.78600 time= 0.09124
Epoch: 0148 train_loss= 0.67626 train_acc= 0.96429 val_loss= 1.13986 val_acc= 0.78600 time= 0.09114
Epoch: 0149 train_loss= 0.70559 train_acc= 0.99286 val_loss= 1.13795 val_acc= 0.78600 time= 0.09907
Epoch: 0150 train_loss= 0.65854 train_acc= 0.96429 val_loss= 1.13567 val_acc= 0.78600 time= 0.09224
Epoch: 0151 train_loss= 0.69488 train_acc= 0.97143 val_loss= 1.13300 val_acc= 0.78400 time= 0.09018
Epoch: 0152 train_loss= 0.68918 train_acc= 0.97857 val_loss= 1.13042 val_acc= 0.78400 time= 0.09325
Epoch: 0153 train_loss= 0.73951 train_acc= 0.92143 val_loss= 1.12752 val_acc= 0.78400 time= 0.09307
Epoch: 0154 train_loss= 0.65691 train_acc= 0.97857 val_loss= 1.12448 val_acc= 0.78400 time= 0.09213
Epoch: 0155 train_loss= 0.68707 train_acc= 0.97143 val_loss= 1.12171 val_acc= 0.78600 time= 0.09107
Epoch: 0156 train_loss= 0.70395 train_acc= 0.97143 val_loss= 1.11998 val_acc= 0.78600 time= 0.09609
Epoch: 0157 train_loss= 0.67509 train_acc= 0.96429 val_loss= 1.11802 val_acc= 0.78600 time= 0.08905
Epoch: 0158 train_loss= 0.70231 train_acc= 0.94286 val_loss= 1.11607 val_acc= 0.78600 time= 0.09194
Epoch: 0159 train_loss= 0.65953 train_acc= 0.97143 val_loss= 1.11402 val_acc= 0.78400 time= 0.09507
Epoch: 0160 train_loss= 0.70041 train_acc= 0.97143 val_loss= 1.11227 val_acc= 0.78400 time= 0.08906
Epoch: 0161 train_loss= 0.70023 train_acc= 0.97143 val_loss= 1.11047 val_acc= 0.78200 time= 0.09011
Epoch: 0162 train_loss= 0.68871 train_acc= 0.95714 val_loss= 1.10819 val_acc= 0.78400 time= 0.10229
Epoch: 0163 train_loss= 0.65557 train_acc= 0.98571 val_loss= 1.10623 val_acc= 0.78200 time= 0.08943
Epoch: 0164 train_loss= 0.73047 train_acc= 0.93571 val_loss= 1.10486 val_acc= 0.78000 time= 0.09106
Epoch: 0165 train_loss= 0.68565 train_acc= 0.95714 val_loss= 1.10370 val_acc= 0.78000 time= 0.10022
Epoch: 0166 train_loss= 0.65343 train_acc= 0.97143 val_loss= 1.10239 val_acc= 0.78000 time= 0.09363
Epoch: 0167 train_loss= 0.70125 train_acc= 0.97143 val_loss= 1.10147 val_acc= 0.78200 time= 0.08913
Epoch: 0168 train_loss= 0.69909 train_acc= 0.95000 val_loss= 1.10069 val_acc= 0.78000 time= 0.09407
Epoch: 0169 train_loss= 0.65012 train_acc= 0.96429 val_loss= 1.10006 val_acc= 0.78200 time= 0.09409
Epoch: 0170 train_loss= 0.66773 train_acc= 0.95000 val_loss= 1.09972 val_acc= 0.78200 time= 0.09122
Epoch: 0171 train_loss= 0.72109 train_acc= 0.92857 val_loss= 1.09840 val_acc= 0.78200 time= 0.09825
Epoch: 0172 train_loss= 0.67563 train_acc= 0.95714 val_loss= 1.09644 val_acc= 0.78200 time= 0.09607
Epoch: 0173 train_loss= 0.64704 train_acc= 0.97143 val_loss= 1.09398 val_acc= 0.78200 time= 0.09307
Epoch: 0174 train_loss= 0.58342 train_acc= 0.98571 val_loss= 1.09138 val_acc= 0.77800 time= 0.09006
Epoch: 0175 train_loss= 0.67515 train_acc= 0.94286 val_loss= 1.08887 val_acc= 0.77400 time= 0.09832
Epoch: 0176 train_loss= 0.68394 train_acc= 0.93571 val_loss= 1.08582 val_acc= 0.77800 time= 0.09232
Epoch: 0177 train_loss= 0.70085 train_acc= 0.94286 val_loss= 1.08304 val_acc= 0.77800 time= 0.08814
Epoch: 0178 train_loss= 0.60540 train_acc= 0.98571 val_loss= 1.08044 val_acc= 0.77800 time= 0.08908
Epoch: 0179 train_loss= 0.63127 train_acc= 0.95000 val_loss= 1.07856 val_acc= 0.78200 time= 0.09121
Epoch: 0180 train_loss= 0.69479 train_acc= 0.93571 val_loss= 1.07661 val_acc= 0.78200 time= 0.09005
Epoch: 0181 train_loss= 0.62900 train_acc= 0.97857 val_loss= 1.07482 val_acc= 0.78600 time= 0.09110
Epoch: 0182 train_loss= 0.64596 train_acc= 0.92857 val_loss= 1.07334 val_acc= 0.78600 time= 0.09413
Epoch: 0183 train_loss= 0.59649 train_acc= 0.97857 val_loss= 1.07162 val_acc= 0.78400 time= 0.09027
Epoch: 0184 train_loss= 0.64177 train_acc= 0.96429 val_loss= 1.07015 val_acc= 0.78400 time= 0.09206
Epoch: 0185 train_loss= 0.61356 train_acc= 0.96429 val_loss= 1.06902 val_acc= 0.78400 time= 0.09514
Epoch: 0186 train_loss= 0.64748 train_acc= 0.95000 val_loss= 1.06780 val_acc= 0.78600 time= 0.09006
Epoch: 0187 train_loss= 0.63458 train_acc= 0.96429 val_loss= 1.06619 val_acc= 0.78800 time= 0.09219
Epoch: 0188 train_loss= 0.60758 train_acc= 0.97143 val_loss= 1.06476 val_acc= 0.78800 time= 0.10107
Epoch: 0189 train_loss= 0.63303 train_acc= 0.95714 val_loss= 1.06355 val_acc= 0.78800 time= 0.11807
Epoch: 0190 train_loss= 0.62635 train_acc= 0.98571 val_loss= 1.06231 val_acc= 0.78400 time= 0.09707
Epoch: 0191 train_loss= 0.60898 train_acc= 0.98571 val_loss= 1.06063 val_acc= 0.78200 time= 0.08906
Epoch: 0192 train_loss= 0.63756 train_acc= 0.95714 val_loss= 1.05901 val_acc= 0.77800 time= 0.09024
Epoch: 0193 train_loss= 0.62371 train_acc= 0.94286 val_loss= 1.05767 val_acc= 0.77800 time= 0.09017
Epoch: 0194 train_loss= 0.60151 train_acc= 0.96429 val_loss= 1.05636 val_acc= 0.77800 time= 0.08806
Epoch: 0195 train_loss= 0.60843 train_acc= 0.95714 val_loss= 1.05533 val_acc= 0.77800 time= 0.09127
Epoch: 0196 train_loss= 0.59138 train_acc= 0.97143 val_loss= 1.05411 val_acc= 0.78000 time= 0.09612
Epoch: 0197 train_loss= 0.59821 train_acc= 0.97857 val_loss= 1.05297 val_acc= 0.78000 time= 0.09718
Epoch: 0198 train_loss= 0.60693 train_acc= 0.97143 val_loss= 1.05188 val_acc= 0.77800 time= 0.09016
Epoch: 0199 train_loss= 0.60899 train_acc= 0.95714 val_loss= 1.05047 val_acc= 0.77800 time= 0.09311
Epoch: 0200 train_loss= 0.59147 train_acc= 0.97143 val_loss= 1.04964 val_acc= 0.77800 time= 0.08811
Optimization Finished!
Test set results: cost= 1.01263 accuracy= 0.81400 time= 0.04103

Process finished with exit code 0
