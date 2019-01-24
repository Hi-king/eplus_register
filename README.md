# eplus_register

1. クレカは事前に登録しておく
2. シリアル番号のファイルserial.txtを作っておく
3. config.yamlを作っておく
   * cardSelectorDOMは、開発者ツールとかで、実際に使うカードのDOMのID調べて書く必要があります

```
less serial.txt |while read line;do;for i in 2 3 4 5;do python run.py $line $i;done;done
```