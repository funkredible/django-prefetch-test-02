# django-prefetch-test-01

prefetchとone-to-many-to-manyの簡単なテスト。
views.pyのindex1ではprefetchを使用し、index2ではprefetchを使用していない。
granpa.htmlで子テーブルにアクセスしている。
index1、index2それぞれのSQLの発行のされ方が異なる。
index2ではgranpa.htmlで子テーブルアクセス時にSQLが発行される。

Modelクラスの外部キーにrelated_nameを使うことで任意のプロパティ名を使用可能（models.py、granpa.htmlを参照）。

子テーブルをprefetchする場合の記述。
（デフォルト）Granpa.objects.all().prefetch_related('papa_set')
（設定後）Granpa.objects.all().prefetch_related('papas')

子テーブルのさらに子テーブル
（デフォルト）Granpa.objects.all().prefetch_related('papa_set__child_set')
（設定後）Granpa.objects.all().prefetch_related('papas__children')

