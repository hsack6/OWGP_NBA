ROOT_PATH = "/Users/shohei/work/NBA"
L = 3
ratio_test = 0.1
ratio_valid = 0.2

all_node_num = 3859
n_expanded = 117 # (MakeSample/link_prediction_newで確認できる)
adj_shape = (all_node_num, all_node_num * L)
max_nnz_am = 22108 # 隣接疎行列の全サンプルにおける非ゼロ要素数の最大値（Model/confirm_max_nnz_amで確認できる）
attribute_dim = 35

######################################################################################################################
# ディレクトリ名の定義

# MakeSample IO dir
# prediction_num_of_edge
MakeSample_prediction_num_of_edge_InputDir = ROOT_PATH + "/data/graph"
MakeSample_prediction_num_of_edge_OutputDir = ROOT_PATH + "/data/learning_data/prediction_num_of_edge"
# prediction_num_of_node
MakeSample_prediction_num_of_node_InputDir = ROOT_PATH + "/data/graph"
MakeSample_prediction_num_of_node_OutputDir = ROOT_PATH + "/data/learning_data/prediction_num_of_node"
# link_prediction_appeared
MakeSample_link_prediction_appeared_InputDir = ROOT_PATH + "/data/graph"
MakeSample_link_prediction_appeared_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_appeared"
# link_prediction_disappeared
MakeSample_link_prediction_disappeared_InputDir = ROOT_PATH + "/data/graph"
MakeSample_link_prediction_disappeared_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_disappeared"
# node_prediction_lost
MakeSample_node_prediction_lost_InputDir = ROOT_PATH + "/data/graph"
MakeSample_node_prediction_lost_OutputDir = ROOT_PATH + "/data/learning_data/node_prediction_lost"
# attribute_prediction_exist
MakeSample_attribute_prediction_exist_InputDir = ROOT_PATH + "/data/graph"
MakeSample_attribute_prediction_exist_PTS_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_exist_PTS"
MakeSample_attribute_prediction_exist_Age_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_exist_Age"
MakeSample_attribute_prediction_exist_Tm_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_exist_Tm"
MakeSample_attribute_prediction_exist_Pos_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_exist_Pos"
# attribute_prediction_new
MakeSample_attribute_prediction_new_InputDir = ROOT_PATH + "/data/graph"
MakeSample_attribute_prediction_new_OutputDir = ROOT_PATH + "/data/learning_data/attribute_prediction_new"
# link_prediction_new
MakeSample_link_prediction_new_InputDir = ROOT_PATH + "/data/graph"
MakeSample_link_prediction_new_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new"
MakeSample_link_prediction_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new/Baseline"
MakeSample_link_prediction_new_DeepMatchMax_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new/DeepMatchMax"
MakeSample_link_prediction_new_FNN_OutputDir = ROOT_PATH + "/data/learning_data/link_prediction_new/FNN"


# Model IO dir
# prediction_num_of_edge
# Baseline
Model_prediction_num_of_edge_InputDir = MakeSample_prediction_num_of_edge_OutputDir
Model_prediction_num_of_edge_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/new/Baseline"
Model_prediction_num_of_edge_appeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/appeared/Baseline"
Model_prediction_num_of_edge_disappeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/disappeared/Baseline"
# LSTM
Model_prediction_num_of_edge_InputDir = MakeSample_prediction_num_of_edge_OutputDir
Model_prediction_num_of_edge_new_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/new/LSTM"
Model_prediction_num_of_edge_appeared_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/appeared/LSTM"
Model_prediction_num_of_edge_disappeared_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_edge/disappeared/LSTM"

# prediction_num_of_node
# Baseline
Model_prediction_num_of_node_InputDir = MakeSample_prediction_num_of_node_OutputDir
Model_prediction_num_of_node_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/new/Baseline"
Model_prediction_num_of_node_lost_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/lost/Baseline"
# LSTM
Model_prediction_num_of_node_InputDir = MakeSample_prediction_num_of_node_OutputDir
Model_prediction_num_of_node_new_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/new/LSTM"
Model_prediction_num_of_node_lost_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/prediction_num_of_node/lost/LSTM"

# link_prediction_appeared
Model_link_prediction_appeared_InputDir = MakeSample_link_prediction_appeared_OutputDir
Model_link_prediction_appeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/Baseline"
Model_link_prediction_appeared_Random_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/Random"
Model_link_prediction_appeared_COSSIMMLP_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/COSSIMMLP"
Model_link_prediction_appeared_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_appeared/STGGNN"

# link_prediction_disappeared
Model_link_prediction_disappeared_InputDir = MakeSample_link_prediction_disappeared_OutputDir
Model_link_prediction_disappeared_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/Baseline"
Model_link_prediction_disappeared_Random_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/Random"
Model_link_prediction_disappeared_COSSIMMLP_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/COSSIMMLP"
Model_link_prediction_disappeared_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_disappeared/STGGNN"

# node_prediction_lost
Model_node_prediction_lost_InputDir = MakeSample_node_prediction_lost_OutputDir
Model_node_prediction_lost_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/Baseline"
Model_node_prediction_lost_Random_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/Random"
Model_node_prediction_lost_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/LSTM"
Model_node_prediction_lost_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/node_prediction_lost/STGGNN"

# attribute_prediction_exist
Model_attribute_prediction_exist_PTS_InputDir = MakeSample_attribute_prediction_exist_PTS_OutputDir
Model_attribute_prediction_exist_PTS_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_PTS/Baseline"
Model_attribute_prediction_exist_PTS_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_PTS/LSTM"
Model_attribute_prediction_exist_PTS_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_PTS/STGGNN"

Model_attribute_prediction_exist_Age_InputDir = MakeSample_attribute_prediction_exist_Age_OutputDir
Model_attribute_prediction_exist_Age_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Age/Baseline"
Model_attribute_prediction_exist_Age_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Age/LSTM"
Model_attribute_prediction_exist_Age_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Age/STGGNN"

Model_attribute_prediction_exist_Tm_InputDir = MakeSample_attribute_prediction_exist_Tm_OutputDir
Model_attribute_prediction_exist_Tm_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Tm/Baseline"
Model_attribute_prediction_exist_Tm_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Tm/LSTM"
Model_attribute_prediction_exist_Tm_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Tm/STGGNN"

Model_attribute_prediction_exist_Pos_InputDir = MakeSample_attribute_prediction_exist_Pos_OutputDir
Model_attribute_prediction_exist_Pos_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Pos/Baseline"
Model_attribute_prediction_exist_Pos_LSTM_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Pos/LSTM"
Model_attribute_prediction_exist_Pos_STGGNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_exist_Pos/STGGNN"

# attribute_prediction_new
Model_attribute_prediction_new_InputDir = MakeSample_attribute_prediction_new_OutputDir
Model_attribute_prediction_new_Baseline_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new/Baseline"
Model_attribute_prediction_new_FNN_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new/FNN"
Model_attribute_prediction_new_DeepMatchMax_OutputDir = ROOT_PATH + "/data/learning_result/attribute_prediction_new/DeepMatchMax"

# link_prediction_new
Model_link_prediction_new_Baseline_mix_InputDir = MakeSample_link_prediction_new_Baseline_OutputDir + "/mix"
Model_link_prediction_new_Baseline_learning_InputDir = MakeSample_link_prediction_new_Baseline_OutputDir + "/learning"
Model_link_prediction_new_Baseline_inference_InputDir = MakeSample_link_prediction_new_Baseline_OutputDir + "/inference"

Model_link_prediction_new_DeepMatchMax_mix_InputDir = MakeSample_link_prediction_new_DeepMatchMax_OutputDir + "/mix"
Model_link_prediction_new_DeepMatchMax_learning_InputDir = MakeSample_link_prediction_new_DeepMatchMax_OutputDir + "/learning"
Model_link_prediction_new_DeepMatchMax_inference_InputDir = MakeSample_link_prediction_new_DeepMatchMax_OutputDir + "/inference"

Model_link_prediction_new_FNN_mix_InputDir = MakeSample_link_prediction_new_FNN_OutputDir + "/mix"
Model_link_prediction_new_FNN_learning_InputDir = MakeSample_link_prediction_new_FNN_OutputDir + "/learning"
Model_link_prediction_new_FNN_inference_InputDir = MakeSample_link_prediction_new_FNN_OutputDir + "/inference"

Model_link_prediction_new_COSSIMMLP_Baseline_mix_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/Baseline/mix"
Model_link_prediction_new_COSSIMMLP_Baseline_learning_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/Baseline/learning"
Model_link_prediction_new_COSSIMMLP_Baseline_inference_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/Baseline/inference"

Model_link_prediction_new_COSSIMMLP_DeepMatchMax_mix_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/DeepMatchMax/mix"
Model_link_prediction_new_COSSIMMLP_DeepMatchMax_learning_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/DeepMatchMax/learning"
Model_link_prediction_new_COSSIMMLP_DeepMatchMax_inference_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/DeepMatchMax/inference"

Model_link_prediction_new_COSSIMMLP_FNN_mix_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/FNN/mix"
Model_link_prediction_new_COSSIMMLP_FNN_learning_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/FNN/learning"
Model_link_prediction_new_COSSIMMLP_FNN_inference_OutputDir = ROOT_PATH + "/data/learning_result/link_prediction_new/COSSIMMLP/FNN/inference"


# Evaluation IO dir
# prediction_num_of_edge
# Baseline
Evaluation_prediction_num_of_edge_new_Baseline_InputDir = Model_prediction_num_of_edge_new_Baseline_OutputDir
Evaluation_prediction_num_of_edge_appeared_Baseline_InputDir = Model_prediction_num_of_edge_appeared_Baseline_OutputDir
Evaluation_prediction_num_of_edge_disappeared_Baseline_InputDir = Model_prediction_num_of_edge_disappeared_Baseline_OutputDir
# LSTM
Evaluation_prediction_num_of_edge_new_LSTM_InputDir = Model_prediction_num_of_edge_new_LSTM_OutputDir
Evaluation_prediction_num_of_edge_appeared_LSTM_InputDir = Model_prediction_num_of_edge_appeared_LSTM_OutputDir
Evaluation_prediction_num_of_edge_disappeared_LSTM_InputDir = Model_prediction_num_of_edge_disappeared_LSTM_OutputDir
Evaluation_prediction_num_of_edge_new_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_edge/new"
Evaluation_prediction_num_of_edge_appeared_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_edge/appeared"
Evaluation_prediction_num_of_edge_disappeared_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_edge/disappeared"

# prediction_num_of_node
# Baseline
Evaluation_prediction_num_of_node_new_Baseline_InputDir = Model_prediction_num_of_node_new_Baseline_OutputDir
Evaluation_prediction_num_of_node_lost_Baseline_InputDir = Model_prediction_num_of_node_lost_Baseline_OutputDir
# LSTM
Evaluation_prediction_num_of_node_new_LSTM_InputDir = Model_prediction_num_of_node_new_LSTM_OutputDir
Evaluation_prediction_num_of_node_lost_LSTM_InputDir = Model_prediction_num_of_node_lost_LSTM_OutputDir
Evaluation_prediction_num_of_node_new_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_node/new"
Evaluation_prediction_num_of_node_lost_OutputDir = ROOT_PATH + "/data/result/prediction_num_of_node/lost"

# link_prediction_appeared
Evaluation_link_prediction_appeared_Baseline_InputDir = Model_link_prediction_appeared_Baseline_OutputDir
Evaluation_link_prediction_appeared_Random_InputDir = Model_link_prediction_appeared_Random_OutputDir
Evaluation_link_prediction_appeared_COSSIMMLP_InputDir = Model_link_prediction_appeared_COSSIMMLP_OutputDir
Evaluation_link_prediction_appeared_STGGNN_InputDir = Model_link_prediction_appeared_STGGNN_OutputDir
Evaluation_link_prediction_appeared_OutputDir = ROOT_PATH + "/data/result/link_prediction_appeared"

# link_prediction_disappeared
Evaluation_link_prediction_disappeared_Baseline_InputDir = Model_link_prediction_disappeared_Baseline_OutputDir
Evaluation_link_prediction_disappeared_Random_InputDir = Model_link_prediction_disappeared_Random_OutputDir
Evaluation_link_prediction_disappeared_COSSIMMLP_InputDir = Model_link_prediction_disappeared_COSSIMMLP_OutputDir
Evaluation_link_prediction_disappeared_STGGNN_InputDir = Model_link_prediction_disappeared_STGGNN_OutputDir
Evaluation_link_prediction_disappeared_OutputDir = ROOT_PATH + "/data/result/link_prediction_disappeared"

# node_prediction_lost
Evaluation_node_prediction_lost_Baseline_InputDir = Model_node_prediction_lost_Baseline_OutputDir
Evaluation_node_prediction_lost_Random_InputDir = Model_node_prediction_lost_Random_OutputDir
Evaluation_node_prediction_lost_LSTM_InputDir = Model_node_prediction_lost_LSTM_OutputDir
Evaluation_node_prediction_lost_STGGNN_InputDir = Model_node_prediction_lost_STGGNN_OutputDir
Evaluation_node_prediction_lost_OutputDir = ROOT_PATH + "/data/result/node_prediction_lost"

# attribute_prediction_exist
Evaluation_attribute_prediction_exist_PTS_Baseline_InputDir = Model_attribute_prediction_exist_PTS_Baseline_OutputDir
Evaluation_attribute_prediction_exist_PTS_LSTM_InputDir = Model_attribute_prediction_exist_PTS_LSTM_OutputDir
Evaluation_attribute_prediction_exist_PTS_STGGNN_InputDir = Model_attribute_prediction_exist_PTS_STGGNN_OutputDir
Evaluation_attribute_prediction_exist_PTS_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_exist_PTS"

Evaluation_attribute_prediction_exist_Age_Baseline_InputDir = Model_attribute_prediction_exist_Age_Baseline_OutputDir
Evaluation_attribute_prediction_exist_Age_LSTM_InputDir = Model_attribute_prediction_exist_Age_LSTM_OutputDir
Evaluation_attribute_prediction_exist_Age_STGGNN_InputDir = Model_attribute_prediction_exist_Age_STGGNN_OutputDir
Evaluation_attribute_prediction_exist_Age_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_exist_Age"

Evaluation_attribute_prediction_exist_Tm_Baseline_InputDir = Model_attribute_prediction_exist_Tm_Baseline_OutputDir
Evaluation_attribute_prediction_exist_Tm_LSTM_InputDir = Model_attribute_prediction_exist_Tm_LSTM_OutputDir
Evaluation_attribute_prediction_exist_Tm_STGGNN_InputDir = Model_attribute_prediction_exist_Tm_STGGNN_OutputDir
Evaluation_attribute_prediction_exist_Tm_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_exist_Tm"

Evaluation_attribute_prediction_exist_Pos_Baseline_InputDir = Model_attribute_prediction_exist_Pos_Baseline_OutputDir
Evaluation_attribute_prediction_exist_Pos_LSTM_InputDir = Model_attribute_prediction_exist_Pos_LSTM_OutputDir
Evaluation_attribute_prediction_exist_Pos_STGGNN_InputDir = Model_attribute_prediction_exist_Pos_STGGNN_OutputDir
Evaluation_attribute_prediction_exist_Pos_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_exist_Pos"

# attribute_prediction_new
Evaluation_attribute_prediction_new_Baseline_InputDir = Model_attribute_prediction_new_Baseline_OutputDir
Evaluation_attribute_prediction_new_FNN_InputDir = Model_attribute_prediction_new_FNN_OutputDir
Evaluation_attribute_prediction_new_DeepMatchMax_InputDir = Model_attribute_prediction_new_DeepMatchMax_OutputDir
Evaluation_attribute_prediction_new_OutputDir = ROOT_PATH + "/data/result/attribute_prediction_new"

# link_prediction_new
Evaluation_link_prediction_new_COSSIMMLP_Baseline_mix_InputDir = Model_link_prediction_new_COSSIMMLP_Baseline_mix_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_Baseline_learning_InputDir = Model_link_prediction_new_COSSIMMLP_Baseline_learning_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_Baseline_inference_InputDir = Model_link_prediction_new_COSSIMMLP_Baseline_inference_OutputDir

Evaluation_link_prediction_new_COSSIMMLP_DeepMatchMax_mix_InputDir = Model_link_prediction_new_COSSIMMLP_DeepMatchMax_mix_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_DeepMatchMax_learning_InputDir = Model_link_prediction_new_COSSIMMLP_DeepMatchMax_learning_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_DeepMatchMax_inference_InputDir = Model_link_prediction_new_COSSIMMLP_DeepMatchMax_inference_OutputDir

Evaluation_link_prediction_new_COSSIMMLP_FNN_mix_InputDir = Model_link_prediction_new_COSSIMMLP_FNN_mix_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_FNN_learning_InputDir = Model_link_prediction_new_COSSIMMLP_FNN_learning_OutputDir
Evaluation_link_prediction_new_COSSIMMLP_FNN_inference_InputDir = Model_link_prediction_new_COSSIMMLP_FNN_inference_OutputDir

Evaluation_link_prediction_new_OutputDir = ROOT_PATH + "/data/result/link_prediction_new"

# graph_prediction
Evaluation_graph_prediction_OutputDir = ROOT_PATH + "/data/result/graph_prediction"

######################################################################################################################
# モデルハイパラメータの定義

# prediction_num_of_edge
prediction_num_of_edge_worker = 2
prediction_num_of_edge_batchSize = 2
prediction_num_of_edge_state_dim = 1
prediction_num_of_edge_output_dim = 1
prediction_num_of_edge_init_L = L
prediction_num_of_edge_niter = 1000
prediction_num_of_edge_patience = 10
prediction_num_of_edge_lr = 0.01
prediction_num_of_edge_max_appeared = 1639
prediction_num_of_edge_min_appeared = 19
prediction_num_of_edge_max_disappeared = 1685
prediction_num_of_edge_min_disappeared = 15
prediction_num_of_edge_max_new = 1399
prediction_num_of_edge_min_new = 213

# prediction_num_of_node
prediction_num_of_node_worker = 2
prediction_num_of_node_batchSize = 2
prediction_num_of_node_state_dim = 1
prediction_num_of_node_output_dim = 1
prediction_num_of_node_init_L = L
prediction_num_of_node_niter = 1000
prediction_num_of_node_patience = 10
prediction_num_of_node_lr = 0.01
prediction_num_of_node_max_new = 117
prediction_num_of_node_min_new = 21
prediction_num_of_node_max_lost = 101
prediction_num_of_node_min_lost = 17

# link_prediction_appeared
link_prediction_appeared_worker = 2
link_prediction_appeared_batchSize = 2
link_prediction_appeared_state_dim = attribute_dim
link_prediction_appeared_annotation_dim = attribute_dim
link_prediction_appeared_output_dim = all_node_num
link_prediction_appeared_init_L = L
link_prediction_appeared_niter = 100
link_prediction_appeared_n_steps = 5
link_prediction_appeared_patience = 5
link_prediction_appeared_lr = 0.01

# link_prediction_disappeared
link_prediction_disappeared_worker = 2
link_prediction_disappeared_batchSize = 2
link_prediction_disappeared_state_dim = attribute_dim
link_prediction_disappeared_annotation_dim = attribute_dim
link_prediction_disappeared_output_dim = all_node_num
link_prediction_disappeared_init_L = L
link_prediction_disappeared_niter = 100
link_prediction_disappeared_n_steps = 5
link_prediction_disappeared_patience = 5
link_prediction_disappeared_lr = 0.01

# node_prediction_lost
node_prediction_lost_worker = 2
node_prediction_lost_batchSize = 2
node_prediction_lost_state_dim = attribute_dim
node_prediction_lost_annotation_dim = attribute_dim
node_prediction_lost_output_dim = 1
node_prediction_lost_init_L = L
node_prediction_lost_niter = 100
node_prediction_lost_n_steps = 5
node_prediction_lost_patience = 10
node_prediction_lost_lr = 0.01

# attribute_prediction_exist_Tm
attribute_prediction_exist_Tm_worker = 2
attribute_prediction_exist_Tm_batchSize = 2
attribute_prediction_exist_Tm_state_dim = attribute_dim
attribute_prediction_exist_Tm_annotation_dim = attribute_dim
attribute_prediction_exist_Tm_output_dim = 30
attribute_prediction_exist_Tm_init_L = L
attribute_prediction_exist_Tm_niter = 100
attribute_prediction_exist_Tm_n_steps = 5
attribute_prediction_exist_Tm_patience = 10
attribute_prediction_exist_Tm_lr = 0.01
attribute_prediction_exist_Tm_ID = 0
attribute_prediction_exist_Tm_idx = [i for i in range(30)]
attribute_prediction_exist_Tm_n_class = len(attribute_prediction_exist_Tm_idx)

# attribute_prediction_exist_Pos
attribute_prediction_exist_Pos_worker = 2
attribute_prediction_exist_Pos_batchSize = 2
attribute_prediction_exist_Pos_state_dim = attribute_dim
attribute_prediction_exist_Pos_annotation_dim = attribute_dim
attribute_prediction_exist_Pos_output_dim = 5
attribute_prediction_exist_Pos_init_L = L
attribute_prediction_exist_Pos_niter = 100
attribute_prediction_exist_Pos_n_steps = 5
attribute_prediction_exist_Pos_patience = 10
attribute_prediction_exist_Pos_lr = 0.01
attribute_prediction_exist_Pos_ID = 1
attribute_prediction_exist_Pos_idx = [i for i in range(30, 33)]
attribute_prediction_exist_Pos_n_class = len(attribute_prediction_exist_Pos_idx)

# attribute_prediction_exist_Age
attribute_prediction_exist_Age_worker = 2
attribute_prediction_exist_Age_batchSize = 2
attribute_prediction_exist_Age_state_dim = attribute_dim
attribute_prediction_exist_Age_annotation_dim = attribute_dim
attribute_prediction_exist_Age_output_dim = 1
attribute_prediction_exist_Age_init_L = L
attribute_prediction_exist_Age_niter = 100
attribute_prediction_exist_Age_n_steps = 5
attribute_prediction_exist_Age_patience = 10
attribute_prediction_exist_Age_lr = 0.01
attribute_prediction_exist_Age_mean = 26.5358227532985
attribute_prediction_exist_Age_std = 3.90389575522484
attribute_prediction_exist_Age_idx = [33]

# attribute_prediction_exist_PTS
attribute_prediction_exist_PTS_worker = 2
attribute_prediction_exist_PTS_batchSize = 2
attribute_prediction_exist_PTS_state_dim = attribute_dim
attribute_prediction_exist_PTS_annotation_dim = attribute_dim
attribute_prediction_exist_PTS_output_dim = 1
attribute_prediction_exist_PTS_init_L = L
attribute_prediction_exist_PTS_niter = 100
attribute_prediction_exist_PTS_n_steps = 5
attribute_prediction_exist_PTS_patience = 10
attribute_prediction_exist_PTS_lr = 0.01
attribute_prediction_exist_PTS_mean = 558.397908887229
attribute_prediction_exist_PTS_std = 510.751814658408
attribute_prediction_exist_PTS_idx = [34]

# attribute_prediction_new
attribute_prediction_new_worker = 2
attribute_prediction_new_batchSize = 2
attribute_prediction_new_d0 = attribute_dim
attribute_prediction_new_d1 = 64
attribute_prediction_new_d2 = 128
attribute_prediction_new_d3 = 1024
attribute_prediction_new_d4 = 512
attribute_prediction_new_d5 = 256
attribute_prediction_new_d6 = 128
attribute_prediction_new_init_L = L
attribute_prediction_new_niter = 100
attribute_prediction_new_patience = 10
attribute_prediction_new_lr = 0.01

# link_prediction_new
link_prediction_new_worker = 2
link_prediction_new_batchSize = 2
link_prediction_new_state_dim = attribute_dim
link_prediction_new_annotation_dim = attribute_dim
link_prediction_new_output_dim = all_node_num + n_expanded
link_prediction_new_init_L = L
link_prediction_new_niter = 1
link_prediction_new_n_steps = 5
link_prediction_new_patience = 3
link_prediction_new_lr = 0.01
