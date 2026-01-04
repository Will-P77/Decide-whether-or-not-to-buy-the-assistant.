import numpy as np
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder


df = pd.read_csv('shopping_data.csv')

df['item_name'] = df['item_name'].fillna('')

num_cols = ['current_price']
other_num_cols = ['discount']
cat_cols = ['category']
text_cols = 'item_name'

x = df.drop(columns=['label'], axis=1)
y = df['label']


num_pipeline = Pipeline([
    ('log', FunctionTransformer(np.log1p, validate=False, feature_names_out='one-to-one')),
    ('scaler', StandardScaler()),
])

cat_pipeline = Pipeline([
    ('onehot', OneHotEncoder(handle_unknown='ignore')),
])

other_pipeline = Pipeline([
    ('scaler', StandardScaler()),
])

text_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
])


preprocessor_add_text = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols),
    ('tfidf', text_pipeline, text_cols), # 这里的 key 是 tfidf
    ('other_num', other_pipeline, other_num_cols)
], remainder='drop')


final_model = Pipeline([
    ('preprocessor', preprocessor_add_text),
    ('clf', LogisticRegression(max_iter=2000, random_state=42)),
])

final_model.fit(x, y)

joblib.dump(final_model, 'model.joblib')

print("保存成功")