# FNNとFNN_1の違い
FNNはnew nodeに接続されるリンクを学習対象としている。  
FNN_1はDEALの学習設定に揃えて評価する。trainもvalidもexisting node間のリンクで学習しており、validはネガティブ/ポジティブサンプリングされたノードペアで評価。