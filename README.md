# django-prefetch-test-01

prefetchとone-to-many-to-manyの簡単なテスト。
views.pyのindex1ではprefetchを使用し、index2ではprefetchを使用していない。
granpa.htmlで子テーブルにアクセスしている。
index1、index2それぞれのSQLの発行のされ方の違いが確認できる。

子テーブルをprefetchする場合の記述はデフォルトでは以下
Granpa.objects.all().prefetch_related('papa_set')

子テーブルのさらに子テーブル
Granpa.objects.all().prefetch_related('papa_set__child_set')

