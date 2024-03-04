# bentomlを利用したサンプルコード
import bentoml
from sklearn.base import BaseEstimator, TransformerMixin

# BentoMLを利用したモデルの作成
model: BaseEstimator = bentoml.sklearn.load_model("iris_clf:latest")

# モデル情報の取得
bento_model: bentoml.Model = bentoml.models.get("iris_clf:latest")

print(bento_model.name)
print(bento_model.version)
print(bento_model.tag)
print(bento_model.info.metadata)
print(bento_model.info.labels)

