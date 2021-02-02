#!/usr/bin/env bash
WORK_PATH=$(pwd)
USER=`whoami`
HOST=`hostname`

# ここから existing node の属性予測の実験

# repeat1_attribute_prediction_exist_PTS_utilize_disappeared学習
cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/Baseline
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/EGCNh
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/EGCNo
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/GCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/LSTM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/Random
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/STGCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/STGGNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/DynGEM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_disappeared/FNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Evaluation
CURRENT_DIR=`pwd`
EXEC="python repeat1_attribute_prediction_exist_PTS_utilize_disappeared.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="




# repeat1_attribute_prediction_exist_PTS_utilize_lost学習
cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/Baseline
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/EGCNh
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/EGCNo
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/GCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/LSTM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/Random
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/STGCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/STGGNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/DynGEM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_lost/FNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Evaluation
CURRENT_DIR=`pwd`
EXEC="python repeat1_attribute_prediction_exist_PTS_utilize_lost.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="




# repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link学習
cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/Baseline
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/EGCNh
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/EGCNo
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/GCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/LSTM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/Random
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/STGCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/STGGNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/DynGEM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link/FNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Evaluation
CURRENT_DIR=`pwd`
EXEC="python repeat1_attribute_prediction_exist_PTS_utilize_new_attribute_link.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="





# repeat1_attribute_prediction_exist_PTS_utilize_all学習
cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/Baseline
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/EGCNh
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/EGCNo
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/GCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/LSTM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/Random
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/STGCN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

#cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/STGGNN
#CURRENT_DIR=`pwd`
#EXEC="python main.py"
#NOW=`date`
#echo "==============start: ${NOW}=============="
#echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
#$EXEC
#NOW=`date`
#echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/DynGEM
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Model/repeat1_attribute_prediction_exist_PTS_utilize_all/FNN
CURRENT_DIR=`pwd`
EXEC="python main.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="

cd $WORK_PATH/Evaluation
CURRENT_DIR=`pwd`
EXEC="python repeat1_attribute_prediction_exist_PTS_utilize_all.py"
NOW=`date`
echo "==============start: ${NOW}=============="
echo "${USER}@${HOST}:${CURRENT_DIR}$ ${EXEC}"
$EXEC
NOW=`date`
echo "==============end: ${NOW}=============="