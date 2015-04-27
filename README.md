# django-prefetch-test-01

prefetchとone-to-many-to-manyの簡単なテスト。
views.pyのindex1ではprefetchを使用し、index2ではprefetchを使用していない。
granpa.htmlで子テーブルにアクセスしている。
index1、index2それぞれのSQLの発行のされ方の違いが確認できる。
