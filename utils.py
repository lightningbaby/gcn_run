import numpy as np
import pickle as pkl
import networkx as nx
import scipy.sparse as sp
from scipy.sparse.linalg.eigen.arpack import eigsh
import sys


def parse_index_file(filename):
    """Parse index file."""
    index = []
    for line in open(filename):
        index.append(int(line.strip()))#移除首尾空格，将index连接起来
    return index


def sample_mask(idx, l):
    """Create mask."""
    mask = np.zeros(l)
    mask[idx] = 1
    return np.array(mask, dtype=np.bool)


def load_data(dataset_str):
    """Load data."""
    names = ['x', 'y', 'tx', 'ty', 'allx', 'ally', 'graph']
    # print("names--load_data---in utils.py",names)
    objects = []
    for i in range(len(names)):
        with open("data/ind.{}.{}".format(dataset_str, names[i]), 'rb') as f:
            if sys.version_info > (3, 0):
                objects.append(pkl.load(f, encoding='latin1'))
            else:
                objects.append(pkl.load(f))

    x, y, tx, ty, allx, ally, graph = tuple(objects)
    # x是训练样例的特征向量，eg (0, 19)	1.0,有140个训练杨莉
    # y是训练样例的标签，即文章的分类，one-hot,一共7个分类,[0 0 0 1 0 0 0]
    # tx，ty 是测试样例 (0, 311)	1.0,[0 0 0 ..., 0 0 0]
    # allx，ally是所有样例
    # graph 是dict,格式{index:[邻居节点的index]} 顺序是allx的顺序，每一篇paper的邻居节点
    # defaultdict(<class 'list'>, {0: [633, 1862, 2582], 1: [2, 652, 654]... 2707: [598, 165, 1473, 2706]
    # print('x:')
    # print(x)
    # test_idx_reorder 是文件中Test样例的index
    test_idx_reorder = parse_index_file("data/ind.{}.test.index".format(dataset_str))#Test index
    # print('test_idx_reorder')
    # print(test_idx_reorder)
    test_idx_range = np.sort(test_idx_reorder)#测试样例的id,从1708到2707
    # print('test_idx_range')
    # print(test_idx_range)

    if dataset_str == 'citeseer':
        # Fix citeseer dataset (there are some isolated nodes in the graph)
        # Find isolated nodes, add them as zero-vecs into the right position
        test_idx_range_full = range(min(test_idx_reorder), max(test_idx_reorder)+1)
        tx_extended = sp.lil_matrix((len(test_idx_range_full), x.shape[1]))
        tx_extended[test_idx_range-min(test_idx_range), :] = tx
        tx = tx_extended
        ty_extended = np.zeros((len(test_idx_range_full), y.shape[1]))
        ty_extended[test_idx_range-min(test_idx_range), :] = ty
        ty = ty_extended

    features = sp.vstack((allx, tx)).tolil()#连接矩阵allx,tx，再转化为链表格式,2707个节点对应的引用，eg(2707, 1392)	1.0
    features[test_idx_reorder, :] = features[test_idx_range, :]# 将测试部分的index重新排序了 eg(2707, 1414)	1.0
    # print('features:')
    # print(features.shape[0])
    adj = nx.adjacency_matrix(nx.from_dict_of_lists(graph))#将graph转化为networkx的图，返回一个邻接矩阵,eg  (2707, 2706)	1
    labels = np.vstack((ally, ty))
    labels[test_idx_reorder, :] = labels[test_idx_range, :]#label是所有样例的

    idx_test = test_idx_range.tolist()#有1000个Test样例
    # print('idx_test:')
    # print(len(idx_test))
    idx_train = range(len(y))# range(0,140)，由140个训练样例
    # print('idx_train:')
    # print(len(idx_train))
    idx_val = range(len(y), len(y)+500)#用来valid的index ，有500个

    train_mask = sample_mask(idx_train, labels.shape[0]) #(2708,) [ True  True  True ..., False False False],shape[0]是labels的行数
    val_mask = sample_mask(idx_val, labels.shape[0])#2708行
    test_mask = sample_mask(idx_test, labels.shape[0])#2708行
    # print('train_mask:')
    # print(train_mask)
    # print('val_mask:')
    # print(val_mask)
    # print('test_mask:')
    # print(test_mask)


    y_train = np.zeros(labels.shape)
    y_val = np.zeros(labels.shape)
    y_test = np.zeros(labels.shape)
    y_train[train_mask, :] = labels[train_mask, :]
    y_val[val_mask, :] = labels[val_mask, :]
    y_test[test_mask, :] = labels[test_mask, :]

    #features 是（2702，,754）1.0的样式
    #y_train-- [[ 0.  0.  0. ...,  0.  0.  0.]
    #y_val-- [[ 0.  0.  0. ...,  0.  0.  0.]
    # y_test - - [[0.  0.  0...., 0.  0.  0.]
    # train_mask - - [True  True  True..., False False False]
    # val_mask - - [False False False..., False False False]
    # test_mask - - [False False False..., True  True  True]
    # features - -- (array([[0, 1274],, dtype=int32), array([ 0.11111111,  0.11111111,  0.11111111, ...,  0.07692308,
    # , dtype = float32), (2708, 1433))
    # print("before return--load_data-in utils.py-adj--",adj,"\ny_train--" , y_train,"\ny_val--" , y_val, "\n y_test--" ,y_test,"\n train_mask--" , train_mask, "\n val_mask--" ,val_mask,"\n test_mask--" , test_mask)
    return adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask


def sparse_to_tuple(sparse_mx):
    """Convert sparse matrix to tuple representation."""
    def to_tuple(mx):
        if not sp.isspmatrix_coo(mx):
            mx = mx.tocoo()
        coords = np.vstack((mx.row, mx.col)).transpose()
        values = mx.data
        shape = mx.shape
        return coords, values, shape

    if isinstance(sparse_mx, list):
        for i in range(len(sparse_mx)):
            sparse_mx[i] = to_tuple(sparse_mx[i])
    else:
        sparse_mx = to_tuple(sparse_mx)

    return sparse_mx


def preprocess_features(features):
    """Row-normalize feature matrix and convert to tuple representation"""
    rowsum = np.array(features.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    features = r_mat_inv.dot(features)
    return sparse_to_tuple(features)


def normalize_adj(adj):
    """Symmetrically normalize adjacency matrix."""
    adj = sp.coo_matrix(adj)#稀疏矩阵
    rowsum = np.array(adj.sum(1))#将输入数据转换为ndarray
    d_inv_sqrt = np.power(rowsum, -0.5).flatten()
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0.#判断是否无穷
    d_mat_inv_sqrt = sp.diags(d_inv_sqrt)
    return adj.dot(d_mat_inv_sqrt).transpose().dot(d_mat_inv_sqrt).tocoo()


def preprocess_adj(adj):
    """Preprocessing of adjacency matrix for simple GCN model and conversion to tuple representation."""
    adj_normalized = normalize_adj(adj + sp.eye(adj.shape[0]))#numpy.eye 生成对角矩阵
    return sparse_to_tuple(adj_normalized)


def construct_feed_dict(features, support, labels, labels_mask, placeholders):
    """Construct feed dictionary."""
    feed_dict = dict()
    feed_dict.update({placeholders['labels']: labels})
    feed_dict.update({placeholders['labels_mask']: labels_mask})
    feed_dict.update({placeholders['features']: features})
    feed_dict.update({placeholders['support'][i]: support[i] for i in range(len(support))})
    feed_dict.update({placeholders['num_features_nonzero']: features[1].shape})
    return feed_dict


def chebyshev_polynomials(adj, k):
    """Calculate Chebyshev polynomials up to order k. Return a list of sparse matrices (tuple representation)."""
    print("Calculating Chebyshev polynomials up to order {}...".format(k))

    adj_normalized = normalize_adj(adj)
    laplacian = sp.eye(adj.shape[0]) - adj_normalized
    largest_eigval, _ = eigsh(laplacian, 1, which='LM')
    scaled_laplacian = (2. / largest_eigval[0]) * laplacian - sp.eye(adj.shape[0])

    t_k = list()
    t_k.append(sp.eye(adj.shape[0]))
    t_k.append(scaled_laplacian)

    def chebyshev_recurrence(t_k_minus_one, t_k_minus_two, scaled_lap):
        s_lap = sp.csr_matrix(scaled_lap, copy=True)
        return 2 * s_lap.dot(t_k_minus_one) - t_k_minus_two

    for i in range(2, k+1):
        t_k.append(chebyshev_recurrence(t_k[-1], t_k[-2], scaled_laplacian))

    return sparse_to_tuple(t_k)
