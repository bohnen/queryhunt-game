[![Streamlitで開く](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://queryhunt-game.streamlit.app/)

# 🕵️‍♂️ QueryHunt - SQLミステリーゲーム

**QueryHunt**は、殺人ミステリーの興奮とAIの力を組み合わせたインタラクティブなSQLゲームです。オリジナルのSQL Murder Mysteryに触発されたこのプロジェクトでは、プレイヤーがAI生成データに対してSQLクエリを実行し、ユニークな事件を解決することに挑戦します。TiDBのハッカソンプロジェクトとして開発されたQueryHuntは、TiDB Serverless、GPT-4、その他の最新技術の可能性を示しています。

## アーキテクチャ

<img src="https://i.postimg.cc/G34Zdz22/Architecture.png"/>

## 特徴

- **魅力的なゲームプレイ:** プレイヤーはSQLクエリを使用してデータを探索し、動的に生成されたストーリー内で犯人を特定します。
- **AIによるヒント:** AIアシスタントが過去のクエリに基づいてヒントを提供し、正解への道筋を案内します。
- **モダンな技術スタック:** TiDB Serverless、GPT-4o mini、オープンソースライブラリを活用して、スムーズで最新の体験を提供します。
- **スケーラブルかつユニーク:** 各ゲームセッションはユニークで、新しいストーリーとデータが毎回生成され、プレイヤーに新たな挑戦を提供します。

## 技術スタック

- **TiDB Serverless:** AIが生成した一時的なゲームデータ（被害者、容疑者、証拠、アリバイなどのテーブル）を保存。
- **TiDB VectorSearch:** vs_game_schemaテーブルに保存されたスキーマ埋め込みを参照して、AIが有効なSQLクエリを生成。
- **Llama-Index:** ゲームデータの生成と検証のワークフローを管理し、自己修復プロセスも含む。
- **OpenAI:** GPT-4o miniモデルがユニークなゲームストーリー、データ、およびプレイヤー向けの個別ヒントを生成。
- **Streamlit:** SQLクエリを実行できるカスタムSQLエディタを含むユーザーインターフェースを提供。

## 仕組み

1. **ストーリー生成:** AIがユニークな殺人ミステリーストーリーを生成し、関連データをデータベースに入力。
2. **データ探索:** プレイヤーはSQLクエリを実行してデータを探索し、手がかりをつなぎ合わせて犯人を特定。
3. **ヒントシステム:** AIがプレイヤーのクエリ履歴に基づいてヒントを提供し、容疑者を絞り込む手助けをします。
4. **勝利条件:** プレイヤーが犯人を正しく特定するとゲーム終了。

## Llama-Indexワークフロー

以下は、複数のLLMコールと一時的なゲームデータをTiDB Serverlessに取り込むために使用されるLlama-Indexワークフローの図です。

<img src="https://i.postimg.cc/7LpS7xgj/Llama-Index-Workflow.png"/>

[YouTubeでデモ動画を見る](https://youtu.be/IEwo6FUG1PY)

## 始め方

QueryHuntをローカルでセットアップして実行するには:

1. **リポジトリをクローン:**
   このリポジトリを `git clone` してください。

2. **必要なパッケージをインストール:**
   ```bash
   cd queryhunt-game
   pip install -r requirements.txt
   ```

3. **以下のシークレットを自身の認証情報に置き換えます:**
   ```bash
   cd .streamlit
   mv secrets.toml.template secrets.toml
   vim secrets.toml
   ```

4. **データベースを初期化**
   ```bash
   python make_index.py
   python make_leaderboard.py
   ```

5. **エントリーポイントapp.pyを実行:**
   ```bash
   streamlit run app.py
   ```
