Shiftless Collatz Model
Binary Interference in the 3n+LSB Trajectory
Author: Hiroshi Harada
Date: March 21, 2026
License: Documents (CC BY 4.0), Code (MIT)

概要
Shiftless Collatz モデルは、従来の Collatz 写像から右シフト操作（n/2）を完全に取り除いた新しい写像である。
最下位ビット（LSB）を捨てる代わりに、そのビットの重み 2^v をそのまま加算する。
n_{k+1} = 3 n_k + LSB(n_k)
LSB(n_k) = 2^v
ここで v は n_k の最下位の 1 ビットの位置（LSB の指数）である。
この変更により、ビット情報が一切失われず、軌道全体を 2 次元のビットキャンバスとして可視化できる。
その結果、標準 Collatz では見えないフラクタル構造、キャリー雪崩、干渉パターンが明瞭に現れる。
本リポジトリには以下が含まれる。
- Shiftless Collatz モデルの Python 実装
- 軌道およびビット構造の可視化
- 研究レポート（日本語・英語）
- モデルの挙動を示す図（Figures 1–5）

主な発見
- 標準 Collatz モデルとの同値性
- 各ステップの奇数部分が完全に一致する
- 2 の冪（ジャックポット）に到達するステップ数が、標準 Collatz の奇数部分 1 に到達するステップ数と一致する
（Figure 1）
- キャリー雪崩とフラクタル構造
- 低位ビットが急速に消滅
- 高位ビットにシェルピンスキーガスケット状の構造
- 軌道全体に複雑な干渉パターン
（Figure 2）
- Reach と Fill の二段階構造
- Reach: n → 3n
- Fill: 3n → 3n + LSB
（Figure 3）
- 3n / 3n+1 / 3n+LSB の同期比較
- 3n: きれいなガスケット構造
- 3n+1: わずかに歪むが類似
- 3n+LSB: LSB の重みにより構造が崩壊し干渉縞が発生
（Figure 4）
- 軌道の線形分解と干渉幾何学
n_k = 3(k-1-i) L_i
- 成分 A: 初期シードの幾何学的拡大
- 成分 B: LSB の累積寄与
- 干渉: A と B が同じビット位置で重なるとキャリーが発生しビットが消滅
（Figure 5）

リポジトリ構成
/code
code_01_collatz_shiftless_equivalence.py
code_02_collatz_shiftless_compact.py
code_03_collatz_shiftless_full.py
code_04_collatz_shiftless_comparison.py
code_05_collatz_shiftless_decomposition.py
/docs
Title_Collatz_Shiftless.pdf
Report_EN_Collatz_Shiftless.pdf
Report_JP_Collatz_Shiftless.pdf
README_EN
README_JP
LICENSE
LICENSE-CC-BY-4.0

必要環境
Python 3.9 以上
NumPy
Matplotlib
依存関係のインストール:
pip install numpy matplotlib

可視化の実行方法
例:
python code_02_collatz_shiftless_compact.py
各スクリプトは研究レポートに対応する図を生成する。

ライセンス
ドキュメント: CC BY 4.0
コード: MIT License
Copyright (c) 2026 Hiroshi Harada

引用
Harada, Hiroshi (2026).
"Shiftless Collatz Model: Binary Interference in the 3n + LSB Trajectory."
Zenodo. DOI: (to be assigned)
